# _*_coding:utf-8_*_

# 单链表
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None


class LinkList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count


    def add(self,item):
        """头部添加节点"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.item)
            cur = cur.next

    def append(self,item):
        cur = self.__head
        node = Node(item)
        if cur is None:
            self.add(item)
            return
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert(self,pos,item):
        cur = self.__head
        node = Node(item)
        index = 1
        while cur.next:
            index+=1
            if index ==pos:
                node.next = cur.next
                cur.next = node


if __name__ == '__main__':
    linklist = LinkList()
    linklist.add(2)
    linklist.add(22)
    linklist.add(1)
    # print(linklist.is_empty())
    # linklist.travel()
    # print(linklist.length())
    linklist.append(1)
    linklist.append(222)
    linklist.insert(2,9)
    linklist.append(333)
    linklist.travel()


