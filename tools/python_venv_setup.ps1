
$requirementsFile = Join-Path -Path $PSScriptRoot -ChildPath "python_requirements.txt"


& "python" -m venv --clear --upgrade-deps ..\env
$parentPath = Split-Path -parent $PSScriptRoot
$envPython = Join-Path -Path $parentPath -ChildPath "env\Scripts\python"

& $envPython -m pip install --upgrade pip

& $envPython -m pip install -r $requirementsFile