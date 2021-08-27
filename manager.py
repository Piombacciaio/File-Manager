import ctypes, os, send2trash, shutil, sys

ctypes.windll.kernel32.SetConsoleTitleW(f'File Manager ;) | made by piombacciaio')


disks = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

def nextpage():
    os.system("cls")
    print("""
        ███████╗██╗██╗     ███████╗  ███╗   ███╗ █████╗ ███╗  ██╗ █████╗  ██████╗ ███████╗██████╗   ██╗ ██╗  
        ██╔════╝██║██║     ██╔════╝  ████╗ ████║██╔══██╗████╗ ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗  ╚═╝ ╚██╗ 
        █████╗  ██║██║     █████╗    ██╔████╔██║███████║██╔██╗██║███████║██║  ██╗ █████╗  ██████╔╝       ╚██╗
        ██╔══╝  ██║██║     ██╔══╝    ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║  ╚██╗██╔══╝  ██╔══██╗  ██╗  ██╔╝
        ██║     ██║███████╗███████╗  ██║ ╚═╝ ██║██║  ██║██║ ╚███║██║  ██║╚██████╔╝███████╗██║  ██║  ╚█║ ██╔╝ 
        ╚═╝     ╚═╝╚══════╝╚══════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚╝ ╚═╝
    _____________________________________________________________________________________________________________
                            V 0.0.0                            made by piombacciaio                             \n\n""")

# Lists each folder and file present in the current working directory
def listDirs():
    listed_dir = os.listdir(os.getcwd())
    print()
    for x in listed_dir:
        print("- " + x)

