class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class modifiedQueue():

    def __init__(self,data):
        self.head=Node(data)
        self.tail=self.head
        self.length=1
    
    def peek(self):
        return self.head.data

    def enqueue(self,data):
        newNode=Node(data)
        if self.length<=0:
            self.head=newNode
            self.tail=newNode
            return
        self.tail.next=newNode
        self.tail=newNode
        self.length+=1

    def dequeue(self):
        if self.length<0:
            print ("ERROR: 'empty list' Index out of range!")
            return None
        holdingpointer=self.head
        if self.length==0:
            self.head=None
            self.length-=1
            return holdingpointer.data

        self.head=self.head.next
        self.length-=1
        return holdingpointer.data
    
    def isEmpty(self):
        if self.length==0:
            return True
        return False
    
    def getallelements(self):

        current_node=self.head
        if self.length==0:
            return
        elements=[self.head.data]

        while current_node.next != None:

            current_node=current_node.next
            elements.append(current_node.data)
        return elements
        
    #displays all the elements in the queueedlist
    def display(self):
        print(self.getallelements())

newlist=modifiedQueue(0)
newlist.display()
for x in range(1,11):
    newlist.enqueue(x)
    newlist.display()

for x in range(0,newlist.length):
    newlist.dequeue()
    newlist.display()
print(newlist.length)
print(newlist.isEmpty())
newlist.display()