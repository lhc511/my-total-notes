"""search.py 二分查找方法训练"""


# list01=[0,1,2,3,4,5,6,7,8,9]
# list 为有序数列，key为要查找的关健值，返回key在数列中的索引号
def search(list_, key):
    # 第一个数index最后一个数index
    low, high = 0, len(list_)-1
    while low < high:
        mid = (low + high) // 2
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Key index:", search(l, 8))
