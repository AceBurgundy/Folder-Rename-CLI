import re
import os

def clear():
    os.system("cls")
    
def fixPathName(location):
    pattern = re.compile(r'\s+')
    if "\\" in location:
        folder_directory = re.sub(pattern, ' ', location.replace("\\","/"))
        return folder_directory
    else:
        print("    this is not a directory")

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
        Add numbers to each folder to sequentialize them
        Combine 1st and 2nd
        
    To start, copy the path of the parent folder you want to manage
    
    ex: D:\Parent\Child
    
    path: 
"""))
    
    choose(location)
    
if __name__ == '__main__':
    main()