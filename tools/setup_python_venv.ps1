$repoRootFolder = Split-Path $PSScriptRoot -Parent
$requirementsFile = Join-Path -Path $repoRootFolder -ChildPath "tools\python_requirements.txt"
$requirementsFileDev = Join-Path -Path $repoRootFolder -ChildPath "tools\python_dev_requirements.txt"
$venvDir = Join-Path -Path $repoRootFolder -ChildPath ".venv"
$venvExecutable = Join-Path -Path $venvDir -ChildPath "Scripts\python.exe"

Push-Location $repoRootFolder

Write-Host $(`
    "`n"+`
    "Upgrading system pip" +`
    "`n--------------------`n" )`
    -ForegroundColor Yellow

& "python" -m pip install --upgrade pip



Write-Host $(`
    "`n" +`
    "creating fresh venv in "        +`
    $venvDir.Trim() +`
    "`n-----------------------------------------------------------------------------`n"       )`
    -ForegroundColor Yellow


& "python" -m venv --clear --upgrade-deps $venvDir


Write-Host $(`
    "`n"+`
    "Installing Dependencies from " +`
    $requirementsFile.Trim() +`
    "`n-----------------------------------------------------------------------------------------------`n" )`
    -ForegroundColor Yellow

& $venvExecutable -m pip install -r $requirementsFile

Write-Host $(`
    "`n"+`
    "Installing DEV Dependencies from " +`
    $requirementsFileDev.Trim() +`
    "`n-----------------------------------------------------------------------------------------------`n" )`
    -ForegroundColor Yellow

& $venvExecutable -m pip install -r $requirementsFileDev



Write-Host $(`
    "`n"+`
    "`n-----------------------------------------------------" +`
    "`n=====================================================`n" +`
    "                     Finished" +`
    "`n=====================================================`n" +`
    "-----------------------------------------------------`n" )`
    -ForegroundColor Yellow
