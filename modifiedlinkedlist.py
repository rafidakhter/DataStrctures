     
class LinkedList(): 
    
    def __init__(self,data):
        self.headData=data
        self.head={
            "data": self.headData,
            next:None}

        self.tail=self.head
        self.length=1 

    def length(self):
        return self.length

    def append(self,data):
        newNode={
            "data":data,
            next:None}
        self.tail[next]=newNode
        self.tail=newNode
        self.length+=1
    
    def prepend(self,data):
        newNode={
            "data":data,
            next:None}
        newNode[next]=self.head
        self.head=newNode
        self.length+=1

    def getallelements(self):

        current_node=self.head
        elements=[self.head["data"]]

        while current_node[next] != None:
            current_node=current_node[next]
            elements.append(current_node["data"])

        return elements

    def display(self):
        elements=self.getallelements()
        print(elements)

        #inserting a new data at a given index
    def insert(self,data,index):
        if index<=0:
            self.prepend(data)
            return
        if index>=self.length:
            self.append(data)
            return
        current_node=self.head
        counter=1
        while True:
            last_node=current_node
            current_node=current_node[next]
            if counter == index:
                newNode={
                "data":data,
                next:None}
                newNode[next]=last_node[next]
                last_node[next]=newNode
                self.length+=1
                return
            counter+=1
    

newlist=LinkedList(10)
newlist.append(5)
newlist.append(16)   
newlist.prepend(1)  
newlist.insert(2,3)  
newlist.insert(2,0)     
newlist.insert(4,3)
newlist.display()
print(newlist.length)