from DataStructures.Tree import bst_node as bn

def new_map():
    return {"root": None}

def put(my_bst, key, value):
    my_bst = insert_node(my_bst["root"], key, value)
    return my_bst

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
    return root

def get(my_bst, key):
    respuesta = get_node(my_bst["root"], key)
    if respuesta is not None:
        return bn.get_value(respuesta)
    else:
        return None

def get_node(root, key):
    if root is None:
        return None
    if key == bn.get_key(root):
        return root
    elif key < bn.gey_key(root):
        return get_node(root["left"], key)
    else: 
        return get_node(root["right"], key)

    
def size(my_bst):
    return size_tree(my_bst["root"])
     
def size_tree(root):
    if root is None:
        return 0
    else:
        return root["size"]

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

    