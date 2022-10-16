a, op, b = input().split()
while op != "?":
    a = int(a)
    b = int(b)
    if op == "+":
        print(a+b)
    if op == "-":
        print(a-b)
    if op == "*":
        print(a*b)
    if op == "/":
        print(a//b)
    a, op, b = input().split()
