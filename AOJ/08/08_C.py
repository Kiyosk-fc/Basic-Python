counter = [0 for i in range(ord("z")-ord("a")+1)]
while True:
    try:
        documents = input().lower()
        for j in documents:
            if ord("a") <= ord(j) <= ord("z"):
                counter[ord(j) - ord("a")] += 1
    except EOFError:
        break
for k in range(len(counter)):
    print(chr(k+ord("a")), ":", counter[k])
