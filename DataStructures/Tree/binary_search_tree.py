from DataStructures.Tree import bst_node as bn
from DataStructures.List import  single_linked_list as sl

def new_map():
    return {"root": None}

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
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
    elif key < bn.get_key(root):
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

def contains(my_bst, key):
    res = get(my_bst, key)
    if res is not None:
        return True
    else:
        return False

def is_empty(my_bst):
    return size(my_bst) == 0

def key_set(my_bst):
    key_list = sl.new_list()
    key_set_tree(my_bst["root"], key_list)
    return key_list

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
 
def value_set(my_bst):
    value_list = sl.new_list()
    value_set_tree(my_bst["root"], value_list)
    return value_list

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
