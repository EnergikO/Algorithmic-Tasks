# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: None}}}


def deleteDuplicates(head):
	if not head:
		return None

	temp_answer = [head.val]
	answer: ListNode

	while head.next is not None:
		head = head.next

		if head.val != temp_answer[-1]:
			temp_answer.append(head.val)

	answer = ListNode(temp_answer[-1], None)
	temp_answer.pop()

	while temp_answer:
		answer = ListNode(temp_answer[-1], answer)
		temp_answer.pop()

	return answer


print(deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, None)))))
