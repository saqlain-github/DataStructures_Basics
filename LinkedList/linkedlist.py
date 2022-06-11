class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertat(self,prev_node, new_value):
        if prev_node is Node:
            print("Previous node is empty")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_value):
        new_node = Node(new_value)
        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printlist(self):
        if self.head ==None:
            print("Empty list")
            return
        tmp = self.head
        while tmp:
            print(tmp.data,"->",end=" ")
            tmp  = tmp.next


    def deletenode(self,key):
        temp = self.head
        #case1
        if temp is not None:
            if temp.data == key:
                self .head = temp.next
                temp = None
                return
        #case2
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #case3
        if temp == None:
            print("No key")
            return

        prev.next = temp.next
        temp = None


    def deleteall(self):
        curr = self.head
        while curr:
            prev = curr.next

            del curr.data
            curr = prev

    def getnodecnt(self,node):
        if not node:
            return 0
        return 1 + self.getnodecnt(node.next)

    def getcount(self):
        return self.getnodecnt(self.head)

    def reversellist(self):
        prev = None
        nex = None
        curr = self.head
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        self.head = prev

if __name__=='__main__':
    llist = Linkedlist()
    llist.append(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.printlist()
    #llist.deletenode(4)
    #llist.getcount()
    #llist.deleteall()
    llist.reversellist()
    print()
    llist.printlist()
    print()


