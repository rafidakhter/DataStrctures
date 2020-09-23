import sys
sys.path.insert(0,r'C:\Users\rafid\Desktop\DataStructures')

from stacked_list import *
import heapq

def stringreverse(string):
#finding the reverse of "we will conquere COVID-19" usinck stacked data structured
    mylist = stackedlist()
    for st in string: #O(n)
        mylist.push(st)
    temp_ary=[]
    for x in range(0, mylist.length()): #O(n)
        temp_ary.append(mylist.pop())

    separator=""
    reverse=separator.join(temp_ary)
    return reverse

##not effecient because the funtion split called in 
def stringreverse1(string):
    spl=string
    rev=[]
    for x in range(len(spl)-1,0,-1): #O(n)
        rev.append(spl[x] )
    rev.append(spl[0])
    separator=""
    rev1=separator.join(rev)
    return rev1

def stringreverse3(string):
    rev=[]
    i=-1
    heapq.heapify(rev) 
    for char in string:
        heapq.heappush(rev,(i,char))
        i-=1
    temp=[]
    for char in string:
        a=heapq.heappop(rev)
        temp.append(a[1])
        separator=""
    rev1=separator.join(temp)
    return rev1
    





rev=stringreverse("we will conquere COVID-19")
rev2=stringreverse1("we will conquere COVID-19")
rev3=stringreverse3("we will conquere COVID-19")

print(rev2)
print(rev)
print(rev3)

