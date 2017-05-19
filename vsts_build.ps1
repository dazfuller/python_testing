<#
.SYNOPSIS
    VSTS build script
.DESCRIPTION
    A custom script to create and activate the virtual environment, execute unit tests
    and produce coverage information
.EXAMPLE
    PS C:\> .\vsts_build.ps1 -OutputLocation .
    Executes the script and generates the coverage XML output in the current directory
.INPUTS
    OutputLocation - The location to write the coverage XML file
.OUTPUTS
    None
.NOTES
    Currently this re-directs the stderr output of the unittests and coverage commands, 
    this is because the TestTextRunning by default outputs to stderr which can cause
    a build failure in VSTS
#>
Param (
    [string] $OutputLocation
)

python -m venv .\venv\build
.\venv\build\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Output "> Executing unit tests"
& coverage run -m unittest discover 2>execute_stderr.txt

Write-Output "> Generating coverage report"
& coverage xml -o "$($OutputLocation)\coverage.xml" 2>coverage_stderr.txt