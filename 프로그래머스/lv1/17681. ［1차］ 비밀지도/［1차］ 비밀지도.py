def solution(n, arr1, arr2):
    tmp1 = []
    tmp2 = []
    arr3 = []
    for i in range(n):
        tmp1.append(format(arr1[i], 'b'))
        tmp2.append(format(arr2[i], 'b'))
        tmp1[i] = "0"*(n - len(tmp1[i])) + tmp1[i]
        tmp2[i] = "0"*(n - len(tmp2[i])) + tmp2[i]
    for  i in range(n):
        temp = []
        for j in range(n):
            if tmp1[i][j]=="0" and tmp2[i][j]== "0": 
                temp.append(" ")
            else: 
                temp.append("#")
        arr3.append(temp)
    for i in range(len(arr3)):
        arr3[i] = "".join(arr3[i])
    return arr3