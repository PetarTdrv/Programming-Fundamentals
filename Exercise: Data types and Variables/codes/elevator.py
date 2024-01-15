persons = int(input())
capacity = int(input())
 
if persons <= capacity:
    print(1)
else:
    first_course = persons // capacity
    if persons % capacity != 0:
        first_course += 1
    print(first_course)
