def solution(n, lost, reserve):
    only_reserve = list(set(reserve) - set(lost))
    only_lost = list(set(lost) - set(reserve))
    only_reserve.sort();
    
    for reserve in only_reserve:
        front = reserve - 1
        back = reserve + 1
        if front in only_lost:
            only_lost.remove(front)
        elif back in only_lost:
            only_lost.remove(back)

    return n - len(only_lost)