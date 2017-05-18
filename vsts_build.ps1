python -m venv .\venv\build
.\venv\build\Scripts\Activate.ps1
pip install -r requirements.txt
coverage run -m unittest discover
coverage xml