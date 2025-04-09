# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
# C "  /Users/conner/Downloads/ICS 32/Assignment1-ICS32/   " -n "  my_diary  "
import shlex
from pathlib import Path
from notebook import Notebook
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

def check_file():
    pass

def is_json_file():
    pass


def create_notebook(notebook_path: str, notebook_name: str) -> str:
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
    print(directory)
    if not directory.exists() or not directory.is_dir():
        print("ERROR: Directory does not exist")
        return

    notebook_path = directory / f"{notebook_name}.json"
    if notebook_path.exists():
        print("ERROR: Path already exists")
        return

    username = input("Please enter your username:\n")
    password = input("Please enter your password:\n")
    bio = input("Please describe your bio:\n")

    notebook = Notebook(username, password, bio)
    notebook.save(notebook_path)
    print(f"{notebook_path} CREATED")


def delete_notebook(notebook_file: str) -> str:
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


def load_notebook(notebook_path):
    print(notebook_path) 
    path = Path(notebook_path)

    




def edit_notebook(command):
    pass


def print_notebook_info(command):
    pass
