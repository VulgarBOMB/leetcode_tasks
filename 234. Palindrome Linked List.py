class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode):
        list_to_arr = self.helper(head)
        if 0 == len(list_to_arr) % 2:
            left = list_to_arr[:len(list_to_arr) // 2]
            right = list_to_arr[len(list_to_arr) // 2:][::-1]
            return True if left == right else False
        else:
            print(1)
            mid_index = len(list_to_arr) // 2
            left = list_to_arr[:mid_index]
            right = list_to_arr[mid_index + 1:][::-1]
            return True if left == right else False

    def helper(self, head: ListNode):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


linked_list = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))

a = Solution()
print(a.isPalindrome(linked_list))
