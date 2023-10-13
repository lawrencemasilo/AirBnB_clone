# AirBnB Clone Project
The first step to building our first full web application

![hbnb logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231013%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231013T102553Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d5c5cdec2c7fe48ba11b4a070dbcfa4370bed0c6c9d446fd8fadca04942e9f5a)
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

In interactive mode:

```
smambo@lenovo-ubuntu:~/AirBnB_clone$ python3 -m unittest discover tests
..
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

.....................................
----------------------------------------------------------------------
Ran 39 tests in 0.007s

OK
smambo@lenovo-ubuntu:~/AirBnB_clone$
```

Non-interactive mode:

```
smambo@lenovo-ubuntu:~/AirBnB_clone$ echo "python3 -m unittest discover tests" | bash
..
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

.....................................
----------------------------------------------------------------------
Ran 39 tests in 0.007s

OK
smambo@lenovo-ubuntu:~/AirBnB_clone$
```
