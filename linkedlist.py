class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def rpush(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def lpush(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def insertafter(self, prev_node, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.data != prev_node.data and temp is not None:
                temp = temp.next
            if temp is None:
                print("not found")
            temp_left = temp.next
            temp.next = Node(data)
            temp.next.next = temp_left

    def pop(self, node):
        if self.head is None:
            print("nothing to pop")
            return
        if node is None:
            print("given node must be in LK to pop")
            return
        if self.head.data == node.data:
            temp = self.head
            self.head = temp.next
            return

        temp = self.head
        while temp.next.data != node.data and temp.next is not None:
            temp = temp.next

        b_temp = temp.next.next
        temp.next = b_temp





    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    _head = LinkedList()
    _head.head = Node(1)

    second = Node(2)
    third = Node(3)

    _head.head.next = second
    second.next = third
    _head.printlist()
    print("###")
    _head.rpush(5)
    _head.printlist()
    print("####")
    _head.lpush(99)
    _head.printlist()

    node99 = Node(5)
    print("$$$$$")
    _head.pop(node99)
    _head.printlist()

