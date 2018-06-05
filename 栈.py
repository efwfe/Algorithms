# _*_coding:utf-8_*_
class Stack:
    def __init__(self):
        self.data = []

        # 添加元素
    def push(self, item):
        self.data.append(item)

        # 顶出元素
    def pop(self):
        return self.data.pop()

        # 返回栈顶元素
    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return self.data ==[]

    def size(self):
        return len(self.data)


if __name__ == '__main__':

    stack = Stack()
    stack.is_empty()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())

    print(stack.size())
    print(stack.peek())

