# Restaurant Menu App - CRUD

* This is a Flask project that I have created with the help of Udacity course curriculum to learn and demonstrate CRUD functionality along with OAuth authentication and authorization

### Prerequisites

* Web Browser

* Network Connection/Internet

* Google+ Account

* Full Stack Vagrant VM, from the Terminal, run: git clone https://github.com/udacity/OAuth2.0 oauth

## Run the virtual machine

1. Open the your preferred Terminal program
1. Using the terminal, change directory to oauth (**cd oauth**)
1. Type **vagrant up** to launch your virtual machine.


## Starting the Vagrant VM

* Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine

* When you want to log out, type **exit** at the shell prompt.
To turn the virtual machine off (without deleting anything), type **vagrant halt**.

* If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.

### Checking shared VM Folder

* Change to the /vagrant directory by typing **cd /vagrant**.

This will take you to the shared folder between your virtual machine and host machine.

* Type **ls**

This is to ensure that you are inside the directory that contains project.py, database_setup.py, and two directories named 'templates' and 'static'

## Running the Restaurant Menu App

1. In the terminal type python database_setup.py, to create the sqlite database, locally
1. Type python lotsofmenus.py, to populate the created database
1. Type python app.py, please visit http://localhost:5000 on your preferred browser

## API Endpoints

While the app is successfully running respective JSON data can be viewed at the below endpoints

#### JSON APIs to view Restaurant Menu details

**/restaurant/<int:restaurant_id>/menu/json**

#### JSON APIs to view Menu item details

**/restaurant/<int:restaurant_id>/menu/<int:menu_id>/json**

## Acknowledgments

* My instructor at Udacity, Lorenzo Brown
* Thanks to PurpleBooth(https://gist.github.com/PurpleBooth) for her README template
