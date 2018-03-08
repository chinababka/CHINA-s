def BinarySearch(lst, l, r, x):
    while l <= r:
        mid = int(l + (r - l) / 2)
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            l = mid + 1
        elif lst[mid] > x:
            r = mid - 1
    return "Error 404"


m = [2, 3, 4, 10, 40]
x = 10
result = BinarySearch(m, 0, len(m) - 1, x)
print(result)
print(m.index(10))
