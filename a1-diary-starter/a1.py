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
                if len(info) == 4:
                    current_notebook, notebook_path = command_parser.create_notebook(
                        info[1].strip(), info[2].strip(), info[3].strip())
                else:
                    print("ERROR")
            elif command_str.startswith("D "):
                if len(info) == 2:
                    command_parser.delete_notebook(info[1].strip())
                else:
                    print("ERROR")
            elif command_str.startswith("O "):
                if len(info) == 2:
                    current_notebook, notebook_path = command_parser.load_notebook(
                        info[1].strip())
                else:
                    print("ERROR")
            elif command_str.startswith("E "):
                if current_notebook:
                    command_parser.edit_notebook(
                        current_notebook, notebook_path, info[1:])
                else:
                    print("ERROR")
            elif command_str.startswith("P "):
                if current_notebook:
                    command_parser.print_notebook_info(
                        current_notebook, info[1:])
                else:
                    print("ERROR")
            else:
                print("ERROR")
        except Exception as e:
            print("ERROR")


if __name__ == "__main__":
    main()
