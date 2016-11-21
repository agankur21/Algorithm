import sys
sys.path.append("../ds")
from Tree import *
from DirectedGraph import *


def array_to_bst(sorted_array,start_index,end_index):
    """
    Question 4.2
    :param sorted_array:
    :param start_index:
    :param end_index:
    :return:
    """
    if end_index-start_index <= 0:
        return None
    elif end_index-start_index ==1:
        node = TreeNode(sorted_array[start_index])
        return node
    else:
        middle_element_index = (start_index+end_index)/2
        node = TreeNode(sorted_array[middle_element_index])
        node.left = array_to_bst(sorted_array,start_index,middle_element_index)
        node.right = array_to_bst(sorted_array,middle_element_index+1,end_index)
        return node


def height_tree(node,current_height):
    if node is None or current_height == -1:
        return current_height
    right_height = height_tree(node.right,current_height+1)
    left_height = height_tree(node.left, current_height + 1)
    if left_height == -1 or right_height == -1 or abs(right_height - left_height) > 1 :
        return -1
    else:
        return max(right_height,left_height)


def check_balance_tree(node):
    """
    Q4.4 : Check if the tree is balanced
    :param node:
    :return:
    """
    left_height=height_tree(node.left,0)
    right_height = height_tree(node.right, 0)
    if right_height == -1 or left_height == -1:
        return False
    else:
        return True


def check_value(node,min_value,max_value):
    if node is None:
        return True
    elif node.data > min_value and node.data < max_value:
        return check_value(node.left,min_value,node.data) & check_value(node.right,node.data,max_value)
    else:
        return False


def check_binary_search_tree_(root):
    """
    Q4.5
    :param root:
    :return:
    """
    min_value=-1*sys.maxint
    max_value=sys.maxint
    return check_value(root,min_value,max_value)


def get_min_value(node):
    if node.left is None:
        return node.value
    else:
        return get_min_value(node.left)


def get_successor(node):
    """
    Q4.6
    :param node:
    :return:
    """
    if node.right is not None:
        return get_min_value(node.right)
    else:
        parent=node.parent
        while parent is not None:
            if parent.left == node:
                return parent.value
            else:
                node=parent
                parent = node.parent
        return None



def get_build_order(num_tasks,order_list):
    #Directed graph gives order of precedence.
    #Topological sort is the answer but question is to detect cycle
    #Update graph connections
    directed_graph=DirectedGraph(num_tasks)
    for target,source in order_list:
        directed_graph.connect(source, target)
    #Detect if there is a cycle in the graph
    node_sequence=[]
    for node in directed_graph.nodes:
        node_sequence = node_sequence + directed_graph.get_dfs(node)
    node_sequence.reverse()
    return node_sequence