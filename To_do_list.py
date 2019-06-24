#!/usr/bin/env python
# coding: utf-8

# In[8]:


task_list=[]
status_list=[]

def create_task():
    global task_list
    global status_list
    print('################## Creating a task ##################')
    new_task=str(input("Please input the new task "))
    new_task_status=str(input("Please enter the status for new task "))
    chk=int(input("Please enter 1 to put the task on end or 2 to put the task in between "))
    if(chk==1):
        task_list.append(new_task)
        status_list.append(new_task_status)
        print('')
        print('############# Task added at the end of the List #################')
    else:
        print ('############# Creating a task in between #################')
        print()
        list_task()
        index=int(input('Please enter a task number after which you want to place your task'))
        list1=[]
        list2=[]
        list11=[]
        list22=[]
        i=0
        if index > len(task_list)-1:
            print('invalid index try again ')
        else: 
            index=index+1
            while i < index:
                list1.append(task_list[i])
                list11.append(status_list[i])
                i=i+1
            list1.append(new_task)
            list11.append(new_task_status)
            while i < len(task_list):
                list2.append(task_list[i])
                list22.append(status_list[i])
                i=i+1
            #chunks = [task_list[x:x+chk] for x in range(0, len(task_list), chk)]
            #chunks2 = [task_list[x:x+len[task_list]] for x in range(chk, len(task_list), len(task_list))]
            #task_list=chunks+chunks2
            task_list=list1+list2
            status_list=list11+list22
    
    pass
def list_task():
    print('')
    print('############# Task list is as fallows ############')
    x=0
    print ('Task no ' + '  ' + '  Task          '+ '    Status ')
    while x < len(task_list):
        print (str(x)+ '         ' +str(task_list[x])+'           '+str(status_list[x]) )
        x+=1
    pass

def update_task():
    global task_list
    global status_list
    list_task()
    print('################ updating a task from task list ########################')
    index=int(input('Please enter a task number which you want to Update '))
    list1=[]
    list2=[]
    list11=[]
    list22=[]
    i=0
    if index > len(task_list)-1:
        print('Invalid index try again')
    else :
        while i < index:
            list1.append(task_list[i])
            list11.append(status_list[i])
            i=i+1

        update_task=str(input("Please input the updated task "))
        updated_task_status=str(input("Please enter the status for updated task "))
        list1.append(update_task)
        list11.append(updated_task_status)
        i+=1
        while i < len(task_list):
            list2.append(task_list[i])
            list22.append(status_list[i])
            i=i+1


        task_list=list1+list2
        status_list=list11+list22
    pass




def delete_task():
    global task_list
    global status_list
    list_task()
    print('################ Deleting a task from task list ########################')
    index=int(input('Please enter a task number which you want to Delete '))
    list1=[]
    list2=[]
    list11=[]
    list22=[]
    i=0
    if index > len(task_list)-1:
        print('invalid index try again ')
    else :
        while i < index:
            list1.append(task_list[i])
            list11.append(status_list[i])
            i=i+1
        #list.append(new_task)
        i+=1
        while i < len(task_list):
            list2.append(task_list[i])
            list22.append(status_list[i])
            i=i+1

        task_list=list1+list2
        status_list=list11+list22
    pass
    
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




