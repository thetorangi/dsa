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

    def disp(self,rootNode):
        if not rootNode:
            return
        self.disp(rootNode.left)
        print(rootNode.data)
        self.disp(rootNode.right)
    
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
            self.inOrder(rootNode.left)
            self.inOrder(rootNode.right)

    def postOrder(self,rootNode):
        if rootNode is None:
            return
        else:
            self.inOrder(rootNode.left)
            self.inOrder(rootNode.right)
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

BST = treeNode(None)

BST.disp(BST)

BST.insert(BST,40)
BST.insert(BST,60)
BST.insert(BST,70)
BST.insert(BST,50)
BST.insert(BST,30)
BST.insert(BST,10)

# BST.inOrder(BST)

print(BST.levelOrder(BST))


print(BST.search(BST,90))