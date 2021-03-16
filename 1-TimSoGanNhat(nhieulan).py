import sys
input = sys.stdin.readline

def InnovateBinarySearch(l, k, x):
    left = 0
    right = len(l) - k
    while left < right:
        mid = (left + right) // 2
        if (x - l[mid]) > (l[mid + k] - x):
            left = mid + 1
        else:
            right = mid
    return l[left : left + k]

n = int(input())
l = list(map(int, input().split()))
while True:
    kx = list(map(int, input().split()))
    if (len(kx) == 0):
        break
    if (len(kx) <= n):
        l2 = InnovateBinarySearch(l, kx[0], kx[1])
        print(l2[0], l2[len(l2) - 1]) 
    else:
        break