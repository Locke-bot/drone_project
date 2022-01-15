This is the solution to the coding assignment. 
The project is built in Django with Django Rest Framework. To run the project you only need Python 3 and the python package manage (pip) to be installed on your local machine. 
All project dependencies are available in the ***requirement.txt*** file.


## Build Instructions

From your command line tool run the steps below to build the project:
- **git clone https://oauth:glpat-uzgVi68z6ess8j6ymxzb@gitlab.com/musala-coding-tasks-solutions/oluwatobi-sholanke.git**
- cd oluwatobi-sholanke
- python3 -m venv env
- source env/bin/activate 
- pip install -r drones/requirements.txt

This will install all project dependencies required to run the project.

## Run Instructions

Execute the follow to run the project from project root:
- cd oluwatobi-sholanke
- source env/bin/activate 
- cd drones
- python manage.py runserver

The project will be served on http://localhost:8000

If you have another process running on port 8000, please speciafy port address when running as shown below
- python manage.py runserver localhost:8001

In the example above, I used port address 8001



## Test Instructions

From your command line tool run the steps below to test, from project root:
- cd oluwatobi-sholanke
- source env/bin/activate 
- cd drones
- python manage.py test

You should see the test result show like:

>Found 7 test(s).
>Creating test database for alias 'default'...
>System check identified no issues (0 silenced).
>.......
>Ran 7 tests in 0.027s
>OK
>Destroying test database for alias 'default'...
