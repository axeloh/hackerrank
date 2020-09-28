"""

Given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes
contain a single digit.
Add the two number and return it as a linked list.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807

"""

# Definition for singly-linked list

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

class Solution:
    def getNumber(self, l1):
        node = l1
        number_str = ""
        while node is not None:
            number_str = str(node.val) + number_str
            node = node.next

        return int(number_str)


    def addTwoNumbers(self, l1, l2, c = 0):
        l1_num = self.getNumber(l1)
        l2_num = self.getNumber(l2)
        total = l1_num + l2_num

        total_str = str(total)
        print(total_str)
        i = len(total_str) - 1
        head = ListNode(int(total_str[i]))
        node = head
        while i > 0:
            i -= 1
            next_ = ListNode(int(total_str[i]))
            node.next = next_
            node = next_

        return head




if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(3)
    l1.printList()

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l2.printList()


    result = Solution().addTwoNumbers(l1, l2)
    print('--- RESULT ---')
    result.printList()




