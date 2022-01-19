# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        
        current = head
        while current != None:
            visited.add(current)
            current = current.next
            if current in visited:
                return current
        return None
