# _*_coding:utf-8_*_

def merge_sort(li):
    if len(li) ==1:
        return li

    # 分表
    mid_index = len(li)//2
    left = li[:mid_index]
    right = li[mid_index:]

    l_res = merge_sort(left)
    r_res = merge_sort(right)

    res = merge(l_res,r_res)
    return res

def merge(left, right):
    left_index = 0
    right_index = 0
    res = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            res.append(left[left_index])
            left_index +=1
        else:
            res.append(right[right_index])
            right_index += 1
    res = res + right[right_index:]
    res = res + left[left_index:]
    return  res

if __name__ == '__main__':
    l = [2,4,56,7,2,2,1,1]
    print(merge_sort(l))

    # O(nlogn)