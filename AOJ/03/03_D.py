a, b, c = map(int, input().split())
x = 1
i = 0
while c >= x:
    if c % x == 0 and a <= x <= b:
        i += 1
    x += 1
print(i)
