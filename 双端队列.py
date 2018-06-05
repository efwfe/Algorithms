# _*_coding:utf-8_*_
class Deque:
    def __init__(self):
        self.data = []

        # 头加入元素
    def add_front(self, item):
        self.data.insert(0,item)
        # 尾加入元素
    def add_rear(self,item):
        self.data.append(item)
        # 头删除
    def remove_front(self):
        return self.data.pop(0)
        # 尾删
    def remove_rear(self):
        return self.data.pop()

    def is_empty(self):
        return self.data ==[]

    def size(self):
        return len(self.data)


if __name__ == '__main__':
    pass



