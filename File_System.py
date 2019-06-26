#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os

def create_file():
    file_name = str(input ("please enter the name of the file to be created, with .txt ")) 
    f= open(file_name,"w+")
    pass
def remove_file():
    file_name = str(input ("please enter the name of the file to bee deleted, with .txt "))
    os.remove(file_name)
    print("File Removed!")
    pass

def show_file():
    file_name = str(input ("please enter the name of the file to be shown , with .txt ")) 
    file = open(file_name, "r")
    for line in file:
        print (line)
    pass

def update_file():
    file_name = str(input ("please enter the name of the file to be created with .txt ")) 
    msg = str(input ("please enter the message to be updated "))
    choice = str(input ("please enter 'a' for append and 'o' for overwrite "))
    if choice =='a':
        file = open(file_name, "a")
        msg="\n"+msg
        file.write(msg)
        file.close()
    if choice =='o':
        file = open(file_name, "w")
        file.write(msg)
        file.close()
    pass

def find_in_file():
    file_name = str(input ("please enter the name of the file to do the searchin , with .txt "))
    input_ = str(input ("please enter the string you want to find "))
    file = open(file_name, "r")
    i=0
    for line in file:
        num=line.find(input_)
        i+=1
        if num==0:
            print('string found on line number '+ str(i))
        
    pass


def replace_in_file():
    file_name = str(input ("please enter the name of the file to do the replacing , with .txt "))
    input_ = str(input ("please enter the string you want to replace "))
    input1_ = str(input ("please enter the string you want to replace with "))
    file = open(file_name, "r")
    i=0
    file_dump=''
    for line in file:
        file_dump+=line.replace(input_, input1_)
        #print(line)
        #file_dump+=line
    file = open(file_name, "w")
    file.write(file_dump)
    file.close()
    pass


def main():

    i=1

    while i!=0:


        print('1. Create a file ')

        print('2. Remove file ')

        print('3. Show the content of the file ')

        print('4. Update file content (Append and overwrite both) ')
        
        print('5. Search a string in a file ')
        
        print('6. Replace a word with other word ')
        
        print('0. Exit Program ')

        i=int(input())

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
if __name__ == '__main__':

    main()


# In[ ]:




