# WiredWorld
> This is a Django website project, assigned by SoftUni for an exam.

To run it locally you will need:
 - Postgres database
 - install all packages using ```pip install -r requirements.txt```
 - migrate database using ```python manage.py migrate```
 - .env file that needs to have:
   - basic variables:
     - SECRET KEY
     - DEBUG (1 or 0)
     - ALLOWED_HOST
   - database variables:
     - DB_NAME
     - DB_USER
     - DB_PASSWORD
     - DB_HOST
     - DB_PORT
   - variables for GMAIL SMTP server:
     - EMAIL_HOST_USER
     - EMAIL_HOST_PASSWORD
