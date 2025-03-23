import sys
import os
import subprocess
import shutil
import readline

prev_dir = None

# List of built-in commands in Oshell
BUILTIN_COMMANDS = [
    "exit", "speak", "type", "clear", "ls", "makedir", "removedir", 
    "changedir", "curdir", "createfile", "delfile", "writefile", 
    "appendfile", "copyfile"
]

def main():
    global prev_dir
    while True:
        current_dir = os.getcwd()
        sys.stdout.write(f"Current Working Directory is : {current_dir}\n")

        sys.stdout.write("# ")
        sys.stdout.flush()
        command = input()

        if command.strip():
            readline.add_history(command)

        c = command.split()

        if not c:
            continue

        if c[0] == 'exit':
            if len(c) > 1 and c[1].isdigit():
                sys.exit(int(c[1]))
            else:
                sys.exit()

        if c[0] == 'speak':
            sys.stdout.write(' '.join(c[1:]) + '\n')
            continue

        if c[0] == 'type' and len(c) > 1:
            for cmd in c[1:]:
                if cmd in BUILTIN_COMMANDS:
                    print(f"{cmd} is a shell built-in command")
                else:
                    found = False
                    paths = os.getenv("PATH").split(os.pathsep)  

                    for path in paths:
                        if os.path.isdir(path):
                            for ext in ([""] if os.name != "nt" else os.getenv("PATHEXT").split(";")):
                                full_path = os.path.join(path, cmd + ext)
                                if os.path.exists(full_path):
                                    print(f"{cmd} is an executable command at {full_path}")
                                    found = True
                                    break
                        if found:
                            break
                    
                    if not found:
                        print(f"{cmd}: not found")
            continue

        if c[0] == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        # Directory Manipulation
        if c[0] == 'ls':
            try:
                if os.name == 'nt':  
                    for item in os.listdir():
                        print(item)  
                else:  
                    os.system('ls')
            except Exception as e:
                print(f"Error: {e}")
            continue

        if c[0] == 'makedir':
            if len(c) > 1:
                try:
                    os.mkdir(c[1])
                    print(f"Directory: {c[1]} created successfully")
                except FileExistsError:
                    print(f"Error: The directory '{c[1]}' already exists.")
                except PermissionError:
                    print(f"Error: Permission denied to create '{c[1]}'.")
                except Exception as e:
                    print(f"Error: {e}")
            continue

        if c[0] == 'removedir':
            if len(c) > 1:
                try:
                    shutil.rmtree(c[1]) 
                    print(f"Directory: {c[1]} removed successfully")
                except FileNotFoundError:
                    print(f"Error: The directory '{c[1]}' does not exist.")
                except PermissionError:
                    print(f"Error: Permission denied to remove '{c[1]}'.")
                except Exception as e:
                    print(f"Error: {e}")
            continue

        if c[0] == 'changedir':
            prev_dir = os.getcwd()
            if len(c) > 1:
                try:
                    os.chdir(c[1])
                    print(f"Directory changed to: {os.getcwd()}")  
                except FileNotFoundError:
                    print(f"Error: The directory '{c[1]}' does not exist.")
                except PermissionError:
                    print(f"Error: Permission denied to change to '{c[1]}'.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Error: No directory specified.")
            continue

        if c[0] == 'curdir':
            try:
                print(os.getcwd())
            except Exception as e:
                print(e)
            continue

        if c[0] == 'changedir' and c[1] == '-' or c[0] == 'changedir' and c[1] == "..":
            if prev_dir:
                os.chdir(prev_dir)
                print(f"Directory successfully changed to {prev_dir}")
            else:
                print("No previous directory to return to")
            continue

        # File Handling
        if c[0] == 'createfile':
            try:
                with open(c[1], "w") as f:
                    f.write(" ")
                print(f"{c[1]}: file created successfully")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")
            continue

        if c[0] == 'delfile':
            try:
                os.remove(c[1])
                print(f"{c[1]}: file deleted successfully")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")
            continue

        if c[0] == "writefile":
            try:
                with open(c[1], "w") as f:
                    writer = input("Enter the Content you want to write: ")
                    f.write(writer)
                print(f"File {c[1]}: data written successfully")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(e)
            continue

        if c[0] == "appendfile":
            try:
                with open(c[1], "a") as f:
                    writer = input("Enter the Content you want to append: ")
                    f.write(writer)
                print(f"File {c[1]}: data appended successfully")
            except FileNotFoundError as e:
                print(str(e))
            except Exception as e:
                print(e)
            continue

        if c[0] == 'copyfile':
            print("------------------------------Executing Copyfile Command------------------------------")
            try:
                if not os.path.exists(c[1]):
                    print(f"Error: {c[1]} not found in the current directory")
                else:
                    with open(c[1], "r") as src_file:
                        reader = src_file.read()

                    with open(c[2], "w") as dest_file:
                        dest_file.write(reader)

                    print("Data copied successfully")

            except FileNotFoundError:
                print(f"Error: {c[1]} not found")
            except Exception as e:
                print(f"Error: {e}")
            continue

        # Running external executable commands
        found = False
        for path in os.getenv("PATH").split(os.pathsep):
            if os.path.isdir(path):
                for f in os.listdir(path):
                    if f == c[0]:
                        result = subprocess.run(c, capture_output=True, text=True)
                        print(result.stdout, " ")
                        found = True
                        break
            if found:
                break

        if not found:
            print(f"{command}: command not found")

if __name__ == '__main__':
    main()
