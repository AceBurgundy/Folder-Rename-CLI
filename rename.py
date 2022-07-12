import re
import os
import sys 

def clear():
    os.system("cls")
    
def prompt():
    
    proceed = input("\n    Continue? Y|N: ")
    
    while not 'Y' or not 'N':
        proceed = input("\n    Continue? Y|N: ")
        
    if proceed == 'Y':
        return True

    elif proceed == 'N':
        print("    Cautious are we?")
        sys.exit(0)
         
def fixPathName(location):
    pattern = re.compile(r'\s+')
    if "\\" in location:
        folder_directory = re.sub(pattern, ' ', location.replace("\\","/"))
        return folder_directory
    else:
        print("    this is not a directory")

def remove_words(folders):
    clear()
    print("""\n
    Enter the files you want to remove (separate each one with a comma) ex: (C89),(C90),[English],~,1080p")
    for words in parenthesis ex: (English Sub)
    separate them like this => (English , Sub) 

    To prevent errors, I advice you to do this on the notepad first 

    Shortcuts for copy and pasting in the terminal is ctrl + shift + key\n""")
    
    items = {input("    Enter here: ")}
    items_to_remove = ",".join(items).split()
    
    for name in range(len(folders)):
        result = [word for word in folders[name].split() if word not in items_to_remove]
        os.rename(folders[name], " ".join(result))
        
def incrementFolders(folders):
    clear()
    print("""\n
    Simply adds numbers to each folder name to sequentialize them\n
""")
    if prompt():
        for name in range(len(folders)):
            if name < 10:
                os.rename(folders[name], folders[name] + " 0" + str(name))
            else:
                os.rename(folders[name], folders[name] + " " + str(name))


def choose(location):
    clear()
    os.chdir(location)
    folders = os.listdir(location)
    
    print("""\nChoose from the following options
          
              Remove unnecessary details like: [English] [1080] 480p Engsub         press 1
              Add a number to sequence all your files                               press 2
              Remove all symbols from the folders name                              press 3
              Default (remove unnecessary details and sequence all folders)         press 4\n""")
    
    option = int(input("    Choose: "))
    
    if option == 1:
        remove_words(folders),
    elif option == 2:
        incrementFolders(folders),
    elif option == 3:
        remove_symbols(folders),
    elif option == 4:
        basic(folders),
    else:
        print("    Invalid input")
              
        
def main():
    location = fixPathName(input("""
    Folder Renaming System in python
    
    Features
        Remove unwanted folder details like "[English], Eng Sub, 1080p"
        Remove unwanted symbols like -*&^%
        Add numbers to each folder name to sequentialize them
        Combine 1st and 2nd
        
    To start, copy the path of the parent folder you want to manage
    
    ex: D:\Parent\Child
    
    path: 
"""))
    
    choose(location)
    
if __name__ == '__main__':
    main()