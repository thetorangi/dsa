class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def inOrder(self,rootNode):
        if not rootNode:
            return 
        else:
            self.inOrder(rootNode.left)
            print(rootNode.data)
            self.inOrder(rootNode.right)
    
    def preOrder(self,rootNode):
        if not rootNode:
            return
        else:
            print(rootNode.data)
            self.preOrder(rootNode.left)
            self.preOrder(rootNode.right)

    def postOrder(self,rootNode):
        if not rootNode:
            return
        else:
            self.postOrder(rootNode.left)
            self.postOrder(rootNode.right)
            print(rootNode.data)

    def levelOrder(self,rootNode):
        if not rootNode:
            return 
        else:
            curr = rootNode
            queue = []
            res =[]
            queue.append(rootNode)

            while len(queue) > 0 :
                curr = queue.pop(0)
                res.append(curr.data)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            return res
    
    def search(self,rootNode,val):
        if not rootNode:
            return "Not Found"
        else:
            if rootNode.data == val:
                return "Success"
            lf = self.search(rootNode.left,val)
            if lf == "Success":
                return "Success"
            rf = self.search(rootNode.right,val)
            return rf        
    
    def searchLevel(self,rootNode,val):
        if not rootNode:
            return "not Found"
        else :
            curr = rootNode
            queue = []
            res = []
            queue.append(rootNode)
            while len(queue) > 0 :
                curr = queue.pop(0)
                if curr.data == val :
                    return "Success"
                res.append(curr.data)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return "Not Found"

    def ins(seld,rootNode,newNode):
        if not rootNode:
            rootNode = newNode
        else:
            queue = []
            res = []
            curr = rootNode
            queue.append(rootNode)
            while len(queue)  > 0 :
                curr = queue.pop(0)
                res.append(curr.data)
                if curr.left is not None:
                    queue.append(curr.left)
                else:
                    curr.left = newNode
                    return "inserted"
                if curr.right is not None:
                    queue.append(curr.right)
                else:
                    curr.right = newNode
                    return "Inserted SucessFully "

tree = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
tree.left = cold
tree.right = hot
tea = Node("Tea")
coffee = Node("Coffee")
fanta = Node("Fanta")
cola = Node("Cola")
cold.left = fanta
cold.right = cola
hot.left = tea
hot.right = coffee
boost = Node("Boost")

# print("Preorder\n")
# tree.preOrder(tree)
# print("\nInorder\n")
# tree.inOrder(tree)
# print("\nPostOrder\n")
# tree.postOrder(tree)


# print(tree.levelOrder(tree))

# print(tree.ins(tree ,  boost))

# print(tree.levelOrder(tree))

# print(tree.searchLevel(tree , "Tea"))


# print(tree.search(tree , "Colda"))