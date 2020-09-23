#%%
class Node():
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

#%%
class BinarySearchTree():
    def __init__(self):
        self.root=None

    def insert(self,data):

        newNode=Node(data)

        if(self.root==None):
            self.root=newNode
            return 
        else:   
            currentNode=self.root
            while True:
                if data<currentNode.data:
                    #go left
                    if currentNode.left==None:
                        currentNode.left=newNode

                        return
                    currentNode=currentNode.left
                else:
                    if currentNode.right==None:
                        currentNode.right=newNode
                        return
                    currentNode=currentNode.right

    def lookup(self,data):
        if not self.root:
            return False
        else:   
            currentNode=self.root
            while True:
                if data<currentNode.data:
                    if currentNode.left ==None:
                        return False
                    #go left
                    if currentNode.left.data==data:
                        return currentNode.left
                    currentNode=currentNode.left
                else:
                    if currentNode.right ==None:
                        return False
                    if currentNode.right.data==data:
                        return currentNode.right
                    currentNode=currentNode.right
    def remove(self,data):





# %%
tree= BinarySearchTree()
tree.insert(4)
tree.insert(9)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)

a=tree.lookup(170)
print(a.data)



# %%
tree.lookup(5)
# %%
