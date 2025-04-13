# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
# Command C Test Input: C "/Users/conner/Downloads/ICS 32/Assignment1-ICS32" -n "my_diary"
# Command C Test Input: C "/Assignment1-ICS32/a1-diary-starter" -n my_diary2
# Command D Test Input: D "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary5.json"
# Command O Test Input: O "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary1.json"


import command_parser


def main():
    current_notebook = None
    notebook_path = None

    while True:
        command_str = input("")
        info = command_parser.parse_command(command_str)

        #notebook_loaded = False
        #print(f"Notebook Loaded Status: {notebook_loaded}")

        if command_str == "Q":
            break

        elif command_str.startswith("C "):
            current_notebook, notebook_path = command_parser.create_notebook(info[1].strip(), info[3].strip())
            
        elif command_str.startswith("D "):
            command_parser.delete_notebook(info[1].strip())

        elif command_str.startswith("O "):
            current_notebook, notebook_path = command_parser.load_notebook(info[1].strip())
            
        elif command_str.startswith("E "):
            if current_notebook:
                command_parser.edit_notebook(current_notebook, notebook_path, info[1:])
            else:
                print("ERROR: No notebook loaded")
        else:
            print("ERROR: Invalid command.")


if __name__ == "__main__":
    main()
