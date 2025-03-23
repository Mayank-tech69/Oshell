import sys
import os
import subprocess
import shutil
import readline
prev_dir = None


def main():
    global prev_dir
    while True:
        #history = []

        current_dir = os.getcwd()
        sys.stdout.write(f"Current Working Directory is : {current_dir}\n")

        sys.stdout.write("# ")
        sys.stdout.flush()
        command = input()

        if command.strip():
            # history.append(command)
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
            for s in c[1:]:
                if s in ['speak', 'exit', 'type']:
                    print(f"{s} is a shell builtin command")
                else:
                    found = False
                    paths = os.getenv("PATH").split(";" if os.name == "nt" else ":")  
                    
                    for path in paths:
                        if os.path.isdir(path):
                            for ext in ([""] if os.name != "nt" else os.getenv("PATHEXT").split(";")):
                                full_path = os.path.join(path, s + ext)
                                if os.path.exists(full_path):
                                    print(f"{s} is {full_path}")
                                    found = True
                                    break
                        if found:
                            break
                    
                    if not found:
                        print(f"{s}: not found")
            continue

        if c[0] == 'clear':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            continue

        #directory manupulation

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
                directory_name = c[1]
                try:
                    os.mkdir(directory_name)
                    print(f"Directory:{directory_name} created successfully")
                except FileExistsError:
                    print(f"Error: The directory '{directory_name}' already exists.")
                except PermissionError:
                    print(f"Error: Permission denied to create '{directory_name}'.")
                except Exception as e:
                    print(f"Error: {e}")
            continue

        if c[0] == 'removedir':
            if len(c) > 1:
                directory_name = c[1]
                try:
                    
                    # os.rmdir(directory_name) does not remove directories when not empty
                    shutil.rmtree(directory_name) # forcefully remove the entire directory
                    print(f"Directory:{directory_name} removed successfully")
                except FileExistsError:
                    print(f"Error: The directory '{directory_name}' does not exists.")
                except PermissionError:
                    print(f"Error: Permission denied to remove '{directory_name}'.")
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
            #if len(c)>1:
            try:
                print(os.getcwd())
            except Exception as e:
                print(e)
            continue

        if c[0] == 'changedir' and c[1] == '-' or c[0]=='changedir' and c[1] == "..":
            if prev_dir:
                os.chdir(prev_dir)
                print(f"Directory successfully changed to {prev_dir}")
            else:
                print("No previous directory to return to")
            continue

        
        
        # file handling
        if c[0]=='createfile':
            try:
                with open(f"{c[1]}", "w") as f:
                    f.write(" ")
                print(f"{c[1]}: file created succesfully")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")
            continue
        if c[0]=='delfile':
            try:
                os.remove(c[1])
                print(f"{c[1]}: file deleted succesfully")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")
            continue
        
        if c[0]== "writefile":
            try:
                with open(f"{c[1]}", "w") as f:
                    writer = input("Enter the Content you want to write: ")
                    f.write(writer)
                print(f"file {c[1]}: data written succesfully")

            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(e)
            continue

        if c[0]== "appendfile":
            try:
                with open(f"{c[1]}", "a") as f:
                    writer = input("Enter the Content you want to append: ")
                    f.write(writer)
                print(f"file {c[1]}: data appended succesfully")

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