while True:
    nextpage()
    print("1.Open files or folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")

    user_input = input("Please choose one of the options: ")
    if user_input == '1':
        nextpage()

        # Main page

        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')
        print('Available disks: ')

        for n in range(len(disks)):
            print(str(5 + n) + '. ' + disks[n])
        
        while True:
            inp = input("\nEnter your Choice: ")

            if inp == '1':
                nextpage()
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '2':
                nextpage()
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                nextpage()
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                nextpage()
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in disks:
                nextpage()
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / disk name.\n')


        while True:

            listDirs()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    os.system('"' + res + '"')

                else:
                    os.chdir(res)

            elif res == 'exit':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == 'back':                          # Back command to go up one directory
                os.chdir('..')
                nextpage()

            else:
                print('Nothing found with this name.')

    # Rename page

    if user_input == '2':

        nextpage()
        print("You chose to rename")
        print('disks: ')

        for x in range(len(disks)):
            print(str(1 + x) + '. ' + disks[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in disks:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct drive name.\n')

        while True:
            listDirs()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "rename" to rename this directory')
            res = input('\nChoose a file to rename: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    new_name = input("Enter a new name: ")
                    original_directory = res
                    new_directory = os.getcwd() + '\\' + new_name
                    shutil.move(original_directory, new_directory)

                else:
                    os.chdir(res)

            elif res == 'exit':    # Exit command to exit from loop
                sys.exit(0)

            elif res == 'back':    # Back command to go up one directory
                os.chdir('..')
                nextpage()

            elif res == 'rename':  # Rename command to delete one directory
                new_name = input("Enter a new name: ")
                original_directory = os.getcwd()
                os.chdir('..')
                new_directory = os.getcwd() + '\\' + new_name
                shutil.move(original_directory, new_directory)
                
            else:
                print('Nothing found with this name.')

    
    # Move page
    if user_input == '3':

        nextpage()
        print("You chose to move")
        print('disks: ')

        for x in range(len(disks)):
            print(str(1 + x) + '. ' + disks[x])

        while True:
            inp = input("\nEnter your Choice: ")

            if inp in disks:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirs()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "cut" to move this directory')
            res = input('\nChoose a file to move: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nMove " + res + " to a desired location.")

                    while True:

                        for x in range(len(disks)):
                            print(str(1 + x) + '. ' + disks[x])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in disks:
                            os.chdir(inp2 + '\\')
                            break

                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:

                        listDirs()
                        print('Type "paste" to paste this file in current directory')
                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):

                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")

                            else:
                                os.chdir(res2)

                        elif res2 == 'paste':
                            shutil.move(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)

            elif res == 'exit':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == 'back':                          # Back command to go up one directory
                os.chdir('..')
                nextpage()

            elif res == 'cut':

                og_path = os.getcwd()
                print("Moving the current directory")

                while True:

                    for x in range(len(disks)):
                        print(str(1 + x) + '. ' + disks[x])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in disks:
                        os.chdir(inp2 + '\\')
                        break

                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirs()
                    print('\nType "paste" to paste this folder in current directory')
                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):

                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")

                        else:
                            os.chdir(res2)

                    elif res2 == 'paste':
                        shutil.move(og_path, os.getcwd())
                        break

            else:
                print('Nothing found with this name.')

                
    # Copy page
    if user_input == '4':

        nextpage()
        print("You chose to copy")
        print('disks: ')

        for x in range(len(disks)):
            print(str(1 + x) + '. ' + disks[x])

        while True:

            inp = input("\nEnter your Choice: ")

            if inp in disks:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct drive name.\n')

        while True:

            listDirs()
            print('\n\nType "exit" to exit from file manager.')
            print('Type "back" to go up one directory.')
            print('Type "copy" to copy this directory')
            res = input('\nChoose a file to copy: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):

                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res + " to a desired location.")

                    while True:

                        for x in range(len(disks)):
                            print(str(1 + x) + '. ' + disks[x])

                        inp2 = input("\nEnter your Choice: ")

                        if inp2 in disks:
                            os.chdir(inp2 + '\\')
                            break

                        else:
                            print('Error\nEnter a correct drive name.\n')

                    while True:

                        listDirs()
                        print('Type "paste" to copy this file in current directory')
                        res2 = input('\nChoose a file to move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):

                            if os.path.isfile(res):
                                print("You can't choose a file.\nPlease choose a folder.")

                            else:
                                os.chdir(res2)

                        elif res2 == 'paste':
                            shutil.copy(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)

            elif res == 'exit':  # Exit command to exit from loop
                sys.exit(0)

            elif res == 'back':  # Back command to go up one directory
                os.chdir('..')
                nextpage()

            elif res == 'copy':

                og_path = os.getcwd()
                print("Copying the current directory")

                while True:

                    for x in range(len(disks)):
                        print(str(1 + x) + '. ' + disks[x])

                    inp2 = input("\nEnter your Choice: ")

                    if inp2 in disks:
                        os.chdir(inp2 + '\\')
                        break

                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirs()
                    print('\nType "paste" to copy this file in current directory')
                    res2 = input('\nChoose a folder to open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):

                        if os.path.isfile(res):
                            print("You can't choose a file.\nPlease choose a folder.")

                        else:
                            os.chdir(res2)

                    elif res2 == 'paste':

                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break

            else:
                print('Nothing found with this name.')


    # Delete Page
    if user_input == '5':

        while True:

            nextpage()
            print('\n1. Permanently \n2. Recycle Bin')
            user_input = input('Would you like to permanently delete or send to Recycle Bin?: ')

            if user_input == '1':
                
                nextpage()
                print('You chose to permanently delete files/folders.\n')
                print('disks: ')

                for x in range(len(disks)):
                    print(str(1 + x) + '. ' + disks[x])

                while True:

                    inp = input("\nEnter your Choice: ")

                    if inp in disks:
                        os.chdir(inp + '\\')
                        break

                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirs()
                    print('\n\nType "exit" to exit from file manager.')
                    print('Type "back" to go up one directory.')
                    print('Type "delete" to permanently delete this directory')
                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):

                        if os.path.isfile(res):
                            print('Are you sure you want to permanently delete this file? (YES/NO)')
                            ans = input('Yes or No: ')

                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)

                            elif ans.lower() == "no" or "n":
                                print("operation aborted")

                        else:
                            os.chdir(res)

                    elif res == 'exit':                      # Exit command to exit from loop
                        sys.exit(0)

                    elif res == 'back':                      # Back command to go up one directory
                        os.chdir('..')
                        nextpage()

                    elif res == 'delete':                    # Delete command to delete one directory
                        print('Are you sure you want to permanently delete this folder? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)
                        
                        elif ans.lower() == "no" or "n":
                            print("operation aborted")

                    else:
                        print('Nothing found with this name.')

            elif user_input == '2':

                nextpage()
                print('You chose to temporarily delete files/folders.')
                print('disks: ')

                for x in range(len(disks)):
                    print(str(1 + x) + '. ' + disks[x])

                while True:

                    inp = input("\nEnter your Choice: ")
                    if inp in disks:
                        os.chdir(inp + '\\')
                        break

                    else:
                        print('Error\nEnter a correct drive name.\n')

                while True:

                    listDirs()
                    print('\n\nType "exit" to exit from file manager.')
                    print('Type "back" to go up one directory.')
                    print('Type "delete" to send this directory to recycle bin')
                    res = input('\nChoose a file to delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):

                        if os.path.isfile(res):
                            # Warning to prevent accidental deletion
                            print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                            ans = input('Yes or No: ')

                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)

                            elif ans.lower() == "no" or "n":
                                print("operation aborted")

                        else:
                            os.chdir(res)

                    elif res == 'exit':  # Exit command to exit from loop
                        sys.exit(0)

                    elif res == 'back':  # Back command to go up one directory
                        os.chdir('..')
                        nextpage()

                    elif res == 'delete':  # Delete command to delete one directory
                        
                        print('Are you sure you want to send this folder to recycle bin? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)

                        elif ans.lower() == "no" or "n":
                            print("operation aborted")
                                                   
                    else:
                        print('Nothing found with this name.')
    else:
        print('You chose wrong number')