first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
number_of_students = int(input())

all_students_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
hour_counter = 0

while number_of_students > 0:
    hour_counter += 1

    if hour_counter % 4 == 0:
        continue
    else:
        number_of_students -= all_students_per_hour

print(f"Time needed: {hour_counter}h.")
