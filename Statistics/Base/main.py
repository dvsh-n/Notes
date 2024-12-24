class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_sample_linked_list():
    # Create nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    return node1

# Example usage
head = create_sample_linked_list()

slow = head
fast = head.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

curr = slow.next
prev = slow.next = None

while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

first, second = head, prev
while second:
    tmp1, tmp2 = first.next, second.next
    first.next = second
    second.next = tmp1
    first, second = tmp1, tmp2


for i in range(10):
    print(head.val)
    head = head.next
