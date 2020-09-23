def findMatch(array):
    history={}
    for elm in array:
        if elm in history.keys():
            print(f"matching element is {elm}")
            return elm
        else:
            history[elm]=True
    return None
 
Array1=[2,5,1,2,3,5,1,2,4]
Array2=[2,1,1,2,3,5,1,2,4]
Array3=[1,2,3,4]

findMatch(Array1)
findMatch(Array2)
findMatch(Array3)
