import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendances = 0

for _ in range(number_of_students):
    number_of_attendances = int(input())
    bonus_for_student = number_of_attendances / number_of_lectures * (5 + additional_bonus)
    if math.ceil(bonus_for_student) > max_bonus:
        max_bonus = math.ceil(bonus_for_student)
        max_attendances = number_of_attendances

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendances} lectures.")
