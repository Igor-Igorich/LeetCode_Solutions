
from typing import Optional, Self

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates(
            self: Self,
            head: Optional[ListNode]
            ) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        prev = head
        cur = head.next
        while cur != None:
            if cur.val == prev.val:
                prev.next = cur.next
                del(cur)
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head
    
    def delete_duplicates_optimized(
            self: Self,
            head: Optional[ListNode]
            ) -> Optional[ListNode]:
        
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next # удаляем ссылку, Python сам соберет мусор
            else:
                cur = cur.next
        
        return head