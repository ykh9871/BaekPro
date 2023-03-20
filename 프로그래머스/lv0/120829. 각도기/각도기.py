def solution(angle):
    if 90>angle>0:
        return 1
    elif 90==angle:
        return 2
    elif 180>angle>90:
        return 3
    else:
        return 4