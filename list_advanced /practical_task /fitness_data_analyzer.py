# Here is function for calculations.
def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    BMI = weight / height ** 2
    return BMI

def calculate_calories_burned(duration, weight):
    """Calculate the estimated number of calories burned during exercise."""
    colories_per_minute = 0.035 * weight
    burned_colories = colories_per_minute * duration
    return burned_colories

def filter_overweight_people(people_data):
    """Filter overweight people based on BMI."""
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people


people_data = []

print("Enter fitness data for each person (Enter a blank name to finish):")

# Start getting information for person.
while True:
    name = input("\nEnter person's name: ").strip()
    if not name:
        break

    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)

# Here is main Fitness Analysis.
print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'], person['weight'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned:.2f}")

# Here check which person is with overweight.
overweight_people = filter_overweight_people(people_data)
print("\nOverweight People:")
for person in overweight_people:
    bmi = calculate_bmi(person['weight'], person['height'])
    print(f"{person['name']}: BMI = {bmi:.2f}")
