import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    # def addChild(self,TreeNode):
    #     self.children.append(TreeNode)

    # def __str__(self,level=0):
    #     res = " " * level +str(self.data) + "\n"
    #     for child in self.children:
    #         res += child.__str__(level+1)
    #     return res
    
tree = TreeNode("Drinks" )

cold = TreeNode("Cold")
hot = TreeNode("Hot")

tree.left = hot
tree.right = cold

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

fanta = TreeNode("Fanta" )
cola = TreeNode("Cola" )

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)


def postOrder(rootNode):
    if not rootNode:
        return
    preOrder(rootNode.left)
    preOrder(rootNode.right)
    print(rootNode.data)

def inOrder(rootNode):
    if not rootNode:
        return
    preOrder(rootNode.left)
    print(rootNode.data)
    preOrder(rootNode.right)

def levelOrder(rootNode):
    if not rootNode:
        return
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.left is not None:
            customQueue.enqueue(root.value.left)
        if root.value.right is not None:
            customQueue.enqueue(root.value.right)
    

print("----- Pre Order Taversal ----")
preOrder(tree)
print("----- In Order Taversal ----")
inOrder(tree)
print("----- Post Order Taversal ----")
postOrder(tree)
print("----- Level Order Taversal ----")
levelOrder(tree)