from stacked_list import *

def stringreverse(string):
#finding the reverse of "we will conquere COVID-19" usinck stacked data structured
    strings=string
    mylist = stackedlist()
    for string in strings:
        mylist.push(string)
    temp_ary=[]
    for x in range(0, mylist.length()):
        temp_ary.append(mylist.pop())

    separator=""
    reverse=separator.join(temp_ary)
    return reverse

rev=stringreverse("we will conquere COVID-19")
print(rev)