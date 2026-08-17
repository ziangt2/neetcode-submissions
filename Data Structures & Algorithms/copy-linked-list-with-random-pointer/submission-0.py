"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        dicts = {None : None}
        while cur:
            copy = Node(cur.val)
            dicts[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = dicts[cur]
            copy.next = dicts[cur.next]
            copy.random = dicts[cur.random]
            cur = cur.next
        return dicts[head]