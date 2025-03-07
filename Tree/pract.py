class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,rootNode,data):
        if rootNode.data == None:
            rootNode.data = data
        elif rootNode.data >= data :
            if rootNode.left is None:
                rootNode.left = treeNode(data)
            else:
                self.insert(rootNode.left , data)
        else:
            if rootNode.right is None:
                rootNode.right = treeNode(data)
            else:
                self.insert(rootNode.right , data)
        
    def inOrder(self,rootNode):
        if not rootNode:
            return
        else :
            self.inOrder(rootNode.left)
            print(rootNode.data)
            self.inOrder(rootNode.right)
        
    def levelOrder(self,rootNode):
        if not rootNode:
            return 
        else:
            temp = rootNode
            queue =[]
            res =[]
            queue.append(temp)
            while len(queue) > 0:
                temp = queue.pop(0)
                res.append(temp.data)
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
        return res
    
    def search(self,rootNode,data):
        if not rootNode:
            return "Not Found"
        if rootNode.data == data :
            return "Yes"
        elif data <= rootNode.data:
            lf = self.search(rootNode.left,data)
            if lf == "Yes":
                return "Yes"
        else:
            rg = self.search(rootNode.right,data)
            return rg




BST = treeNode(None)

BST.insert(BST,10)
BST.insert(BST,5)
BST.insert(BST,20)
BST.insert(BST,2)

# BST.inOrder(BST)


print(BST.levelOrder(BST))


print(BST.search(BST,2))