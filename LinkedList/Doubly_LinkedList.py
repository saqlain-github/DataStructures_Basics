import gc
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LL:
    def __init__(self):
        self.head = None

    def push(self,new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self,prev_node, new_data):

        if prev_node is None:
            print("Prev cannot be none")

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insert_last(self,new_value):
        new_node = Node(new_value)
        new_node.next = None
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            return

    def count_DLL(self,head):
        '''
        temp = self.head
        self.count = 0
        while temp.next is not None:
            self.count += 1
            temp = temp.next
        return self.count
           '''
        while head is not None:
            print(head.data,"->",end = "")
            head = head.next

    def delete_DLL(self,key):

        if self.head is None or key is None:
            return
        #case 1 delete head
        if self.head == key:
            self.head == key.next

        #case2 not last node, in between
        if key.next is not None:
            key.next.prev = key.prev

        #case3 last in between
        if key.prev is not None:
            key.prev.next = key.next

        # there can we more cases also

        gc.collect()