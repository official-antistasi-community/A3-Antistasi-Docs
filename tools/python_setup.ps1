$error.clear()

try{
# try to get the pyhton version

$cmdOutput = & "python" --version


# check if it starts with the correct version, as we dont care about the patch part of the version
$python10Installed = $cmdOutput.StartsWith("Python 3.10")

}
# any way to prevent the error being printed out?
catch{"Error occured"}

if ($error){
    # error means python is not installed at all and therefore this gets set to false
    $python10Installed = $false
}

if (-Not $python10Installed){
    # create a full path to download the installer
    $installerFile = Join-Path -Path $PSScriptRoot -ChildPath "python-3.10.4-amd64.exe"


    Invoke-WebRequest "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe" -OutFile $installerFile
    # install python in a way the script waits for it to finish
    $proc = Start-Process -Wait -FilePath $installerFile -ArgumentList "/passive", "InstallAllUsers=1", "PrependPath=1", "CompileAll=1", "Include_test=1", "Include_symbols=1", "Include_debug=1", "Include_dev=1", "Include_pip=1"




}
# these depent on the env variables being set by the python installer (pythons script folder) to be available,
# unable to nicely test it on my system
# update pip,
& "pip" install --upgrade pip

# install pipx
& "pip" install --user pipx

# ensure pipx is on the path
& "pipx" ensurepath

# install sphinx into a venv of pipx
& "pipx" install sphinx==4.5.0

# inject the sub-dependencies for sphinx
& "pipx" inject sphinx sphinx-bootstrap-theme==0.8.1
& "pipx" inject sphinx sphinxcontrib-images==0.9.4
& "pipx" inject sphinx sphinxcontrib-mermaid==0.7.1
& "pipx" inject sphinx myst-parser==0.17.2