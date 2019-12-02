"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        first = head
        second = head

        n = 1

        while first.next:
            first = first.next
            n +=1
        first.next = head

        for i in range(k-n%n-1):
            second = second.next
        res = second.next
        second.next = None
        return  res


        # for i in range(k):
        #     if second.next is None:
        #         second = head
        #     else:
        #         second = second.next
        # while second.next is not None:
        #     second = second.next
        #     first = first.next
        # tmp = first.next
        # first.next = None
        # res = tmp
        # while tmp.next:
        #     tmp = tmp.next
        # tmp.next = head
        # return  res

