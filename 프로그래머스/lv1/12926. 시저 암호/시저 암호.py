def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in small:
            index = small.find(char)+n
            answer += small[index%26]
        elif char in big:
            index = big.find(char)+n
            answer += big[index%26]
        else:
            answer += " "
    return answer
