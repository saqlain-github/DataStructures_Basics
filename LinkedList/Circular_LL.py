class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Circular_LL:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node

    def printCLL(self):
        temp = self.head
        if temp.next is not None:
            while True:
                print(temp.data,"->",end = "")
                temp = temp.next
                if temp == self.head:
                    break

    def delete_item(self,delete_val):
        curr_node = self.head
        prev_node = None
        while curr_node:
            if curr_node.data == delete_val and curr_node == self.head:
                #case1 head is the only element in the list
                if curr_node.next == self.head:
                    curr_node==None
                    self.head == None
                    return

                #case2 there are more elements in c list
                else:
                    #traverse and update head; delete head
                    while curr_node.next != self.head:
                        curr_node = curr_node.next
                    curr_node.next = self.head.next
                    self.head = self.head.next
                    return

            #current is not head
            elif curr_node.data == delete_val:
                prev_node.next = curr_node.next
                curr_node = None
                return

            else:
                if curr_node.next == self.head:
                    print("item not found")
                    break

            prev_node = curr_node
            curr_node = curr_node.next


    def count_CLL(self):
        self.count = 0
        temp = self.head
        if temp.next is not None:
            while True:
                self.count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return self.count


    def to_Circular(self,head):
        start = head
        while head.next is not None:
            head = head.next

        head.next = start
        return


mylist = Circular_LL()

mylist.push(3)
mylist.push(4)
mylist.push(5)
mylist.push(6)

mylist.printCLL()
print()
print(mylist.count_CLL())