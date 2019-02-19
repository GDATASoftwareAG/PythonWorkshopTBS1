# Modules need to be imported via the "import" statement.
# There are two different ways to import a module: import
# the whole module or import only specific items from a module.
# We'll start by importing a whole module, the "os" module.

import os

# This module can be used for operating system functions like
# listing directories or changing the working directory in a script.
# The functions called will work on any platform that the python
# library supports, so you can write OS independent code with this.

# Print the current working directory:

current_working_directory = os.getcwd()
print(current_working_directory)

# One directory up:
os.chdir('..')

# List all files in this dir:
files = os.listdir(os.getcwd())
for file in files:
    print(file)

os.chdir(current_working_directory)

# You can also execute commands, in this case calling the "HelloWorld" in this directory,
# by calling an os function named "system"
# Please notice that the called process will block the execution of the script until it terminates.

os.system("HelloWorld.exe")

# Now we'll import a specific function from the hashlib module:

from hashlib import md5

# By the way: it's considered bad practice to import functions and models somewhere else as at the top of files

hasher = md5()

# As you can call the imported class directly instead of using "hashlib.md5()".

hasher.update("What is the MD5 representation of this string?".encode('utf-8'))

print(hasher.hexdigest())

