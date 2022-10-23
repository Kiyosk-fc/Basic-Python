n, x = map(int, input().split())
while n != 0 or x != 0:
    pattern = 0
    for k in range(1, n+1):
        for j in range(1, k):
            for i in range(1, j):
                if i + j + k == x:
                    pattern += 1
    print(pattern)
    n, x = map(int, input().split())
