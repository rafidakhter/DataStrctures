class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.previous=None

class stackedlist:

    def __init__(self):
        self.head=node()
    
    #adds an element to the end of stackedlist:
    def push(self,data):
        newnode=node(data)
        current_node=self.head
        while current_node.next != None:
            current_node=current_node.next
        current_node.next=newnode
        newnode.previous=current_node

    #take out the last element in the stackedlist:   
    def pop(self):
        current_node=self.head
        while current_node.next != None:
            lastnode=current_node
            current_node=current_node.next
        lastnode.next=None
        return current_node.data

    #get the length of the stackedlist using a counter:
    def length(self):
        current_node=self.head
        counter=0
        while current_node.next !=None:
            counter +=1
            current_node=current_node.next 
        return counter

    #get all element of the stack
    def getallelements(self):

        current_node=self.head
        elements=[]

        while current_node.next != None:
            current_node=current_node.next
            elements.append(current_node.data)

        return elements
    
    
    #displays last element in the stackedlist
    def peek(self):
        current_node=self.head
        while current_node.next !=None:
            current_node=current_node.next 
        print(current_node.data)

    #empty check
    def is_empty(self):
        return self.length==0
    
    #displays all the elements in the stackedlist
    def display(self):
        print(self.getallelements())

