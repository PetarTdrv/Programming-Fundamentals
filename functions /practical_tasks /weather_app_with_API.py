import requests

def weather(user_input):
    """
    Get the current temperature in Celsius for a specified city using the OpenWeatherMap API.

    Parameters:
    - user_input (str): The name of the city for which the temperature is requested.

    Returns:
    - float or None: The current temperature in Celsius if successful, None otherwise.
    """
    api_key = '75b6174acbc6149d0d9953d7493819c6'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    town = user_input
    if weather_data.status_code == 200:
        temp = weather_data.json()['main']['temp']
        celsius = (temp - 32) * 5/9
        return celsius
    else:
        print("Error!")
        return None


def display_weather_info(celsius, town):
    if celsius:
        print(f"The temperature in {town} is : {celsius:.2f}°C")


def main():
    user_input = input("Enter City name: ")
    celsius = weather(user_input)
    if celsius:
        cel = display_weather_info(celsius, user_input)
        return cel
          

print(main())
