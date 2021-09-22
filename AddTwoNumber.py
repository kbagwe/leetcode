# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


            head = temp =None
            carry = 0

            while l1 is not None or l2 is not None:
                print(carry)
                sum_value = carry
                print(sum_value)

                if l1 is not None:
                    print(l1.val)
                    sum_value += l1.val
                    print(sum_value)
                    l1 = l1.next
                    print(l1.next)
                if l2 is not None:
                    print(l2.val)
                    sum_value += l2.val
                    print(sum_value)
                    l2 = l2.next
                    print(l2.next)

                node = ListNode(sum_value % 10)
                print(node)

                carry = sum_value // 10
                print(carry)

                if temp is None:
                    temp = head = node
                # for any other node
                else:
                    temp.next = node
                    temp = temp.next

            if carry > 0:
                temp.next = ListNode(carry)
            return head