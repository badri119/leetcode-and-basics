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
        while curr.next != None:  # traverse until curr is not empty
            # check to see if curr.next and curr.next.val is equal to curr.val
            while curr.next and curr.next.val == curr.val:
                # if they are equal, curr.next jumps to curr.next.next, so basially skips the duplicate
                curr.next = curr.next.next
            curr = curr.next  # else jump to the next one
        return head  # return head

# OR


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr != None:
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


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

# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to start the result linked list
        dummy = ListNode()
        curr = dummy  # Create a pointer to the dummy node
        carry = 0     # Used to carry values if sum of nodes' values is greater than 9

        # Loop through both linked lists or until carry is non-zero
        while l1 or l2 or carry:
            # Extract the values of nodes in l1 and l2; if they are None, use 0
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0

            # Calculate the sum of the current nodes' values and the carry
            val = v1 + v2 + carry
            carry = val // 10  # Calculate the carry for the next digit
            val = val % 10      # Calculate the value to be placed in the current node

            # Create a new node with the calculated value
            curr.next = ListNode(val)

            # Move the pointers to the next nodes in l1 and l2 (if they exist)
            curr = curr.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        # Return the next node of the dummy node (start of the result linked list)
        return dummy.next

# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/

# Method 1 using sorting:


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]

# Method2 using Hashset:


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return num
            else:
                duplicate.add(num)

# Method3 using Fast and Slow pointers:


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0  # Initialize slow pointer
        fast = 0  # Initialize fast pointer

        # Loop to find intersection point of slow and fast pointers
        while True:
            slow = nums[slow]  # Move slow pointer one step ahead
            fast = nums[nums[fast]]  # Move fast pointer two steps ahead

            # If slow and fast pointers meet, break the loop
            if slow == fast:
                break

        slow2 = 0  # Initialize another pointer starting from the beginning

        # Loop to find the entry point of the cycle
        while slow != slow2:
            slow = nums[slow]  # Move slow pointer one step ahead
            slow2 = nums[slow2]  # Move another pointer one step ahead

            # If both pointers meet, return the duplicate value
            if slow == slow2:
                return slow

# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # create a dummy node
        slow = dummy  # point slow to dummy
        fast = head  # fast to head

        # find middle value by moving slow by 1 and fast by 2 (The Tortoise and hare algo)
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # Slow will be at middle - 1 because of the dummy node that we initialized, so skip the middle value by slow.next.next
        slow.next = slow.next.next
        return dummy.next  # return the linked list minus the dummy


# 2807. Insert Greatest Common Divisors in Linked List
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head #set previous pointer as head
        curr = head.next #set head.next has curr
        while curr: #continue until curr is none
            gcd = math.gcd(prev.val, curr.val) #calculating gcd with prev.val and curr.val
            gcd_node = ListNode(gcd) #Adding List node with the gcd value
            prev.next = gcd_node #connect prev.next to the new gcd_node
            gcd_node.next = curr #connect gcd_node.next to curr
            prev = curr #+1 for prev
            curr = curr.next #+1 for curr
        return head