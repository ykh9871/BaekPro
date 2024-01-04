k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

left, right = 1, max(cables)
result = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(cable // mid for cable in cables)

    if count >= n:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)