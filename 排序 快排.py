# _*_coding:utf-8_*_
def quick_sort(li, start, end):
    if start >=end:
        return

    left = start
    right = end

    mid = li[left]

    while left < right:
        while left < right and li[right] >= mid:
            right -=1
        li[left] = li[right]

        while left < right and li[left] < mid:
            left +=1
        li[right] = li[left]
    li[left] = mid
    quick_sort(li, start, left-1)
    quick_sort(li,left+1, end)

if __name__ == '__main__':

    l = [2,54,6,782,2]
    quick_sort(l,0,len(l)-1)
    print(l)
    # 时间复杂度o(nlogn)、o(n2)