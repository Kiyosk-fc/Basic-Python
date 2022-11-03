x_top, x_back, x_right, x_left, x_front, x_bottom = map(int, input().split())
y_top, y_back, y_right, y_left, y_front, y_bottom = map(int, input().split())
for i in range(4):
    x_top, x_back, x_right, x_left, x_front, x_bottom = x_right, x_back, x_bottom, x_top, x_front, x_left
    for j in range(4):
        x_top, x_back, x_right, x_left, x_front, x_bottom = x_top, x_left, x_back, x_front, x_right, x_bottom
        if x_top == y_top and x_back == y_back and x_right == y_right and x_left == y_left and x_front == y_front and x_bottom == y_bottom:
            print("Yes")
            exit()
print("No")
