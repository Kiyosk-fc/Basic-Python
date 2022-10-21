n = int(input())
all = [i for i in range(1, 53)]
for j in range(n):
    mark, number = input().split()
    number = int(number)
    if mark == "S":
        number += 0
    elif mark == "H":
        number += 13
    elif mark == "C":
        number += 26
    else:
        number += 39
    all.remove(number)
for k in range(52-n):
    if 1 <= all[k] <= 13:
        print("S", all[k])
    elif 14 <= all[k] <= 26:
        print("H", all[k]-13)
    elif 27 <= all[k] <= 39:
        number -= 26
        print("C", all[k]-26)
    else:
        number -= 39
        print("D", all[k]-39)
