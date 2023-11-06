class Node:
    def __init__(self, data):
        self.number = data[1]
        self.coor = data[0]
        self.left = None
        self.right = None
    
def add_node(node, data):
    if node.coor[0] > data[0][0]:
        if not node.left:
            node.left = Node(data)
        else:
            add_node(node.left, data)
    elif node.coor[0] < data[0][0]:
        if not node.right:
            node.right = Node(data)
        else:
            add_node(node.right, data)
            
def preorder(root, order):
    if root:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)

def postorder(root, order):
    if root:
        preorder(root.left, order)
            preorder(root.right, order)
        order.append(root.number)

def solution(nodeinfo):
    info_number = []
    for i in range(len(nodeinfo)):
        info_number.append([nodeinfo[i], i + 1])
        
    info_number = sorted(info_number, key = lambda x: x[0][1], reverse = True)
    root = Node(info_number[0])
    
    for i in info_number:
        add_node(root, i)
    
    preorder_list = []
    preorder(root, preorder_list)
    print(preorder_list)
    
    postorder_list = []
    postorder(root, postorder_list)
    print(postorder_list)
    
    return [preorder_list, postorder_list]

print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))