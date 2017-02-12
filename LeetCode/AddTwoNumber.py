# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getNodeValue(self, node):
        if node is None:
            return 0
        else:
            return node.val

    def getNextNode(self, node):
        if node is None:
            return None
        else:
            return node.next

    def addTwoNodes(self, l1, l2, carryBalance, out):
        total = self.getNodeValue(l1) + self.getNodeValue(l2) + carryBalance
        out.val = total % 10
        return total / 10

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        outListHead = None
        currentPointer = None
        carryBalance = 0
        while (l1 is not None) or (l2 is not None) or (carryBalance > 0):
            # add new node in out
            newListNode = ListNode(0)
            if outListHead is None:
                outListHead = newListNode
                currentPointer = outListHead
            else:
                currentPointer.next = newListNode
                currentPointer = newListNode
            # Add list nodes
            carryBalance = self.addTwoNodes(l1, l2, carryBalance, currentPointer)
            l1 = self.getNextNode(l1)
            l2 = self.getNextNode(l2)
        return outListHead