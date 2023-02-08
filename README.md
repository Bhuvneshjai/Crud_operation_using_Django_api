# Prabhi-Vision Project
## This website using Django framework with the specified requirements.
### follow these steps:

1. Create a Django project using the command django-admin startproject <Image_Market_Project>.
2. Create an app within the project using the command python manage.py startapp <image_handler>.
3. Define the models for the "Image" and "Category" tables in the models.py file of your app.
4. Create the necessary database tables by running the command python manage.py makemigrations and python manage.py migrate.
5. Use the Django admin interface to upload the images and categorize them.
6. In the views.py file of your app, create a view to fetch all the images of a particular category and render them in an HTML template. 
7. In the urls.py file of your app, create a URL pattern to map the view.
8. In the /templates/home.html template, display the images using a loop.

##### Now, when you run the development server and visit the URL for a specific category, you should see all the images for that category displayed on the page.

## create a virtual environment with the dependencies listed in a requirements.txt file.
### use the following steps:

1. Install virtualenv by running the command pip install virtualenv.
2. Create a virtual environment by running the command virtualenv image_virtual_env, where "image_virtual_env" is the name you choose for your virtual environment.
3. Activate the virtual environment by running the command source envname\Scripts\activate (on Windows).
4. Install the dependencies listed in the requirements.txt file by running the command pip install -r requirements.txt.

##### Now, you have a virtual environment with the specified dependencies installed. To deactivate the virtual environment, you can run the command deactivate.

## Create a Django project and app.
### Follow Steps:

1. Register the models in the app's admin.py file.
<!-- from django.contrib import admin
from .models import Image, Category

admin.site.register(Image)
admin.site.register(Category) -->

2. Create a superuser account by running the command python manage.py createsuperuser.
3. Start the development server using the command python manage.py runserver.
4. Visit http://localhost:8000/admin/ in your web browser to access the Django admin panel.
5. username : bhuvneshjain2**@gmail.com
6. password : Bk****2***@