a, op, b = input().split()
while op != "?":
    a = int(a)
    b = int(b)
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    else:
        print(a//b)
    a, op, b = input().split()
