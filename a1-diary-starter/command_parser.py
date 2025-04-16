# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce

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
    A notebook object and the filepath of the notebook
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
    A notebook object and the filepath of the notebook

    """
    path = Path(notebook_path)

    if path.exists() and path.suffix == ".json":
        notebook = Notebook("","","")
        notebook.load(path)
        #with path.open("r") as f:
            # does this properly instantiate a notebook object and use the proper method to load the notebook info
            #data = json.load(f)

        username = input("Please enter the notebook's username:\n")
        password = input("Please enter the notebook's password:\n")

        if username == notebook.username and password == notebook.password:
            print("Notebook loaded.")
            return notebook, path
        else:
            print("ERROR: Wrong info")
    else:
        print("ERROR: Could not load notebook")

def edit_notebook(notebook: Notebook, notebook_path: Path, command: list):
    """"
    Edits a notebook given a command
    
    Arguments:
    notebook: instance of Notebook obkect
    notebook_path: file path of notebook
    command: list of commands given by user input

    Returns:
    A string that represents operation status
    """
    print(command) #this should print a list of the commands and user info

    for i in range(0, len(command),2):
        if(command[i] == "-usr"):
            notebook.username = str(command[i + 1])
        elif(command[i] == "-pwd"):
            notebook.password = str(command[i + 1])
        elif(command[i] == "-bio"):
            notebook.bio = str(command[i + 1])
        elif(command[i] == "-add"):
            new_diary = command[i + 1 ]
            notebook.add_diary(Diary(new_diary))
        elif(command[i] == "-del"):
            notebook.del_diary(int(command[i + 1]))
        else:
            print("ERROR")
    try: 
        notebook.save(notebook_path)
        print("Notebook saved")
    except:
        print("Notebook did not save")
       
    
def print_notebook_info(notebook: Notebook, command: list):
    diary = Diary()

    for i in range(0, len(command)):
        if(command[i] == "-usr"):
            print(f"Username: {notebook.username}")
        if(command[i] == "-pwd"):
            print(f"Password: {notebook.password}")
        if(command[i] == "-bio"):
            print(f"Bio: {notebook.bio}")
        if(command[i] == "-diaries"):
            print(notebook.get_diaries())
            for index, diary in enumerate(notebook.get_diaries()):
                print(index, diary["entry"])
        if(command[i] == "-diary"):
            pass
        if(command[i] == "-all"):
            pass

