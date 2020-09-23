class Node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class modifiedStacks():

    def __init__(self,data=None):
        self.head=Node(data)
        self.length=1
    
    def peek(self):
        return self.head.data

    def push(self,data):
        newNode=Node(data)
        oldnode=self.head
        self.head=newNode
        self.head.next=oldnode
        self.length+=1
        return

    def pop(self):
        head=self.head
        self.head=self.head.next
        self.length-=1
        return head.data
    
    def isEmpty(self):
        if self.length==0:
            return True
        return False
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
    
    def isPalindrome(self):
        stack=[]
        pointer=self.head
        counter=0
        if pointer.next==None:
            return False
        while pointer.next!=None:
            if counter==0:
                stack.append(pointer.data)
                pointer=pointer.next
            else:
                if pointer.data == stack[len(stack)-1]:
                    stack.pop()
                else:
                    stack.append(pointer.data)
                pointer=pointer.next
            counter+=1
        if len(stack)==0:
            return True
        return False



newlist=modifiedStacks(0)

print(newlist.isPalindrome())
