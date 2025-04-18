# Connor Ng
# ngce@uci.edu
# ngce


import shlex
from pathlib import Path
from notebook import Notebook, Diary


def parse_command(command: str) -> list:
    """
    Parses given input using shlex module


    Arguments:
      command: User input including command and path


    Returns:
      List: Parsed info into list
    """

    info = shlex.split(command)
    return info


def create_notebook(notebook_path: str, 
                    flag: str, 
                    notebook_name: str) -> tuple:
    """
    Creates a notebook given a name and a path.


    Arguments:
      notebook_path: The path to create the notebook
      notebook_name: The name of the notebook to be created in the `notebook_path`

    Returns:
      Tuple: A notebook object and the filepath of the notebook
    """

    directory = Path(notebook_path)
    notebook_path = directory / f"{notebook_name}.json"

    if flag != "-n":
        print("ERROR")
        return (None, None)
    if notebook_name.strip() == "":
        print("ERROR")
        return (None, None)
    if not directory.exists() or not directory.is_dir():
        print("ERROR")
        return (None, None)
    if notebook_path.exists():
        print("ERROR")
        return (None, None)

    username = input("")
    password = input("")
    bio = input("")

    notebook = Notebook(username, password, bio)
    notebook.save(notebook_path)
    print(f"{notebook_path} CREATED")
    return notebook, Path(notebook_path)


def delete_notebook(notebook_file: str) -> None:
    """
    Deletes a notebook given user input

    Arguments:
      notebook_file: a user-specified file
    
    Returns:
      NONE
    """
    path = Path(notebook_file)

    while not path.exists() or not path.is_file() or path.suffix != ".json":
        print("ERROR")
        # change this to be empty
        path = Path(input(''))
    else:
        path.unlink()
        print(f'{path} DELETED')


def load_notebook(notebook_path: str) -> tuple:
    """
    Given user input, loads an existing notebook

    Arguments:
      notebook_path: absolute or relative path of a notebook

    Return:
      Tuple: A notebook object and the filepath of the notebook
    """
    path = Path(notebook_path)

    if path.exists() and path.suffix == ".json":
        username = input("")
        password = input("")
        notebook = Notebook("", "", "")
        notebook.load(path)

        if username == notebook.username and password == notebook.password:
            print("Notebook loaded.")
            print(notebook.username)
            print(notebook.bio)
            return notebook, path


def edit_notebook(notebook: Notebook, 
                  notebook_path: Path, 
                  command: list) -> None:
    """"
    Edits a notebook given a command

    Arguments:
      notebook: Notebook object
      notebook_path: file path of notebook
      command: list of commands given by user input

    Returns:
      NONE

    """

    for i in range(0, len(command), 2):
        if (command[i] == "-usr"):
            notebook.username = str(command[i + 1])
        elif (command[i] == "-pwd"):
            notebook.password = str(command[i + 1])
        elif (command[i] == "-bio"):
            notebook.bio = str(command[i + 1])
        elif (command[i] == "-add"):
            new_diary = command[i + 1]
            notebook.add_diary(Diary(new_diary))
        elif (command[i] == "-del"):
            if int(command[i + 1]):
                notebook.del_diary(int(command[i + 1]))
        else:
            print("ERROR")
            notebook.save(notebook_path)
            break
        notebook.save(notebook_path)


def print_notebook_info(notebook: Notebook, 
                        command: list) -> None:
    """"
    Prints notebook info

    Arguments:
      notebook: Notebook obkect
      command: list of commands given by user input
    
    Returns:
      NONE
    """
    diary = Diary()

    for i in range(0, len(command)):
        if (command[i] == "-usr"):
            print(f"{notebook.username}")
        elif (command[i] == "-pwd"):
            print(f"{notebook.password}")
        elif (command[i] == "-bio"):
            print(f"{notebook.bio}")
        elif (command[i] == "-diaries"):
            for index, diary in enumerate(notebook.get_diaries()):
                print(f"{index}: {diary['entry']}")
        elif (command[i] == "-diary"):
            index = int(command[i + 1])
            print(f"{index}: {notebook.get_diaries()[index]['entry']}")
        elif (command[i] == "-all"):
            print(notebook.username)
            print(notebook.password)
            print(notebook.bio)
            for index, diary in enumerate(notebook.get_diaries()):
                print(diary['entry'])
        elif (int(command[i].isdigit())):
            continue
        else:
            print("ERROR")
            break
