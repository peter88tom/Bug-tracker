# Bug-tracker
A responsive web application for tracking project bugs.


## Installation
The application was developed and tested on *linux based operating system* so before running the application, make sure you're machine is python, pip and virtualenv installed. To install, open your terminal then install the following requirements. By default linux comes with Python installed so you can skip and install *pip* and *virtualenv*.

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

Once that is done, we will have a folder *env* in our *Bug-tracker* project. Now let's  activate the environment so that we can install our project requirements
```
Bug-tracker$ source env/bin/activate
```

Install requirements which  is located on *requirements.txt*
```
(env)Bug-tracker$ pip install -r requirements.txt
```


* **Database Setup**

While the environment is activate, migrate the database schema, We don't do any database settings on our *admin/setings.py* because we are using SQLite which is the default django database 

```
(env)Bug-tracker$ python manage.py migrate
```

With that comming django will migrate our database scheme to SQLite.

In this stage we didn't run the *makemigrations* because the migrations files are include in the project located in *app/migrations*


* **Create super-user for creating projects in admin site of the application**
```
(env)Bug-tracker$ python manage.py createsuperuser
```

Will be asked for username, email and password, fill in accondingly.

* **Collecting Static Files**

Static files are css,javascript and image files that our project will be using. Django will compile them and improve loading when it want to use. Here is the command for collection static files

```
(env)Bug-tracker$ python manage.py collectstatic
```

## Running the pp

No you can start the application with the following command
```
(env)Bug-tracker$ python manage.py runserver
```

The command will output the your application is running on port 8000, click the link and visit the page and start creating bugs for listed projects. 

To create projects you have to login into the admin site of the application. here is the a way to access admin site go to *http://localhost:8000/admin*

To login type in the *username and password you created on createsuperuse command*.



## Built With

* [Python](https://docs.python.org/2/index.html) - Programming language used.

* [Django](https://docs.djangoproject.com/en/1.11/) - Python framework used.

* [Django Rest Framework](http://www.django-rest-framework.org/) - API used to populate data for easy bugs and projects listing and filtering.

* [Vue.js](https://vuejs.org/v2/guide/) - Used query data from DRF for easy project filtering and bug listing.

* [SQLite](https://www.sqlite.org/docs.html) - For storing projects and bugs.

* [Select2](https://select2.org/) - For searching projects when creating bugs.

* [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)- For making our application more responsive.
