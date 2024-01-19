year = int(input())

while True:
    year += 1
    string = str(year)
    if len(string) == len(set(string)):
        break
print(year)
    
