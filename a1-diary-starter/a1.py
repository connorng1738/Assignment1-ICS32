    # Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

    # Replace the following placeholders with your information.

    # Connor Ng
    # ngce@uci.edu
    # ngce
    # Command C Test Input: 
    # C "  /Users/conner/Downloads/ICS 32/Assignment1-ICS32/   " -n "  my_diary  "

import command_parser
def main():
    while True:
        command_str = input("")
        info = command_parser.parse_command(command_str)

        if command_str == "Q":
            break
        if command_str.startswith("C "):
                
                command_parser.create_notebook(info[1].strip(), info[3].strip())

if __name__=="__main__":
    main()


    
