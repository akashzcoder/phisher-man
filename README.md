# PhisherMan

![Screenshot](phishing.png)

# To run the overall server:
Step 1: `docker-compose build` <br>
Step 2: `docker-compose up -d`

# To bring the server down:
1. `docker-compose stop -v`

# To manually Run Application Backend
1. Install Python & pip
2. Navigate into the /backend/ folder

**Create a virtual python environment:**

3. `python3 -m venv env`
4. `source env/bin/activate` (On Windows use `env\Scripts\activate`)

**Install Django and the Django REST Framework into the virtual python environment:**

5. `pip install django`
6. `pip install djangorestframework`

**Start the Server:**

7. Navigate into /backend/phish_manager/ 
8. Run `python manage.py runserver`
9. Go to http://127.0.0.1:8000/incidents/ to view all incidents
