pip install virtualenv -q
virtualenv venv/build
.\venv\build\Scripts\activate.ps1
pip install -r requirements.txt
coverage run -m unittest discover
coverage xml