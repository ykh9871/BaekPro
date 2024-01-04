N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

min_repaints = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        repaint_count_w = 0
        repaint_count_b = 0

        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0 and board[i + x][j + y] == 'B':
                    repaint_count_w += 1
                elif (x + y) % 2 == 1 and board[i + x][j + y] == 'W':
                    repaint_count_w += 1

        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0 and board[i + x][j + y] == 'W':
                    repaint_count_b += 1
                elif (x + y) % 2 == 1 and board[i + x][j + y] == 'B':
                    repaint_count_b += 1

        min_repaints = min(min_repaints, repaint_count_w, repaint_count_b)

print(min_repaints)