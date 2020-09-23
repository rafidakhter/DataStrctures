#import heapq
def mergeSortedArray(arrays):
    lst=[]
    for x in range(0,len(arrays)):
        lst.extend(arrays[x])
    lst.sort()
    print(lst)

def mergeSortedArray1(array1,array2):
    ret_ary=[]
    i_a=0
    i_b=0
    while len(array1) !=0 and len(array2):
        if array1[i_a]<array2[i_b]:
            ret_ary.append(array1.pop(i_a))
            i_a+=1
        else:
            ret_ary.append(array2.pop([i_a]))
            i_b+=1
    print(ret_ary)
    return ret_ary
    


mergeSortedArray1([1,2,34,5],[2,3,55,6])