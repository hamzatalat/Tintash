#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
def create_file():
    file_name = str(input ("please enter the name of the file to be created, with .txt ")) 
    f = open(file_name,"w+")
def remove_file():
    file_name = str(input("please enter the name of the file to be deleted, with .txt "))
    os.remove(file_name)
    print("File Removed!")
def show_file():
    file_name = str(input("please enter the name of the file to be shown , with .txt ")) 
    file = open(file_name, "r")
    for line in file:
        print(line)
def update_file():
    file_name = str(input("please enter the name of the file to be updated with .txt ")) 
    choice = str(input ("please enter 'a' for append and 'o' for overwrite "))
    if choice =='a':
        msg = ''
        file = open(file_name, "a")
        while True:
            msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
            if msg != 'e':
                msg="\n" + msg
                file.write(msg)
            else: 
                break
        file.close()
    if choice =='o':
        file = open(file_name, "w")
        while True:
            msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
            if msg != 'e':
                file.write(msg + "\n")
            else:
                break
        file.close()
def find_in_file():
    file_name = str(input("please enter the name of the file to do the search in , with .txt "))
    input_ = str(input("please enter the string you want to find "))
    file = open(file_name, "r")
    for i, line in enumerate(file,1):
        num=line.find(input_)
        if num==0:
            print('string found on line number ' + str(i))
            
def replace_in_file():
    file_name = str(input("please enter the name of the file to do the replacing , with .txt "))
    input_ = str(input("please enter the string you want to replace "))
    input1_ = str(input("please enter the string you want to replace with "))
    file = open(file_name,"r")
    i=0
    file_dump=''
    for line in file:
        file_dump += line.replace(input_,
                                  input1_)
    file = open(file_name, "w")
    file.write(file_dump)
    file.close()
def main():
    i=1
    while True:
        print('')
        i=int(input(' 1. Create a file \n 2. Remove file \n 3. Show the content of the file \n 4. Update file content (Append and overwrite both) \n 5. Search a string in a file \n 6. Replace a word with other word \n 0. Exit Program \n'))
        if i==1 :
            create_file()
        if i==2 :
            remove_file()
        if i==3 :
            show_file()
        if i==4 :
            update_file()
        if i==5 :
            find_in_file()
        if i==6 :
            replace_in_file()
        if i==0 :
            break
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




