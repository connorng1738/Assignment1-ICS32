# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python


# Replace the following placeholders with your information.
# for any commnad, come up with some scenario where you can break your program
# a user is very confused about how to use your program, how would a confused user use your program
# edge cases - any broken commands, any type of path (abs vs relative)
# make sure all the outputs are exactly how they should be
# important to output for each command as instructed


# Command C Test Input: C "/Users/conner/Downloads/ICS 32/Assignment1-ICS32" -n "my_diary"
# Command C Test Input: C "/Assignment1-ICS32" -n my_diary2 #relative path
# Command D Test Input: D "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary.json"
# Command O Test Input: O "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary3.json"
# Command E Test Input: E -usr ur -pw pwd -no a -bio bio 
# Command E Test Input: E -del 2
# Command P Test Input: P -usr -pwd -not -bio


# Connor Ng
# ngce@uci.edu
# ngce


import command_parser




def main():
    current_notebook = None
    notebook_path = None


    while True:
        try:
            command_str = input("")

            if command_str == "Q":
                break

            info = command_parser.parse_command(command_str)

                
            if command_str.startswith("C "):
                    current_notebook, notebook_path = command_parser.create_notebook(info[1].strip(), info[3].strip())
            elif command_str.startswith("D "):
                    command_parser.delete_notebook(info[1].strip())

            elif command_str.startswith("O "):
                    current_notebook, notebook_path = command_parser.load_notebook(info[1].strip())

            elif command_str.startswith("E "):
                    if current_notebook:
                        command_parser.edit_notebook(current_notebook, notebook_path, info[1:])
                    else:
                        print("ERROR")

            elif command_str.startswith("P "):
                if current_notebook:
                    command_parser.print_notebook_info(current_notebook, info[1:])
                else:
                     print("ERROR")
            else:
                print("ERROR")
        except Exception:
            print("ERROR")
if __name__ == "__main__":
   main()
