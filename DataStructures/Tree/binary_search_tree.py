from DataStructures.Tree import bst_node as bn

def get(my_bst, key):
  return search(my_bst, key)
  
def get_recursive(my_bst, key):
  actual=my_bst["root"]
  if actual["key"]==key:
    return bn.get_value(actual)
  else: 
    if key < actual["key"]:
      actual = actual["left"]
    elif key > actual["key"]:
      actual = actual["right"]
    return actual

def put(my_bst, key, value):
    return insert_node(my_bst["root"], key, value)

def insert_node(root, key, value):
    
    if root is None:
        
        root = bn.new_node(key, value)
        
    else : 
        if key < root["key"]:
            root["left"] = insert_node(root["left"],key, value)
        elif key > root["key"]:
            root["right"] = insert_node(root["right"], key, value)
        else:
            root["value"] = value
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    
def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    