W, H, x, y, r = map(int, input().split())
if r <= x < x + r <= W and r <= y < y + r <= H:
    print("Yes")
else:
    print("No")
