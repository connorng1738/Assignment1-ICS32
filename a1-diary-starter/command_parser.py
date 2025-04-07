# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
import shlex
from pathlib import Path
from notebook import Notebook
import json

def create_notebook(command):
    
    info = shlex.split(command)
    print(info)

    path = info[1]
    print(f"Path{path}")
    notebook_name = info[3]
    print(f"Notebook_name{notebook_name}")
    print(notebook_name)
    
    directory = Path(path)
    if not directory.exists() or not directory.is_dir():
        print("ERROR")
        return

    notebook_path = directory / f"{notebook_name}.json"
    if notebook_path.exists():
        print("ERROR")
        return

    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")
    bio = input("Please describe your bio:\n")

    notebook = Notebook(username, password, bio)
    
    notebook_data = {
        'username': notebook.username,
        'password': notebook.password,
        'bio': notebook.bio,
    }

    with open(notebook_path, 'w') as f:
        json.dump(notebook_data, f, indent = 4)
        print("Created")

    
    print(username, password, bio)


def delete_notebook(command):
    pass

def load_notebook(command):
    pass

def edit_notebook(command):
    pass

def print_notebook_info(command):
    pass



