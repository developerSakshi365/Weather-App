import requests
import json
import pyttsx3

engine = pyttsx3.init()  # force Windows driver
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

city = input("Enter City: ")

url = f"https://api.weatherapi.com/v1/current.json?key=465d9fbf44d4456ea5262129252412&q={city}"

r = requests.get(url)
# print(r.text)
weather_data = json.loads(r.text)
w = weather_data["current"]["temp_c"]

print(f"The current weather in {city} is {w} degrees.")
engine.say(f"The current weather in {city} is {w} degrees.")
engine.runAndWait()



