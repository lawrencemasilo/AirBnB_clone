# AirBnB Clone Project
The first step to building our first full web application

![hbnb logo](https://github.com/Smambo/AirBnB_clone/assets/113464914/a2ea971d-d275-4901-ac7f-69a7939c3ffd)

## Description
The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.co.za/?locale=en&_set_bev_on_new_domain=1696855171_NzA3NWE0NjdlOTcw). It will not implement all the features, only some to cover the fundamental concepts of the higher level programming track

## Command Interpreter
* Useful for manipulating data without a visual interface, like in a Shell (perfect for development and debugging)
* In our case, we want to be able to manage the objects of our project:
  * Create a new object (eg: a new User or a new Place)
  * Retrieve an object from a file, database etc...
  * Do operations on objects (count, compute stats, etc...)
  * Update attributes of an object
  * Destroy an object
### How to start it:
1. Type `./console` in your terminal and press `Enter`.
2. Type `help` to see list of available commands.
### How to use it:
The shell in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The shell in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```

### Running Unittests

Make sure to run the tests from the root of the repository

In interactive mode:

`python3 -m unittest discover tests`

Non-interactive mode:

`echo "python3 -m unittest discover tests" | bash`

* To run tests for a specific file, use the absolute path:

  E.g. `python3 -m unittest tests/test_models/test_base_model.py`
