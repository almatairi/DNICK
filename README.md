# DNICK

# KuCakes - Online Cake Store and Design Platform
KuCakes is an online platform that allows users to browse and purchase a variety of delicious cakes and even customize their own cake designs.

# Table of Contents
Getting Started
Prerequisites
Installation
Configuration
Usage
Development
Deployment

# Getting Started
KuCakes makes it easy to set up and start selling and designing cakes online.

# Prerequisites
To run KuCakes locally, you need to have the following software installed:

Python 3.x: Download Python
Django: Install using pip with pip install django
Virtual environment (recommended): Install using pip install virtualenv
Installation
Clone this repository: git clone https://github.com/almatairi/DNICK-prj.git
Navigate to the project directory: cd KuCakes
Create a virtual environment: python3 -m venv venv
Activate the virtual environment:
On macOS and Linux: source venv/bin/activate
On Windows: venv\Scripts\activate
Install project dependencies: pip install -r requirements.txt
Apply database migrations: python manage.py migrate

# Configuration
Before running the project, you'll need to create a superuser account for admin access:

Create a superuser: python manage.py createsuperuser
Follow the prompts to set a username, email, and password for the admin account.

# Usage
Start the development server: python manage.py runserver
Access the admin panel by visiting http://127.0.0.1:8000/admin/ and logging in with your superuser credentials.
Users can browse available cake designs, customize cakes with various options, and add them to their cart.
Users can proceed to the checkout page to finalize their orders.

# Development
Contributions to KuCakes are welcome! To contribute:

Fork the repository and create a new branch for your feature or bug fix.
Make your changes and submit a pull request.
Follow the project's coding standards and guidelines.
Deployment
To deploy KuCakes to a production environment, follow these steps:

Set up a production-ready database (e.g., PostgreSQL).
Configure environment variables for sensitive settings.
Use a web server (e.g., Nginx) and a production WSGI server (e.g., Gunicorn).
Set up HTTPS for secure connections.
Deploy the static files using collectstatic.
