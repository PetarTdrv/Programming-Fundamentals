number_of_balls = int(input())

max_weight = 0
max_time = 0
best_quality = 0
max_value = 0

for i in range(number_of_balls):
    weight = int(input())
    needed_time = int(input())
    quality_of_ball = int(input())
    
    value = (weight / needed_time) ** quality_of_ball
    if value > max_value:
        max_weight = weight
        max_time = needed_time
        best_quality = quality_of_ball
        max_value = value
        
print(f"{max_weight} : {max_time} = {int(max_value)} ({best_quality})")
