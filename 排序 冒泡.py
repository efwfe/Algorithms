# _*_coding:utf-8_*_
def bubble_sort(li):
    n = len(li)

    for i in range(n-1):
        flag = False

        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                flag = True

        if flag == False:
            break

if __name__ == '__main__':
    li = [1,3,5,762,1,4,76]
    bubble_sort(li)
    print(li)
    # max o(n2)
    # min o(n)