# _*_coding:utf-8_*_
# 给一个数组，
# 找出里面最大的2个，并且回答出算法的时间复杂度。可以用任何语言。
#  例子：输入数组[1,2,5,6,3,4,5,4],输出6，5

li = [1,2,5,6,3,4,5,4]
a = [0]*2

for i in set(li):
    if i> min(a):
        a[a.index(min(a))]=i

print(a)

# 时间复杂度O(m*n)