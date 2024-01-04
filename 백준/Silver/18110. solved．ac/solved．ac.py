import sys
input = sys.stdin.readline

def myround(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(input())
if n == 0:
    print(0)
else:
    difficulty = [int(input()) for _ in range(n)]
    trimmedmean = myround(n * 0.15)
    trimmed_opinions = sorted(difficulty)[trimmedmean:n-trimmedmean]
    avg_difficulty = myround(sum(trimmed_opinions) / len(trimmed_opinions))
    print(avg_difficulty)