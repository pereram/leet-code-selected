class Node:
# three properties of a node:  val, left and right
    
    def __init__(self,val):

        self.val=val
        self.right=None
        self.left=None

# print all the leaves in the tree.
def leaves(root,lst):

    if root is None:
        return lst
# if reached a leaf, append it's value to the list
    if root.left is None  and root.right  is None:
        lst.append(root.val)
        return lst
    
    lst=leaves(root.left,lst)
    lst=leaves(root.right,lst)
   
    return lst

# given the root node and the value of the key to be inserted
def insert(node,key):

# if there's no root node, then  create a new Node with the given key and return it.
    if node is None:
        return Node(key)
# at the leaf level(or if there's no root )  then the returned newly cretaed Node(key) will be assigned to node.left 
    if key<node.val:
       node.left= insert(node.left,key)

    elif key> node.val:
        node.right=insert(node.right,key)
#after new assignement(or not) return the node (or current root) to upper level.Above leaf level, it keeps assigning same old values to the left/right nodes.
    return node

# insert values and build the tree
root=None
root=insert(root,50)
insert(root,40)
insert(root,30)
insert(root,60)
insert(root,80)
insert(root,45)
insert(root,20)


lst=[]

levs=leaves(root,lst)

print(levs)