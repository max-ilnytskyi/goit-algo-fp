class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The given previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            current = head_ref
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

    def merge_sorted(self, other_list):
        dummy_node = Node()
        tail = dummy_node
        a, b = self.head, other_list.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy_node.next


list1 = LinkedList()
list1.insert_at_beginning(1)
list1.insert_at_beginning(5)
list1.insert_at_beginning(10)

print("Original Linked List:")
list1.print_list()

list1.reverse()
print("\nReversed Linked List:")
list1.print_list()

list1.insertion_sort()
print("\nSorted Linked List:")
list1.print_list()

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(3)
list2.insert_at_end(13)
list2.insertion_sort()

list1.merge_sorted(list2)
print("\nMerged Sorted Linked List:")
list1.print_list()
