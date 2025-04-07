# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
import shlex

def create_notebook(command):
    
    info = shlex.split(command)
    print(info)

    username = input("")
    password = input("")
    bio = input("")

    

    print(username, password, bio)


