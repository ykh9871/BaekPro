import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
answer_time  = sys.maxsize
answer_height = 0

for height in range(257):
    blocks_above_target , blocks_below_target = 0, 0

    for i in range(N):
        for j in range(M):

            if ground[i][j] > height :
                blocks_above_target += ground[i][j] - height
            else : 
                blocks_below_target += height - ground[i][j]

    if blocks_above_target + B >= blocks_below_target :
        if (blocks_above_target * 2) + blocks_below_target <= answer_time:
            answer_time = (blocks_above_target * 2) + blocks_below_target
            answer_height = height


print(answer_time, answer_height)