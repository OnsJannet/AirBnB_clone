# 0x00. AirBnB clone - The console:

This repository is about a Holbertonschool project about Creating a clone for the Airbnb website. It Helps understanding what is a command interpreter and how it works using Python. In this project we will be creating our own unittests. 

## The consol:
working with both interactive and non-interactive modes, HBnb console is our own version of the Unix shell.



## Environmental Specs:
* __Environment:__ Ubuntu 14.04 LTS
* __Languages:__ Python3
* __Style:__ PEP8

## Compilation & Output:
* for Unit Tests : python3 -m unittest discover tests


## Concept Covered:
* How to create a Python package
* How to create a command interpreter in Python
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What are args and kwargs and how to use them 
* How to handle named arguments in a function

## The Console:
* Commands: 
* (hbnb) quit - we use it to quit the console
* (hbnb) EOF - we use it to quit the console via EOF
* (hbnb) help <command> - we use it to display help
* (hbnb) create <class> - we use it to create and object and display it's id
* (hbnb) show <class> <id> - we use it to show objects and information related to it 
* (hbnb) destroy <class> <id> - we use it to delete an object
* (hbnb) all - we use it to display all instances
* (hbnb) update <class> <id> <attribute name> <attribute value> - we use it to Update the attribute of a class


First thing first we need to run ./console.py
we'll be welcomed with the following output:

* Interactive mode: 


(hbnb) help

```sh
Documented commands (type help <topic>):
========================================
EOF  create  destroy  help  quit  show
```

## The Console:

* (hbnb) create : 
```sh
(hbnb) create BaseModel
b49fce29-9f35-46e7-8b67-174fe11023e2
(hbnb) 
```

* (hbnb) show :

```sh
(hbnb) show BaseModel b49fce29-9f35-46e7-8b67-174fe11023e2
{'id': 'b49fce29-9f35-46e7-8b67-174fe11023e2', 'created_at': '2020-11-04T14:51:51.869897', 'updated_at': '2020-11-04T14:51:51.869933', '__class__': 'BaseModel'}
```

(hbnb) 

* (hbnb) all:

```sh
(hbnb) all
{'id': 'b49fce29-9f35-46e7-8b67-174fe11023e2', 'created_at': '2020-11-04T14:51:51.869897', 'updated_at': '2020-11-04T14:51:51.869933', '__class__': 'BaseModel'}
2020-11-04T14:51:51.869933', '__class__': 'BaseModel'}
```


## Used Files:
* base_model.py: Base Model is the main class or the class of all other classes (Parent Class)
* file_storage.py: a simple storage file that saves information
* user.py: file of the User Class 
* amenity.py: file of the Amenity Class 
* city.py: file of the City Class 
* state.py: file of the State Class 
* place.py: ile of the Place Class 
* review.py: file of the Review Class 

## Author:
* Ons Ben Jannet : https://github.com/OnsJannet
* Ayment Haddaji : https://github.com/Aymen-haddaji-hub