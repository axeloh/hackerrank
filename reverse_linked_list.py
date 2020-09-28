
"""
Dailyproblem from dailyinterviewpro.com

Given a singly-linked list, reverse the list.
Do it both iteratively and recursively.

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " -> "
            node = node.next
        output += "NULL"
        print(output)

    def addNext(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def reverse_list(self):
        # Reversing the list, starting from this node
        prev = None
        current = self
        while current != None:
            next = current.get_next()
            current.next = prev
            prev = current
            current = next

        return prev  # Returns the new head


def createLinkedList(n):
    # Create linked list of n elements
    head = ListNode(0)
    prev = head
    for i in range(1, n):
        node = ListNode(i)
        if prev != None:
            prev.addNext(node)
        prev = node

    return head


if __name__ == '__main__':
    head = createLinkedList(7) # head of linked list

    head.printList()  # Original order
    new_head = head.reverse_list()  # Reverse list order

    # Last is now head node
    new_head.printList()  # Reversed order




