class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1 = self.helper(l1)[::-1]
        l2 = self.helper(l2)[::-1]
        str_l1 = ''
        str_l2 = ''
        for num in l1:
            str_l1 += str(num)
        for num in l2:
            str_l2 += str(num)
        result_sum = list(str(int(str_l1) + int(str_l2)))[::-1]
        return self.create_linked_list(result_sum)

    def helper(self, head: ListNode):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def create_linked_list(self, arr, index=0):
        if index == len(arr):
            return None
        node = ListNode(arr[index])
        node.next = self.create_linked_list(arr, index + 1)
        return node


l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
a = Solution()
print(a.addTwoNumbers(l1, l2))
print(l1)
