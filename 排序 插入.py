# _*_coding:utf-8_*_


def insert(li):
    n = len(li)

    for j in range(1,n):
        for i in range(j,0,-1):
            if li[i] < li[i-1]:
                li[i], li[i-1] = li[i-1], li[i]
            else:
                break

if __name__ == '__main__':
    l = [1,2,54,6,2,3]
    insert(l)
    print(l)