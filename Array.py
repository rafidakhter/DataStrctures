class Array:
    def __init__(self):
         self.length=0
         self.data={} # creats a set where when all the data is stoded as a dictionary
                      # becuase it is stodes as a dictionary the get function is O(1)

    def shiftItem(self,index):
        for i in range (index,self.length-1):
            self.data[i]= self.data[i+1]
        del self.data[self.length-1]
        self.length-=1


    def __str__(self):
        return(f"length:{self.length}, data: {self.data}")

    def get(self,index):
        return self.data[index]
    
    def push(self,item):
        self.data[self.length]=item
        self.length +=1
        return self.length
    
    def pop(self):
        lastitem=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastitem
    
    def delete(self,index):
        item = self.data[index]
        self.shiftItem(index)
        #self.length-=1
        return item
    
    
  

 

newArray=MyArray()
newArray.push("hi")
newArray.push("!")
newArray.push("you")
newArray.push("are")
newArray.push("nice")
newArray.push("WTF")

print(newArray)
newArray.pop()
print(newArray)
newArray.delete(0)
print(newArray)
newArray.delete(0)
print(newArray)

