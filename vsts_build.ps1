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