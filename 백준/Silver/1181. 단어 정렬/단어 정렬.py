n = int(input())
words = [input() for i in range(n)]
set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key = len)
for i in words:
    print(i)