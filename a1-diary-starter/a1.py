    # Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

    # Replace the following placeholders with your information.

    # Connor Ng
    # ngce@uci.edu
    # ngce
    # Command C Test Input: 
    # C "/home/john/ics 32/my notebooks" -n my_diary

import command_parser
def main():
    while True:
        command_str = input("")
        print(command_str)
        if command_str == "Q":
            break
        if command_str.startswith("C "):
                command_parser.create_notebook(command_str)

if __name__=="__main__":
    main()


    
