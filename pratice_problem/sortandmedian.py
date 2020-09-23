def findMedian(array1,array2):
    sortedArray=sortedAry(array1,array2)
    n=len(sortedArray)
    if n%2==0:
        try:
            median1=sortedArray[(n-1)//2]
        except:
            median1=0
        try:
            median2=sortedArray[n//2]
        except:
            median2=0
        print(median1)
        print(median2)
        median=(median1+median2)/2
    else:
        median=sortedArray[n//2]
    return median

   def sortedAry(array1,array2):
        #if the arrays are empty returns the corresponding array
        if len(array1)==0:
            return num2
        elif len(array2)==0:
            return num1
        
        sortAry=[]
        array2Item=array2[0]
        array1Item=array1[0]

        #while loop will be excicuted until the arrays areempty
        while array1 or array2:
        #compares the first item each array which ever is smaller gets appended to sortAry
            if array1 and array1Item<=array2Item or not array2:
                array1Item=array1.pop(0)
                sortAry.append(array1Item)
                if not array1:
                    pass
                else:
                    array1Item=array1[0]
            else:
                if not array2:
                    pass
                else:
                    array2Item=array2.pop(0)
                    sortAry.append(array2Item)
                    if not array2:
                        pass
                    else:
                        array2Item=array2[0]
        print(sortAry)
        return sortAry