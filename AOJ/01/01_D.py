s = int(input())
h = s//(60*60)
s -= h*60*60
m = s//60
s -= m*60
print(str(h)+":"+str(m)+":"+str(s))
