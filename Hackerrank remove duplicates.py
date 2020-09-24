def removeDuplicates(self,head):
        cur = head
        while cur.next:
            if cur.data != cur.next.data:
                cur = cur.next
            else:
                temp = cur
                while cur.next is not None and cur.data == cur.next.data:
                    cur = cur.next
                temp.next = cur.next
        return head