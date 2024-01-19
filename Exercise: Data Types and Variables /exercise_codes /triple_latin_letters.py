num = int(input())

for i in range(0, num):
    for k in range(0, num):
        for g in range(0, num):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + g)}")
