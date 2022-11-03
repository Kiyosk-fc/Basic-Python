n = int(input())
dices = []
for i in range(n):
    dices.append(list(map(int, input().split())))
for a in range(n):
    top = dices[a][0]
    back = dices[a][1]
    right = dices[a][2]
    left = dices[a][3]
    front = dices[a][4]
    bottom = dices[a][5]
    for b in range(n):
        for c in range(4):
            top, back, right, left, front, bottom = right, back, bottom, top, front, left
            for d in range(4):
                top, back, right, left, front, bottom = top, left, back, front, right, bottom
                if a != b and (top == dices[b][0] and back == dices[b][1] and right == dices[b][2] and
                   left == dices[b][3] and front == dices[b][4] and bottom == dices[b][5]):
                    print("No")
                    exit()
print("Yes")
