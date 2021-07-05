def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

# 원소의 개수와 찾고자하는 target
n, target = map(int, input().split())
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print(None)
else:
    print(result + 1)

