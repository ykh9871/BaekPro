def solution(array, height):
    person = 0
    for i in array:
        if i > height:
            person += 1
    return person