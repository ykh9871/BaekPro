def solution(arr, divisor):
    arr = [i for i in arr if i % divisor == 0]
    arr.sort()
    if len(arr) != 0:
        return arr 
    else:
        return [-1]