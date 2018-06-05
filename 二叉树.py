# _*_coding:utf-8_*_
class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.__root = None

    def add(self, item):
        node = Node(item)

        if self.__root is None:
            self.__root = node
            return
        queue = []
        queue.append(self.__root)

        # 取出节点判断两端
        while queue:
            child = queue.pop(0)
            if child.lchild is None:
                child.lchild = node
                return
            if child.rchild is None:
                child.rchild  = node
                return
            queue.append(child.lchild)
            queue.append(child.rchild)

    def breath_travel(self):
        if self.__root is None:
            return
        queue = []
        queue.append(self.__root)
        while queue:
            node = queue.pop()
            print(node.item)

            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)

    def post_order(self,node):
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.item, end=" ")

    def depth_travel(self):
        self.post_order(self.__root)
        print()

    def pre_order(self,node):
        if node is None:
            return
        print(node.item, end='')
        self.pre_order(node.lchild)
        self.post_order(node.rchild)

    def in_order(self,node):
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.item,end=" ")
        self.in_order(node.rchild)

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    # tree.breath_travel()
    tree.depth_travel()