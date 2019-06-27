#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os


def create_file():
    file_name = str(input ("please enter the name of the file to be created "))
    file_name = file_name + '.txt'
    f = open(file_name,"w+")
    
    
def remove_file():
    file_name = str(input("please enter the name of the file to be deleted "))
    file_name = file_name + '.txt'
    if os.path.isfile('./' + file_name):
        os.remove(file_name)
        print("File Removed!")
    else:
        print ('file does not exist')

        
def show_file():
    file_name = str(input("please enter the name of the file to be shown "))
    file_name = file_name + '.txt' 
    if os.path.isfile('./' + file_name):
        file = open(file_name, "r")
        for line in file:
            print(line)
    else:
        print('file not found ')
        
        
def update_file():
    file_name = str(input("please enter the name of the file to be updated "))
    file_name = file_name + '.txt'
    choice = str(input ("please enter 'a' for append and 'o' for overwrite "))
    if choice =='a':
        msg = ''
        if os.path.isfile('./' + file_name):
            file = open(file_name, "a")
            while True:
                msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
                if msg != 'e':
                    msg="\n" + msg
                    file.write(msg)
                else: 
                    break
            file.close()
        else:
            print ('file does not exist')
    if choice =='o':
        if os.path.isfile('./' + file_name):
            file = open(file_name, "w")
            while True:
                msg = str(input ("please enter the line of message to be updated to the file or 'e' to end the writing "))
                if msg != 'e':
                    file.write(msg + "\n")
                else:
                    break
            file.close()
        else:
            print ('file does not exist')
        
        
def find_in_file():
    file_name = str(input("please enter the name of the file to do the search in "))
    file_name = file_name + '.txt'
    if os.path.isfile('./' + file_name):
        input_ = str(input("please enter the string you want to find "))
        file = open(file_name, "r")
        for i, line in enumerate(file,1):
            num=line.find(input_)
            if num==0:
                print('string found on line number ' + str(i))
    else:
        print ('File not found ')
        
def replace_in_file():
    file_name = str(input("please enter the name of the file to do the replacing  "))
    file_name = file_name + '.txt'
    if os.path.isfile('./' + file_name):
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
    else:
        print ('file not found')
    
    
def main():
    i=1
    while True:
        print('')
        try:
            i=int(input(' 1. Create a file \n 2. Remove file \n 3. Show the content of the file \n 4. Update file content (Append and overwrite both) \n 5. Search a string in a file \n 6. Replace a word with other word \n 0. Exit Program \n'))

        except ValueError:
              print ("please input a relevant number not string \n")
        else:
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




