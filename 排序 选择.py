# _*_coding:utf-8_*_

def select(li):
    n = len(li)
    # 把最小的选出来
    # 记录0位置，把0位置设为最小数
    # 让最小的数和后面的比较

    for j in range(n-1):
        min_index =j

        for i in range(1+j,n):
            if li[i] < li[min_index]:
                min_index = i
        li[min_index], li[j] = li[j],li[min_index]

if __name__ == '__main__':

    l = [1,23,4,5,2,3]
    select(l)
    print(l)