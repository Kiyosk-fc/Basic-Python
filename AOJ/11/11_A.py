top, back, right, left, front, bottom = map(int, input().split())
directions = input()
for v in directions:
    if v == "E":
        top, back, right, left, front, bottom = right, back, bottom, top, front, left
    elif v == "N":
        top, back, right, left, front, bottom = front, top, right, left, bottom, back
    elif v == "S":
        top, back, right, left, front, bottom = back, bottom, right, left, top, front
    elif v == "W":
        top, back, right, left, front, bottom = left, back, top, bottom, front, right
print(top)
