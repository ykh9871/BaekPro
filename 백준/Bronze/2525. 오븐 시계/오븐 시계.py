A, B =  map(int, input().split())
C = int(input())
B = B+C
if B > 59:
    A = A+(B//60)
    B = B%60
    if A>23:
        A= A-24
        print(A,B)
    else:
        print(A,B)
else:
    print(A,B)