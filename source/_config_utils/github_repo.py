"""
WiP.

Soon.
"""

# region [Imports]

import os
import re
import sys
import json
import queue
import math
import base64
import pickle
import random
import shelve
import dataclasses
import shutil
import asyncio
import logging
import sqlite3
import platform
import importlib
import subprocess
import inspect

from time import sleep, process_time, process_time_ns, perf_counter, perf_counter_ns
from io import BytesIO, StringIO
from abc import ABC, ABCMeta, abstractmethod
from copy import copy, deepcopy
from enum import Enum, Flag, auto, unique
from time import time, sleep
from pprint import pprint, pformat
from pathlib import Path
from string import Formatter, digits, printable, whitespace, punctuation, ascii_letters, ascii_lowercase, ascii_uppercase
from timeit import Timer
from typing import TYPE_CHECKING, Union, Callable, Iterable, Optional, Mapping, Any, IO, TextIO, BinaryIO, Hashable, Generator, Literal, TypeVar, TypedDict, AnyStr
from zipfile import ZipFile, ZIP_LZMA
from datetime import datetime, timezone, timedelta
from tempfile import TemporaryDirectory
from textwrap import TextWrapper, fill, wrap, dedent, indent, shorten
from functools import wraps, partial, lru_cache, singledispatch, total_ordering, cached_property
from importlib import import_module, invalidate_caches
from contextlib import contextmanager, asynccontextmanager, nullcontext, closing, ExitStack, suppress
from statistics import mean, mode, stdev, median, variance, pvariance, harmonic_mean, median_grouped
from collections import Counter, ChainMap, deque, namedtuple, defaultdict
from urllib.parse import urlparse
from importlib.util import find_spec, module_from_spec, spec_from_file_location
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from importlib.machinery import SourceFileLoader
from yarl import URL
from github import Github
from github.GitTree import GitTree
from github.GitTreeElement import GitTreeElement
from github.Repository import Repository
from github.Branch import Branch
from github.Commit import Commit

from dotenv import load_dotenv
import requests
load_dotenv("github.env")
# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [Logging]


# endregion[Logging]

# region [Constants]

THIS_FILE_DIR = Path(__file__).parent.absolute()

# endregion[Constants]

# Wed, 18 Aug 2021 11:51:13 GMT


def parse_last_modifed(in_last_modified: str) -> datetime:
    month_conversion_table = {"jan": 1,
                              "feb": 2,
                              "mar": 3,
                              "apr": 4,
                              "may": 5,
                              "jun": 6,
                              "jul": 7,
                              "aug": 8,
                              "sep": 9,
                              "oct": 10,
                              "nov": 11,
                              "dec": 12,
                              "dez": 12}
    cleaned_last_modified = in_last_modified.split(",")[-1].removesuffix("GMT").strip()
    raw_day, raw_month, raw_year, raw_time = cleaned_last_modified.split()

    day = int(raw_day)
    month = month_conversion_table.get(raw_month.casefold())
    year = int(raw_year)
    hour, minute, second = (int(i.strip()) for i in raw_time.split(":"))
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second, tzinfo=timezone.utc)


def get_github_client() -> Github:
    token = os.getenv("_DOC_CREATION_GITHUB_TOKEN", None)
    if token is None:
        print("Warning no github token found")

    return Github(token)


GITHUB_URL = URL("https://github.com")

GITHUB_DONWLOAD_BASE_URL = URL("https://raw.githubusercontent.com")


class GitHubItem:

    def __init__(self,
                 name: str,
                 path: Path,
                 url: URL,
                 last_modified: datetime,
                 sha: str,
                 size: int = None) -> None:
        self.name = name
        self.path = path
        self.url = url
        self.last_modified = last_modified
        self.sha = sha
        self.size = size
        self._parent: "GithubFolder" = None

    @property
    def parent(self) -> Optional["GithubFolder"]:
        return self._parent

    @property
    def parent_folder_path(self) -> Optional[Path]:
        if self.name == "ROOT":
            return None
        return self.path.parent

    def __hash__(self) -> int:
        return hash(self.sha)

    def __repr__(self) -> str:
        """
        Basic Repr
        !REPLACE!
        """
        return f'{self.__class__.__name__}(name={self.name!r}, path={self.path.as_posix()!r}, last_modified={self.last_modified!r}, size={self.size!r}, parent={self.parent!r})'


class GithubFile(GitHubItem):

    def __init__(self,
                 name: str,
                 path: Path,
                 url: URL,
                 download_url: URL,
                 last_modified: datetime,
                 sha: str,
                 size: int = None) -> None:
        super().__init__(name=name,
                         path=path,
                         url=url,
                         last_modified=last_modified,
                         sha=sha,
                         size=size)
        self.download_url = download_url

    def get_content(self) -> str:
        with requests.get(self.download_url) as response:
            return response.text

    def download(self, target_folder: Path) -> Path:
        out_path = target_folder.joinpath(self.name)
        out_path.write_text(self.get_content(), encoding='utf-8', errors='ignore')

    def __repr__(self) -> str:
        """
        Basic Repr
        !REPLACE!
        """
        return f'{self.__class__.__name__}(name={self.name!r},path={self.path.as_posix()!r}, last_modified={self.last_modified!r}, size={self.size!r}, parent={self.parent!r})'


