# _*_coding:utf-8_*_
class Queue:
    def __init__(self):
        self.data = []

        # 入列
    def enqueue(self, item):
        self.data.append(item)

        # 出列
    def dequeue(self):
        return self.data.pop(0)

        # 是否为空
    def is_empty(self):
        return self.data ==[]

        # 大小
    def size(self):
        return len(self.data)

if __name__ == '__main__':

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
