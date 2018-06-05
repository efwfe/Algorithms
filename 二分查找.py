# _*_coding:utf-8_*_

def search(li,item):
    if len(li) == 0 :
        return False

    mid = len(li)//2
    if li[mid] == item:
        return  True
    elif item > li[mid]:
        return search(li[mid+1:], item)
    else:
        return search(li[:mid], item)

if __name__ == '__main__':
    l = [1,2,4,6,2,1,6]
    print(search(l,2))