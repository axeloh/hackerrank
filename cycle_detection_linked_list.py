#!/bin/python3

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

    def print_singly_linked_list(self, sep):
        seen = set([])
        node = self.head
        while node:
            print(str(node.data))

            node = node.next
            if node.data in seen:
                break
            seen.add(node.data)

            if node:
                print(sep)
            if node.data in seen:
                break


"""
Own constraints: 
1) Time complexity < O(n^2)
2) Space complexity must be O(1)
3) LinkedList should not be modified

Possible solutions:
1) Sort&Scan. Time: O(nlogn), Space: O(1). 
Not applicable for linkedlist

2) Use a set and count occurences. Time: O(n), Space: O(n), 
Does not modify anything. 
Constraint 2 violated

3) Floyd's method. Time: < O(n^2), Space: O(1). 
Does not modify anything. Works!
"""


def has_cycle(head):
    # Using Floyd's Tortoise and Hare algorithm
    # Time
    # Time: if cycle: O(λ + μ), λ: loop length, μ: length until        loop
    # if no cycle: O(n)
    # Space: O(1), only uses two pointers and a couple of variables

    turtle = head
    hare = head
    M = 0
    while True:
        if hare is None or turtle is None:
            print('No cycle.')
            return False  # Reached end without meeting
        if turtle.next is None:
            print('No cycle.')
            return False
        if hare.next is None:
            print('No cycle.')
            return False
        if hare.next.next is None:
            print('No cycle.')
            return False

        turtle = turtle.next
        hare = hare.next.next
        M += 1
        if turtle == hare:
            break

    print('There exists a cycle!')
    """
    Turtle and hare has met and are now at same node
    Algorithm says that if one start at beginning,
    and one continues from meeting point, they will meet at the point where the cycle starts.
    Here we only care if there exists a cycle, so we only need to return true here.
    """
    turtle = head
    z = 0  # count to count length of cycle
    while turtle != hare:
        turtle = turtle.next
        hare = hare.next
        z += 1


    # Hare and turtle are now at node beginning cycle
    print(f'Cycle has length: {M}')
    print(f'Cycle starts on the node before the node with value {turtle.data}')

    return True


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #tests = int(input())
    index = int(input('Index: '))
    llist_count = int(input('Number of nodes: '))

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input('Node value (unique): '))
        llist.insert_node(llist_item)

    extra = SinglyLinkedListNode(-1);
    temp = llist.head;

    for i in range(llist_count):
        if i == index:
            extra = temp

        if i != llist_count - 1:
            temp = temp.next

    temp.next = extra
    llist.print_singly_linked_list(sep='->')
    has = has_cycle(llist.head)
    print(has)
