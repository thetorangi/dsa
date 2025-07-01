#binary Search Tree

class treeNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self ,rootNode, value):
        if rootNode.data == None:
            rootNode.data = value
        elif value <= rootNode.data :
            if rootNode.left == None:
                rootNode.left = treeNode(value)
            else:
                self.insert(rootNode.left,value)
        else:
            if rootNode.right == None:
                rootNode.right = treeNode(value)
            else:
                self.insert(rootNode.right,value)
        
        return "Added Sucessfully"

    
    def inOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            self.inOrder(rootNode.left)
            print(rootNode.data)
            self.inOrder(rootNode.right)

    def preOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            print(rootNode.data)
            self.preOrder(rootNode.left)
            self.preOrder(rootNode.right)

    def postOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            self.postOrder(rootNode.left)
            self.postOrder(rootNode.right)
            print(rootNode.data)

    def levelOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            curr = rootNode
            queue = []
            ans = []
            queue.append(curr)
            while len(queue) > 0 :
                curr = queue.pop(0)
                ans.append(curr.data)
                if curr.left is not None :
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return ans

    def search(self,rootNode,value):
        if not rootNode:
            return "Not Found"
        if rootNode.data == value :
            return "Value Found"
        elif rootNode.data > value:
            lf = self.search(rootNode.left,value)
            if lf == "Value Found":
                return "Value Found"
        else:
            rf =self.search(rootNode.right,value)
            return rf
        
    def delete(self,rootNode,value):
        if not rootNode:
            return rootNode
        if value < rootNode.data:
            rootNode.left = self.delete(rootNode.left,value)
        elif value > rootNode.data:
            rootNode.right = self.delete(rootNode.right,value)
        else:
            if rootNode.left is None:
                temp = rootNode.right
                rootNode = None
                return temp
            if rootNode.right is None:
                temp = rootNode.left
                rootNode = None
                return temp
            
            curr = rootNode.right
            while curr.left:
                curr = curr.left
            rootNode.data = curr.data
            rootNode.right = self.delete(rootNode.right,curr.data)
        return rootNode
    
    def delBST(self,rootNode):
        rootNode.data = None
        rootNode.left = None
        rootNode.right = None
        return "Done"

BST = treeNode(None)


BST.insert(BST,40)
BST.insert(BST,30)
BST.insert(BST,50)
BST.insert(BST,20)
BST.insert(BST,35)
BST.insert(BST,45)
BST.insert(BST,55)
BST.insert(BST,42)
BST.insert(BST,41)


print(BST.levelOrder(BST))
