# Python Workshop

This workshop should guide you through the basic things of Python3.

## Order
1. Variables
2. Loops and conditionals
3. Classes and Objects
    1. Inheritance
    2. Access-Rights
4. Python-Console
5. Main-Method
6. Modules
7. Frameworks
    1. PyGame
    2. Flask (Web Endpoint)
    3. PyPlot
8. Databases

## Requirements
To follow all parts of this workshop you'll need the following things:
* Python3
* Pip3
* Flask (installed with pip3)

## 1. Variables
Take a look into `variables.py` and make yourself familiar with the variable assignment.

You can run the `variables.py` by executing `python3 variables.py` inside a bash.

The console output should look like this:
```
12345
3.1415
hello
hello
[0, 1, 2]
(0, 1, 2)
<_io.TextIOWrapper name='variables.py' mode='r' encoding='UTF-8'>
1
1
1
2
1
1
```

Take a look into `global_variables.py` and make yourself familiar with the variable scopes of Python.

Console output:
```
2
2
4
inner_function: 4
outer_function: 4
```

## 2. Loops and conditionals
### Conditionals
Take a look into `conditionals.py` and make yourself familiar with the conditionals in Python.

Executing the script should show this console output:
```
Number = 2.
Number = 2.
Boolean is True.
Only the first boolean is True.
One of the booleans is True.
Start evaluation. True or False.
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Start evaluation. False or True.
Execution of function_to_show_print_with_returned_boolean(boolean).
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Start evaluation. False or False.
Execution of function_to_show_print_with_returned_boolean(boolean).
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Start evaluation. True and False.
Execution of function_to_show_print_with_returned_boolean(boolean).
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Start evaluation. False and True.
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Start evaluation. False and False.
Execution of function_to_show_print_with_returned_boolean(boolean).
Finished evaluation
Greetings.
No world found.
This is the same statement as "if simple_object != None:"
Should be the same
Not the same object even when values in object are the same
Values from objects are the same
```
You can play a bit with the value of `number` to get into the `elif` and into the `else` condition if you want to.

## Loops
Take a look into `loops.py` and make yourself familiar with the loops in Python.

Run the `loops.py` and compare the output with your understanding of the code.
```
Value of i is 0
Value of i is 1
Value of i is 2
Value of i is 3
Value of i is 4
	 hello
	 my
	 name
	 is
	 John
Hello Peter
Hello Maria
Hello John
Number value 0
Number value 1
Number value 2
Number value 3
Number value 4
Number value 5
Number value 6
Number value 7
Number value 8
Number value 9
colors : red
colors : blue
colors : orange
colors : yellow
animals : cow
animals : tiger
animals : fish
animals : dog
username : admin
password : 1234
url : localhost:8080
username : admin
password : 1234
url : localhost:8080
[2, 4]
[1, 3]
['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc']
```

## 3. Classes and objects
Take a look into `classes.py` and make yourself familiar with classes in Python.

Take a special look into the inheritance of those classes.

Every Person has a name and a surname.

A Trainer is a Person with an extra attribute `amount_trainees` which should show the amount of trainees a trainer has.

A Training has a location where the training will take place at, a trainer who will lead the training and some participants.

A TrainingForTrainers is a Training at the location 'TBH1' with a specific topic.

The `get_information`-method will return the information of a TrainingForTrainers.

Console output of execution:
```
Topic: "Python Crashkurs"
Where: TBH1
Trainer: Peter Schmidt
Amount of participants: 3
Amount of effected trainees: 12
```

## 4. Modules
Take a look into `modules.py` and make yourself familiar with the way modules are being used in Python.

Modules can be installed by using a command line tool named `pip` which will download modules from the official
Python module repository hosted on "pypi.org".

## 5. Main-Method
Python has, to our knowledge, a unique way of using the main method in a file. When a module is being imported the 
`__name__` identifier is being set to the name of the module being imported. For example if you would include the 
`classes` module being introduced in Chapter 3 via an `import` statement the `__name__` identifier would be set to
`"classes"` (the literal string `classes`). 

However, if you call a module directly by executing it's python script file the `__name__` identifier will be set to 
`"__main__"` (again, the literal string `__main__`). 

In most Python modules you will find the line `if __name__ == "__main__":` to distinguish between functionality
and execution. Most python developers like this because it allows re-use of code for different purposes and enables
modules to contribute something useful when being imported.

One of the major use cases for this semantic is unit tests when we deal with utility modules.  

Familiarize yourself with `main.py` to see an example of this approach.  

## 6. Python-Console
The Python console is launching a full python interpreter and executes each line being entered directly.

This can be used by the advanced Python magician(c) to solve easy tasks like enumerating files in a directory or 
calculating hashes by the use of Pythons plenty utility modules. 

The console can also be used to quickly verify that some method you are thinking about is working as expected.
This comes in handy when e.g. manipulating strings in real life applications. 

## 7. Frameworks

### 1. PyGame (GUI Framework)
Take a look into the `pygame_example.py`. You'll see a minimal example for a GUI application using PyGame.

PyGame is using an event based model, as you can see in lines 16-26 in `pygame_example.py`. Pay close attention to how
events are being handled.

PyGame has already implemented a lot of form and style attributes you would need in GUI applications, like buttons and 
text boxes. Read [this german example](https://www.spieleprogrammierer.de/wiki/Pygame-Tutorial) which provides a good 
overview on what's possible with the Framework.

Despite the name PyGame can be used to easily create any GUI application, not just games (although that is the focus of 
the core module developers).

### 2. Flask (Web Endpoint)
Take a look at `flask_example.py`. You'll see a minimal example for a web-endpoint using Flask.

In `start_flask_app.sh` you can see how to start the web-application.
```
$ ./start_flask_app.sh 
 * Serving Flask app "flask_example.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
When visiting `http://127.0.0.1:5000/` with a browser you'll see the `Hello, World!`-string.

### 3. MatPlotLib
Take a look at `matplotlib_example.py`. You'll see some basic graphs that can be drawn using matplotlib's `pyplot`
package as well as some basic numpy examples. 

## 8. Databases
In general, Python supports a lot of databases by using different modules. `sqlite3_example.py` shows you a small 
example of sqlite3 using the popular on-disk database framework.

You can also have a look at `mysql_example.py` and `odbc_example.py`, although both of those can not be demonstrated in
this workshop since we don't have local copies of MySQL and MS-SQL databases. However, both files will give you a 
good idea how the modules used work.

# Not enough?
You can easily do some online tutorials by yourself.
[Here](https://medium.com/quick-code/top-tutorials-to-learn-python-programming-200a4283995f) is a page where you can find some nice tutorials which might help you.

If you want to build cool webapps using the Flask micro framework see [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for a complete tutorial.