class GithubFolder(GitHubItem):

    def __init__(self,
                 name: str,
                 path: Path,
                 url: URL,
                 last_modified: datetime,
                 sha: str) -> None:
        super().__init__(name=name,
                         path=path,
                         url=url,
                         last_modified=last_modified,
                         sha=sha,
                         size=None)

        self.children: list[Union["GithubFile", "GithubFolder"]] = []

    def add_child(self, child: Union[GithubFile, "GithubFolder"]):
        child._parent = self
        self.children.append(child)

    def walk(self) -> Generator[Union[GithubFile, "GithubFolder"], None, None]:
        def _recursive_walk(folder: GithubFolder):
            yield folder
            for sub_item in folder.children:
                if isinstance(sub_item, GithubFile):
                    yield sub_item
                elif isinstance(sub_item, GithubFolder):
                    yield from _recursive_walk(sub_item)
        yield from _recursive_walk(self)


class GithubItemsHolder:

    def __init__(self, github_items: Iterable[Union[GithubFile, GithubFolder]]) -> None:
        self.github_items = tuple(github_items)
        self.folder_items = tuple(i for i in self.github_items if isinstance(i, GithubFolder))
        self.file_items = tuple(i for i in self.github_items if isinstance(i, GithubFile))
        self._item_path_map = {i.path: i for i in self.github_items}

    @property
    def root(self) -> GithubFolder:
        return next(i for i in self.folder_items if i.name.casefold() == "root")

    @property
    def read_me(self) -> GithubFile:
        return next(i for i in self.file_items if i.name.casefold() == "readme.md")

    @property
    def changelog(self) -> GithubFile:
        return next(i for i in self.file_items if i.name.casefold() == "changelog.txt")

    def __getitem__(self, path: Path) -> Union[GithubFile, GithubFolder]:
        return self._item_path_map[path]

    def __len__(self) -> int:
        return len(self.github_items)


class GithubRepo:

    def __init__(self, owner_name: str, repo_name: str, branch_name: str = None) -> None:
        self._owner_name = owner_name
        self._repo_name = repo_name
        self._branch_name = branch_name
        self._full_identifier = f"{self._owner_name}/{self._repo_name}"
        self._repo_url = GITHUB_URL / self._owner_name / self._repo_name

        self.github_client: Github = get_github_client()
        self._repo: Repository = self.github_client.get_repo(self._full_identifier)
        self._branch: Branch = None
        self._git_tree: GitTree = None
        self._file_items: GithubItemsHolder = None
        self.initialize_branch()

    def initialize_branch(self) -> None:
        self._branch = self._repo.get_branch(self.branch_name)
        self._git_tree = self._get_git_tree()
        self._file_items = self._get_file_items()

    def _get_file_items(self) -> tuple[Union[GithubFile, GithubFolder]]:

        root = GithubFolder(name="ROOT", path=Path("."), url=self.base_file_url, last_modified=parse_last_modifed(self.git_tree.last_modified), sha=self.git_tree.sha)
        collected_items = [root]
        for item in self.git_tree.tree:

            name = item.path.split("/")[-1]
            url = self.base_file_url / item.path
            last_modifed = parse_last_modifed(item.last_modified)
            sha = str(item.sha)
            size = item.size
            path = Path(item.path)
            if item.type == "tree":
                github_item = GithubFolder(name=name, path=path, url=url, last_modified=last_modifed, sha=sha)
            elif item.type == "blob":
                download_url = self.download_base_url / item.path
                github_item = GithubFile(name=name, path=path, download_url=download_url, url=url, last_modified=last_modifed, sha=sha, size=size)

            collected_items.append(github_item)

        folder_dict = {i.path: i for i in collected_items if isinstance(i, GithubFolder)}
        for collected_item in collected_items:

            parent_item = folder_dict.get(collected_item.parent_folder_path, None)
            if parent_item is not None:

                parent_item.add_child(collected_item)

        return GithubItemsHolder(github_items=collected_items)

    def _get_git_tree(self) -> GitTree:
        latest_sha = self.latest_commit.sha
        return self._repo.get_git_tree(latest_sha, True)

    @property
    def rate_limit_left(self) -> int:
        return self.github_client.rate_limiting[0]

    @property
    def branch_name(self) -> str:
        if self._branch_name is None:
            self._branch_name = self._repo.default_branch
        return self._branch_name

    @branch_name.setter
    def branch_name(self, name: Union[None, str]) -> None:
        self._branch_name = name
        self.initialize_branch()

    @property
    def base_file_url(self) -> URL:
        return self._repo_url / "blob" / self.branch_name

    @property
    def download_base_url(self) -> URL:
        return GITHUB_DONWLOAD_BASE_URL / self._owner_name / self._repo_name / self.branch_name

    @property
    def latest_commit(self) -> Commit:
        return self._branch.commit

    @property
    def branch(self) -> Branch:
        return self._branch

    @property
    def git_tree(self) -> GitTree:
        return self._git_tree

    def __repr__(self) -> str:
        """
        Basic Repr
        !REPLACE!
        """
        return f'{self.__class__.__name__}(owner_name={self._owner_name!r}, repo_name={self._repo_name!r}, branch_name={self.branch_name!r})'


# region[Main_Exec]
if __name__ == '__main__':
    x = GithubRepo("official-antistasi-community", "A3-Antistasi")

    x.initialize_branch()
    a = []
    for i in x._file_items.github_items:
        if i.name.endswith(".sqf"):
            a.append(i)

    with ThreadPoolExecutor(max_workers=10) as pool:
        for c in pool.map(lambda x: x.get_content(), a):
            print(c.splitlines()[:3])

    print(x.rate_limit_left)

# endregion[Main_Exec]
