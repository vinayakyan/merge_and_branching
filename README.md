1. To Run this application first you will have to create a virutal environment
virtualenv venv

2. Activate the virtual environment by the command
venv\scripts\activate - for windows
source venv/Scripts/activate - for linux or in git bash

3. Change directory to demo_project using the command
cd demo_project

4. Install the dependancies by the command pip
pip install -r requirements.txt

5. Perform the makemigrations and migrate
py manage.py makemigrations
py manage.py migrate

6. Run the server to test the app
py manage.py runserver