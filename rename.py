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