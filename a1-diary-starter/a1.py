    # Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

    # Replace the following placeholders with your information.

    # Connor Ng
    # ngce@uci.edu
    # ngce
import command_parser

if __name__=="__main__":
    
    command_str= input('Input your command string here:\n').strip()
    if command_str.startswith("C "):
        command_parser.create_notebook(command_str)
    
