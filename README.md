# Bug-tracker
A responsive web application for tracking project bugs.


## Installation
I do assume that you're running linux based operating system. Before running the application, make sure you're machine is python, pip and virtualenv installed. To install, open your terminal then install the following requirements

* **Python**
```
$ sudo apt-get install python
```
* **pip(for managing project depencies)**
```
$ sudo apt-get install pip
```
* **virtualenv(allow you to avoid installing python packages grobally)**
```
$ pip install virtualenv
```


* **Cloning the project into your local machine**

Once you finish installing the above basic requirements, you will have to clone the application from the repository to anywhere on your machine. here is the command:
```
$ git clone https://github.com/peter88tom/Bug-tracker.git
```

The application will be cloned into ```Bug-tracker```


* **Preparing project environment**

Change directory to Bug-tracker
```
$ cd Bug-tracker
```

Now create a virtual environment by using the virtualenv we installed ealier
```
Bug-tracker$ virtualenv env
```
where *env* is a name of your choice.

Once that is done, we will have a folder *env* in our *Bug-tracker* project. Now it's time to activate the environment we have just created so that we can install our project dependencies
```
Bug-tracker$ source env/bin/activate
```

The environment has been activated, let install project dependencies which  is located on *requirements.txt*
```
(env)Bug-tracker$ pip install -r requirements.txt
```


* **Database configurations**

The dependecies will be installed, now let's do database configuration for our application.

While the environment is activate, create migrations, then migrate the database, we don't do any database settings on our *admin/setings.py* because we are using SQLite which is the default django database 
```
(env)Bug-tracker$ python manage.py makemigrations
(env)Bug-tracker$ python manage.py migrate
```

The above command will create migrations files and migrate our database scheme to SQLite.

Once the migrate is complete, we have to create super-user for our admin site.
```
(env)Bug-tracker$ python manage.py createsuperuser
```

Will be asked for username, enmail and password, fill in the questions

## Running the pp

Once done creating super-user, you can start the application with the following command
```
(env)Bug-tracker$ python manage.py runserver
```

The command will output the your application is running on port 8000, click the link and visit the page and start previewing the projects and their bugs deacriptions

## Running the tests

Explain how to run the automated test for the application
