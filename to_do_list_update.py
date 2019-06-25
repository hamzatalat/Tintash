#!/usr/bin/env python
# coding: utf-8

# In[ ]:


task_list=[]

def create_task():
    name_=str(input('Enter the name of the task '))
    status_=str(input('Enter the status of the task '))
    check_=int(input('Enter 1 if you want to add the task at end or 2 to do other wise '))
    if check_ == 1:
        task_list.append({ "name": name_,"status": status_})
    else:
        list_task()
        index = int(input("Enter the index at which you want to add your task: "))
        task_list.insert(index,{"name": name_ , "status": status_ })

def list_task():
    for count, itr in enumerate(task_list):
        print(count, "  Name :",itr["name"], "  Status :",itr["status"])
        
def update_task():
    index=int(input('Please enter a task number which you want to Update '))
    name=str(input("Enter new name : "))
    status=str(input("Enter new status : "))
    task_list[index]["name"] = name
    task_list[index]["status"] = status
    
    
def delete_task():
    list_task()
    index = int(input("Enter the task index for the task you want to delete : "))
    del task_list[index]
 
        
def main():
    i=1
    while i!=0:
        print('')
        print('')
        print('1. Create a task ')
        print('2. List task ')
        print('3. Update a task ')
        print('4. Delete a task ')
        print('0. Exit Program ')
        i=int(input())
        if(i==1):
            create_task()
        if(i==2):
            list_task()
        if(i==3):
            update_task()
        if(i==4):
            delete_task()
        


if __name__ == '__main__':
    main()


# In[ ]:




