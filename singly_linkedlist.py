class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=node()
    
    #adds an element to the linked list:
    def append(self,data):
        newnode=node(data)
        current_node=self.head 
        while current_node.next != None:
            current_node=current_node.next
        current_node.next=newnode

    #get the length of the linkedlist using a counter:

    def length(self):
        current_node=self.head
        counter=0
        while current_node.next !=None:
            counter +=1
            current_node=current_node.next 
        return counter

    #returns all the elements in the linkedlist in an array
    def getallelements(self):

        current_node=self.head
        elements=[]

        while current_node.next != None:
            current_node=current_node.next
            elements.append(current_node.data)

        return elements

    #get element of a given index
    def get(self,index):
        if index>=self.length() or index<0:
            print ("ERROR: 'Get' Index out of range!")
            return None
        current_node=self.head
        counter=0
        while True: 
            current_node=current_node.next
            if counter==index:
                return current_node.data
            else:
                counter+=1
    
    #delete an element at a given index:
    def erase(self,index):
        if index>=self.length() or index<0:
            print ("ERROR: 'erase' Index out of range!")
            return
        current_node=self.head
        counter=0
        while True:
            last_node=current_node
            current_node=current_node.next
            if counter==index:
                last_node.next=current_node.next
                return
            counter+=1

    #inserting a new data at a given index
    def insert(self,data,index):
        if index<0:
            print ("ERROR: 'insert' Index out of range!")
            return
        if index>=self.length():
            self.append(data)
            return
        current_node=self.head
        counter=0
        while True:
            last_node=current_node
            current_node=current_node.next
            if counter == index:
                new_node=node(data)
                new_node.next=last_node.next
                last_node.next=new_node
                return
            counter+=1
	# Allows for bracket operator syntax (i.e. a[0] to return first item).
    def __getitem__(self,index):
        return self.get(index)


    #displays all the elements in the linkedlist in an array
    
    def display(self):
        elements=self.getallelements()
        print(elements)



my_list=linkedlist()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

a=my_list.getallelements()
print(f'print all elements = {a}')
print('testing display function')
my_list.display()
b=my_list.get(2)
print(f'testing get function at  2nd index = {b}')
my_list.erase(2)
print(f'Erased 2nd index')
my_list.display()
my_list.insert(3,1)
print(f'inserted 3 at 1st index')
my_list.display()
my_list.erase(2)
print(f'Erased 2nd index')
my_list.insert(2,1)
print(f'inserted 2 at 1st index')
my_list.display()
