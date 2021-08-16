# a RESTful app using Python and FastAPI

## Requirements
- asgiref==3.4.1
- cffi==1.14.6
- cryptography==3.4.7
- Django==3.2.6
- django-filter==2.4.0
- django-location-field==2.1.0
- django-rest-knox==4.1.0
- djangorestframework==3.12.4
- Markdown==3.3.4
- Pillow==8.3.1
- psycopg2-binary==2.9.1
- pycparser==2.20
- pytz==2021.1
- six==1.16.0
- sqlparse==0.4.1

## Installation
After clonning the repository, we have to create a virtual environment, so we can have a clean python installation.
we do this by running the command
```
python -m venv env
```
we install all the required dependencies by running
```
pip install -r requirements.txt
```
## how to run

- firstly we have to runserver 
"python manage.py runserver "

- now use the API via postman or some browser

## Structure

- http://127.0.0.1:8000/APIlist
        API lists the details of items via GET request
- http://127.0.0.1:8000/APIregister/  
        Register API to create a new user along its token, just insert email,username and Password via POST request
- http://127.0.0.1:8000/APIlogin/
        Login API to authnticate user, it also managetoken, just provide username and password via POST request
- http://127.0.0.1:8000/APIlogout/
        Logout API, it logout the user, it requires authntication token for its work via POST request
- http://127.0.0.1:8000/APIinsert/
        API to insert the items data, just provide the data via POST request
- http://127.0.0.1:8000/APIdelete/
        API to delete an item, just provide the primary key via POST request
- http://127.0.0.1:8000/APIupdate/
        API to update an item, just provide the updated date along key via POST request
- http://127.0.0.1:8000/APIsearch/
        API for search in item, just provide the search word via POST request 

● its database follows Database NORMALIZATION foriegn and primary keys
● it also VERIFY and VALIDATE users on authentication.
● ss of Running API's in postman are placed in API-SS folder


