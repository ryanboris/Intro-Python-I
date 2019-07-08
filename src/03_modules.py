"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line
# YOUR CODE HERE
for i in sys.argv:
    print(i)

# Print out the OS platform you're using:
# YOUR CODE HERE
platform = sys.platform
print(platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
py_version = sys.version
print(py_version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
process_id = os.getpid()
print(process_id)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print(cwd)

# Print out your machine's login name
# YOUR CODE HERE
machine_login_name = os.getlogin()
print(machine_login_name)
