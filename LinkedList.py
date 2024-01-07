# https://leetcode.com/problems/reverse-linked-list/submissions/1122259984/
# Reverse a Liked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # create a prev and keep it as none for the time being
        curr = head  # curr pointer points to head
        while curr != None:  # traverse until curr is not empty
            nxt = curr.next  # storing temp
            curr.next = prev  # current's pointer will point to prev
            prev = curr  # move prev to current
            curr = nxt  # move curr to curr.next but before doing that, store it in a temp variable
        return prev


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Delete duplicates from a linked list

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head  # pointer curr to head
        while curr != None:  # traverse until curr is not empty
            # check to see if curr.next and curr.next.val is equal to curr.val
            while curr.next and curr.next.val == curr.val:
                # if they are equal, curr.next jumps to curr.next.next, so basially skips the duplicate
                curr.next = curr.next.next
            curr = curr.next  # else jump to the next one
        return head  # return head


# 203. Remove Linked List Elements (delete node when value is given)
# https://leetcode.com/problems/remove-linked-list-elements/description/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node and point its next to the original head
        # here, 0 is the value and head is what it's pointed to
        dummy = ListNode(0, head)

        # Initialize curr pointer to dummy node
        curr = dummy

        # Traverse the linked list
        while curr.next != None:
            # If the next node's value matches the target value
            if curr.next.val == val:
                # Skip the node by pointing curr's next to the node after the next node
                curr.next = curr.next.next
            else:
                # Move curr pointer to the next node
                curr = curr.next

        # Return the updated list starting from the node after the dummy node
        return dummy.next

# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node and link to the head of the node
        dummy = ListNode(0, head)
        left = dummy  # Assign the dummy node to left pointer
        right = head  # Assign the dummy node to right pointer (for now)

        while n > 0 and right != None:  # Loop until n is 0 and right hits the end of the linked list
            # This loop basically moves right to size of n, so gap between left and right pointer will be n
            right = right.next  # move right
            n -= 1  # reduce n

        # Looping through the linked list with the a gap of n between left and right pointer so left pointer will basically reach n-1 node. (so we can delete the next node by doing a next.next)
        while right != None:
            left = left.next
            right = right.next

        # deleting
        # left.next here is basailly n-1, so to delete n, we're doing this
        left.next = left.next.next
        # return the dummy as it'll return the new linkedlist without the n (deleted) no
        return dummy.next


# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  # store the next node value to given node value
        # jump node.next to two points as it'll skip the value since we stored it in the
        node.next = node.next.next

# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # slow pointer at head
        fast = head  # fast pointer at head

        while fast and fast.next != None:  # traverse until fast and fast.next is not none
            slow = slow.next  # move slow to slow.next
            fast = fast.next.next  # fast will basically jump twice, so next.next
            if slow == fast:  # if slow == fast, then there is a cycle
                return True  # return true
        return False  # else false

# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers 'slow' and 'fast' both starting from the head of the list
        slow = head
        fast = head
        slow2 = head  # Another pointer used for finding the start of the cycle

        # Traverse the list using 'fast' and 'slow' pointers
        while fast and fast.next != None:
            slow = slow.next  # Move 'slow' pointer by one node
            fast = fast.next.next  # Move 'fast' pointer by two nodes

            # If 'slow' and 'fast' pointers meet, there is a cycle in the linked list
            if slow == fast:
                # Move 'slow2' pointer from the head and 'slow' pointer from meeting point until they meet
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next

                # Return the node where 'slow2' and 'slow' pointers meet, which is the start of the cycle
                return slow

        # Return None if there is no cycle in the linked list
        return None
