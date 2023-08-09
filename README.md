# WiredWorld
> This is a Django website project, assigned by SoftUni for an exam.

Here is a link to the deployed project using AWS. -> http://wiredworld.ddns.net


- ``📝``Note that the search bar isn't working because there is no SSL Certificate

---

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
   - if you want to deploy it add:
     - STATIC_ROOT=/app/static_files
     - MEDIA_ROOT=/app/media_files

Basic database needs for running the app:
 - add Group called 'Product management' that has full CRUD operations to the products
 - create at least one Category and one Subcategory for adding products
