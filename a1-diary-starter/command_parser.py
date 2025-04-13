# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
# C "  /Users/conner/Downloads/ICS 32/Assignment1-ICS32/   " -n "  my_diary  "pyc
import shlex
from pathlib import Path
from notebook import Notebook, Diary
import json


def parse_command(command: str) -> list:
    """
    Parses given input using shlex module

    Arguments:
      command: User input in the following format: [COMMAND] [INPUT] [[-]OPTION] [INPUT] #probably ask about this docstring as well

    Returns:
      parsed info in a list
    """

    info = shlex.split(command)
    return info


def create_notebook(notebook_path: str, notebook_name: str):
    """
    Creates a notebook given a name and a path.

    Arguments:
      notebook_path: The path to create the notebook
      notebook_name: The name of the notebook to be created in the `notebook_path`

    Returns:
     A string that represents operation status
    """

    print(f"Path: {notebook_path}")

    print(f"Notebook_name: {notebook_name}")

    directory = Path(notebook_path)
    notebook_path = directory / f"{notebook_name}.json"

    if not directory.exists() or not directory.is_dir():
        print("ERROR: Directory does not exist")
        return None

    if notebook_path.exists(): #why is this greyed out
        print("ERROR: Path already exists")
        return None #fix these return statements so they prompt user again later

    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")
    bio = input("Please describe your bio:\n")

    notebook = Notebook(username, password, bio)
    notebook.save(notebook_path)
    print(f"{notebook_path} CREATED")

    return notebook_path, notebook


def delete_notebook(notebook_file: str):
    """
    Deletes a notebook given user input

    Arguments:
    notebook_file: a user-specified file 


    Returns: 
    A string that represents operation status
    """
    path = Path(notebook_file)

    while not path.exists() or not path.is_file() or path.suffix != ".json":
        print("ERROR")
        path = Path(input('Please enter the proper file name: \n'))
    else:
        path.unlink()
        print(f'{path} DELETED')


def load_notebook(notebook_path: str):
    """
    Given user input, loads an existing notebook

    Arguments:
    notebook_path: absolute or relative path of a notebook

    Return:
    A string that represents operation status #Ask about how i can be more specific about what it returns? Should i mention specific errors?

    """
    path = Path(notebook_path)

    if path.exists() and path.suffix == ".json":
        with path.open("r") as f:
            # does this properly instantiate a notebook object and use the proper method to load the notebook info
            data = json.load(f)

        username = input("Please enter the notebook's username:\n")
        password = input("Please enter the notebook's password:\n")

        if username == data["username"] and password == data["password"]:
            notebook = Notebook(data["username"], data["password"], data["bio"])
            print("Notebook loaded.")
            return notebook, path
        else:
            print("ERROR: Wrong info")
    else:
        print("ERROR: Could not load notebook")
        
            
    '''for d in data["_diaries"]:
        notebook.add_diary(Diary(d["entry"], d["timestamp"]))
            print("Notebook loaded.")
            return notebook
        else:
            print("ERROR")
            return None
    else:
        # probably ask about how I should handle being given the wrong notebook_path
        print("ERROR")
        return None'''
    


def edit_notebook(notebook: Notebook, notebook_path: Path, command: list):
    print(command) #this should print a list of the commands and user info
    
    for i in range(0, len(command),2):
        if(command[i] == "-usr"):
            notebook.username = str(command[i + 1])
        elif(command[i] == "-pwd"):
            notebook.password = str(command[i + 1])
        elif(command[i] == "-bio"):
            notebook.bio = str(command[i + 1])
        elif(command[i] == "-add"):
            pass
        elif(command[i] == "-del"):
            pass
        else:
            print("ERROR")
    try:
        notebook.save(notebook_path)
        print("Notebook saved")
    except:
        print("Notebook did not save")
    
        
        
 
def print_notebook_info(command):
    pass
