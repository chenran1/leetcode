'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''

#Definition for singly-linked list.
class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:

    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        '''
        利用while break实现do while的效果
        利用大数相加进位的思想实现基本算法
        :param l2:
        :return:
        '''
        jinwei = 0
        ll = ListNode(0)
        l = ListNode(0)
        i = 0
        while True:
            value = (l1.val + l2.val) % 10 +jinwei
            jinwei = (l1.val + l2.val)//10
            if i == 0:
                l = ListNode(value)
                ll = l
            else:
                ll.next = ListNode(value)
                ll = ll.next
            i +=1

            if l1.next == None and l2.next == None:
                break
            l1 = l1.next
            l2 = l2.next

        return l

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l = Solution.addTwoNumbers(l1,l2)
while l:
    print(l.val)
    l = l.next




