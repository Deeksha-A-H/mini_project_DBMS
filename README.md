# mini_project_DBMS
 I developed restaurant management system, which is desktop application provides service facility to restaurant.

Installation Process
Install Python 
(URL: https://www.python.org/downloads/)	

Install Visual Studio Code  (VS Code)
(URL: https://code.visualstudio.com/)

Install Django:
1.	Open a command prompt
2.	Type: pip install django

Then follow these steps
1.	Install the Python extension.- Open VS Code IDE and click extensions there automatically u will be shown Python extension (Make sure you are connected to Internet)
2.	On your file system, create a project folder for this tutorial, such as your USN (Eg; DBMS).

3.	In that folder, use the following command (as appropriate to your computer) to create a virtual environment named env based on your current interpreter:
# Windows
python -m venv env
4.	Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.
5.	In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:
 
6.	The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./env or .\env:
 


7.	Create a New Terminal : In Menu Terminal -> New Terminal option



Creating project:
1.	Create a django project -  

     django-admin startproject first .
     (dot following project name is important which refers to current directory)

This startproject command assumes (by use of . at the end) that the current folder is your project folder, and creates the following within it:
●	manage.py: The Django command-line administrative utility for the project. You run administrative commands for the project using python manage.py <command> [options].
●	A subfolder named first, which contains the following files:
o	__init__.py: an empty file that tells Python that this folder is a Python package.
o	wsgi.py: an entry point for WSGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.
o	settings.py: contains settings for Django project, which you modify in the course of developing a web app.
o	urls.py: contains a table of contents for the Django project, which you also modify in the course of development.
2.	To verify the Django project, make sure your virtual environment is activated, then start Django's development server using the command “python manage.py runserver”. The server runs on the default port 8000.
3.	When you run the server the first time, it creates a default SQLite database in the file db.sqlite3, which is intended for development purposes but can be used in production for low-volume web apps. Also, Django's built-in web server is intended only for local development purposes. When you deploy to a web host, however, Django uses the host's web server instead. The wsgi.py module in the Django project takes care of hooking into the production servers.
If you want to use a different port than the default 8000, specify the port number on the command line, such as python manage.py runserver 5000. 
When you're done, close the browser window and stop the server in VS Code using Ctrl+C as indicated in the terminal output window.

4. In the VS Code Terminal with your virtual environment activated, run the   administrative utility's startapp command in your project folder (where manage.py resides):
                 python manage.py startapp hello
5.  The command creates a folder called hello that contains a number of code files and one subfolder. Of these, you frequently work with views.py (that contains the functions that define pages in your web app) and models.py (that contains classes defining your data objects). The migrations folder is used by Django's administrative utility to manage database versions. There are also the files apps.py (app configuration), admin.py (for creating an administrative interface), and tests.py (for unit tests). 

And then copy each file into your file don’t copy full file compare and then copy needed things or it will give error.

Installing and Creating Backend 

(i)	XAMPP that contains mysql
URL: https://www.apachefriends.org/download.html
(ii)	Python-mysql driver called mysql client. Don’t use pip. Better to download wheel file and install the same:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient (in that cp3-win32)
when u download u should get a wheel file
then goto the command prompt in the folder where this file is located and type
pip install wheelfilename

We’ll assume you’ve set up a database server, activated it and created a database within it. Database configuration lives in the Django settings file, called settings.py by default. Edit that file and look for the database settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBMS',
        'HOST':'localhost',
        'USER':'root', (xamp user)
        'PASSWORD':'aaa', (xamp password)
        'PORT':3306,
    }
}

Accessing Admin page

Django created and configured the default admin site for you. All that you need to do now is create an admin user (superuser) to log into the admin site. To create an admin user, run the following command from inside your virtual environment:
python manage.py createsuperuser
Enter your desired username and press enter.
Username: admin
You will then be prompted for your email address:
Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
Password: **********
Password (again): *********
Superuser created successfully.
Now that you have created an admin user, you’re ready to start using the Django admin. Let’s start the development server and explore.
First, make sure the development server is running, then open a web browser to http://127.0.0.1:8000/admin/.


For project execution just type “python manage.py runserver” in the command prompt.


