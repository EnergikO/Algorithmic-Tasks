# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = ''
        number_2 = ''

        while l1:
            number_1 += str(l1.val)
            l1 = l1.next

        while l2:
            number_2 += str(l2.val)
            l2 = l2.next

        number_1 = number_1[::-1]
        number_2 = number_2[::-1]

        summa = str(int(number_1) + int(number_2))

        answer = ListNode(int(summa[0]))
        next = ListNode(int(summa[0]))

        for i in range(1, len(summa)):
            answer = ListNode(int(summa[i]), next)
            next = answer

        return answer
