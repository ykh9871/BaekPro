def solution(answers):
    counts = [0 for i in range(3)]

    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        answer = answers[i]
        if(supo1[i%len(supo1)] == answer):
            counts[0] += 1
        if(supo2[i%len(supo2)] == answer):
            counts[1] += 1
        if(supo3[i%len(supo3)] == answer):
            counts[2] += 1     
    
    result = []
    for i in range(len(counts)):
        if(counts[i] == max(counts)):
            result.append(i+1)
    
    return sorted(result)