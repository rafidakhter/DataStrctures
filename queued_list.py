class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class queuelist:
    #first in first out
    #doubly link based que structure
    def __init__(self):
        self.head=node()
    
    #adds an element to the  linked list:
    def enqueue(self,data):
        newnode=node(data)
        current_node=self.head
        while current_node.next != None:
            current_node=current_node.next
        current_node.next=newnode

    #take first the last element in the queueedlist:   
    def dequeue(self):
        if self.length()<=0:
            print ("ERROR: 'empty list' Index out of range!")
            return None
        head_node=self.head
        first_node=head_node.next
        data=first_node.data
        sec_node=first_node.next
        head_node.next=sec_node
        return data


    def length(self):
        current_node=self.head
        counter=0
        while current_node.next !=None:
            counter +=1
            current_node=current_node.next 
        return counter
    
    #get all element of the queue
    def getallelements(self):

        current_node=self.head
        elements=[]

        while current_node.next != None:
            current_node=current_node.next
            elements.append(current_node.data)

        return elements
        
    #displays all the elements in the queueedlist
    def display(self):
        print(self.getallelements())

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
                #we will be deleting current node:
                last_node.next=current_node.next
                next_node=current_node.next
                return
            counter+=1

mylist=queuelist()
for x in range (0,5):
    mylist.enqueue(x)
    mylist.display()
for x in range (0,5):
    mylist.dequeue()
    mylist.display()
