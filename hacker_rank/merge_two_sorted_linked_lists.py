import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    new_head = SinglyLinkedList()
    c1, c2 = head1, head2
    while True:
        if c1 is not None and c2 is not None:
            if c1.data < c2.data:
                new_head.insert_node(c1.data)
                c1 = c1.next
            else:
                new_head.insert_node(c2.data)
                c2 = c2.next
        elif c1 is not None and c2 is None:
            new_head.insert_node(c1.data)
            c1 = c1.next
        else:
            new_head.insert_node(c2.data)
            c2 = c2.next
        if c1 is None and c2 is None:
            break
    return new_head.head



if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list1.insert_node(1)
    list1.insert_node(2)
    list1.insert_node(3)

    list2 = SinglyLinkedList()
    list2.insert_node(3)
    list2.insert_node(4)

    new_head = mergeLists(list1.head, list2.head)

    print(new_head)