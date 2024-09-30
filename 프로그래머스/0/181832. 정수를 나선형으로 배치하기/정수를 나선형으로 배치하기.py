def solution(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    # 나선형이므로 시계 방향 순서대로 (오른쪽, 아래, 왼쪽, 위쪽)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0  # 현재 방향을 가리키는 인덱스 (처음엔 오른쪽)

    x, y = 0, 0  # 시작 좌표

    for num in range(1, n * n + 1):
        matrix[x][y] = num
        # 다음 좌표 계산
        dx, dy = directions[dir_index]
        nx, ny = x + dx, y + dy

        # 경계를 넘어가거나 이미 채워진 곳이면 방향을 바꿈
        if not (0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0):
            dir_index = (dir_index + 1) % 4  # 시계 방향으로 변경
            dx, dy = directions[dir_index]
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    return matrix
