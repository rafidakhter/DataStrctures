# Python code to demonstrate working of 
# heapify(), heappush() and heappop() 

# importing "heapq" to implement heap queue 
import heapq 

# initializing list 
li = []
Alphabets=["A","C","B","D"] 
listing={
    "A":-1,
    "B":-2,
    "C":-3,
    "D":-4

}

# using heapify to convert list into heap 
heapq.heapify(li) 

# printing created heap 
print ("The created heap is : ",end="") 
print (list(li)) 

# using heappush() to push elements into heap 
# pushes 4 
for alph in Alphabets:
    num=listing[alph]
    heapq.heappush(li,(num,alph)) 

# printing modified heap 
print ("The modified heap after push is : ",end="") 
print (list(li)) 

# using heappop() to pop smallest element 
a=heapq.heappop(li)
print(a[1])
print(len(li))


