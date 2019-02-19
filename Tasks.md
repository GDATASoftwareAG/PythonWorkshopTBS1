# Tasks
Here you can find some tasks to process for a better understanding of Python basics.
Therefore read the [Readme](Readme.md) please.

## 1. Variables
Assign some variables and play a bit with the operators `+`, `*`, `%`, `/` and `-`.

## 2. Loops and conditionals
### Conditionals
* create a script which takes a value by using `input("prompt")`
* check if the given value is `>`, `<` or `=` 3
    * input `2` should match the `< 3` condition
    * input `4` should match the `> 3` condition
    * input `3` should match the `= 3` condition
* check if the given value is even or odd
    * `20` should be even
    * `11` should be odd
* try to do an input with a string instead of a number, what will happen?

## Loops
* create a script which prints the numbers from `1` up to `22`
* create a script which prints only the even numbers between `1` and `22`
* create a script which prints elements of the following list:
```python
car_manufacturers = ['Audi', 'BMW', 'Opel', 'Mercedes', 'Hyundai', 'Kia', 'Toyota']
```
* create a script which prints the cars from the nested data structure below together with the related manufacturer
```python
cars = [
    ('Audi', ['A3', 'A8', 'Q7']),
    ('BMW', ['3er', '1er', 'X3']),
    ('Opel', ['Insignia', 'Astra', 'Corsa']),
    ('Mercedes', ['A-Klasse', 'CLA']),
    ('Hyundai', ['Tucson', 'i10', 'i20', 'i30', 'i40']),
    ('Kia', ['Seed', 'Sportage']),
    ('Toyota', ['Auris'])
]
```
* create a loop which asks the user for a password until he inserts `1234` (you can use `input("prompt")` for getting the user input)

## 3. Classes and objects
Create classes which match the following text:
* A vehicle should have a passenger-count, a speed limit in km/h and a wheel-count
* A car should extend the vehicle and have four wheels. The passenger-count should be configurable.
* A car should have additionally a crash-test-rating in stars, a manufacturer and a name
* An e-bike should extend a vehicle with a passenger-count of one, a speed-limit of 25 km/h and a wheel-count of two
* Additionally an e-bike should have a configurable maximum range with one full charged battery
* A garage should be able to contain multiple vehicles
* You should be able to add a vehicle to the garage and remove a vehicle from the garage
* A garage should be able to count all vehicles inside
* A garage should be able to return the information about which vehicles are inside the garage
* Create some different vehicles and a garage
* Add some vehicles to the garage and print the information
* Remove some vehicles from the garage and print the information

## 4. Modules
Use pip to install the following modules:
* pymysql
* pyodbc
* pygame

## 5. Main-Method
Create a function that takes two positive integers as input from console and divides the first variable by the second. 
Write a unit test for this function that includes tests for valid and invalid numbers.

Use the introduced main method implementation for creating the unit test. 

## 6. Python-Console
Use the Python console to achieve the following tasks:
* Enumerate the files in this directory
* Put a string into a variable and print it reversed
* Test the addition, subtraction, division and multiplication of some integer values 
* Create an object and print it so you can see the internal representation
* Advanced: calculate the MD5 hash for Readme.md in this directory

## 7. Frameworks

### 1. PyGame
Modify `pygame_example.py` so that you can handle these button presses:
* 1 on keyboard should turn the screen yellow
* 2 on keyboard should turn the screen green
* 3 on keyboard should turn the screen red
* 4 on keyboard should turn the screen white
* 5 on keyboard should turn the screen black
 

### 2. Flask (Web Endpoint)
Create a simply web-endpoint which takes one int-value in the URL-path and returns the given int-value multiplied by four.

E.g.:

Browse to `http://127.0.0.1:5000/multiply-by-four/2` should return `8`.

Hint:
* `int(x)` will cast the value of `x` to an integer
* `str(x)` will cast the value of `x` to a string

### 3. PyPlot
Extend `matplotlib_example.py` by plotting a second line that draws a straight line from values `-2` to `0` into
the same figure.

## 8. Databases
Extend `sqlite3_example.py` by adding your own user into the users table. Also modify Stefan Decker's access level so
that it's `3` afterwards and delete Manuel Beelen's user.
