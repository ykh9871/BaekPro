def solution(num_list):
    odd = 0
    even = 0
    for n in range(len(num_list)):
        if n%2 != 0:
            odd += num_list[n]
        else:
            even += num_list[n]
    if odd == even:
        return odd
    elif odd > even:
        return odd
    else:
        return even