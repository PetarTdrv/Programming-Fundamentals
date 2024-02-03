start_values = input().split()
arraray = [int(num) for num in start_values]


while True:

    command = input().split()

    if command[0] == "end":
       break

    if command[0] == "swap":
       swap1 = int(command[1])
       swap2 = int(command[2])
       arraray[swap1], arraray[swap2] = arraray[swap2], arraray[swap1]

    elif command[0] == "multiply":
       indx1 = int(command[1])
       indx2 = int(command[2])
       arraray[indx1] *= arraray[indx2]

    elif command[0] == "decrease":
        arraray = [(int(num) - 1) for num in arraray]
           
arraray = [str(i) for i in arraray]          
print(', '.join(arraray))
