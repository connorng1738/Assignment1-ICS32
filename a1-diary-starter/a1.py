# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Connor Ng
# ngce@uci.edu
# ngce
# remember to ask about what -n does
# Command C Test Input: C "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/" -n "my_diary"

# Command D Test Input: D "/Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary3.jso"
# /Users/conner/Downloads/ICS 32/Assignment1-ICS32/my_diary3.json



import command_parser


def main():
    while True:
        command_str = input("")
        info = command_parser.parse_command(command_str)

        if command_str == "Q":
            break
        if command_str.startswith("C "):
            command_parser.create_notebook(info[1].strip(), info[3].strip())
        if command_str.startswith("D "):
            command_parser.delete_notebook(info[1].strip())


if __name__ == "__main__":
    main()
