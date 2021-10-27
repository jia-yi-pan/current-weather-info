# ZIP CODE DATABASE CSV OBTAINED FROM https://www.unitedstateszipcodes.org/zip-code-database/

from tkinter import *
from tkinter import messagebox
import pandas
import requests

FONT = ("Courier", 35)

WEATHER_API = "YOUR API KEY"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def zip_validation(zip_to_check):
    int_zip_to_check = int(zip_to_check)
    zip_data = pandas.read_csv("zip_code_database.csv")
    valid_zip_list = [zip_code for zip_code in zip_data["zip"]]
    if int_zip_to_check in valid_zip_list:
        return zip_to_check


def find_weather_info():
    zip_code = location_entry.get()
    if len(zip_code) == 0:
        messagebox.showinfo(title="Missing Field", message="Please enter a zip code!")
    elif not zip_validation(zip_code):
        messagebox.showinfo(title="Unknown Entry", message="Please enter a valid zip code!")
    else:
        query = {
            "zip": f"{zip_code},us",
            "appid": WEATHER_API,
            "units": "imperial"
        }
        response = requests.get(url=WEATHER_URL, params=query).json()
        weather_condition = response["weather"][0]["description"]
        current_temp = response["main"]["temp"]
        messagebox.showinfo(title="Weather Information", message=f"The weather includes {weather_condition}. It is currently {current_temp} degrees Fahrenheit.")


window = Tk()

window.title("What's the Weather?")
window.config(padx=60, pady=60, bg="white")

canvas = Canvas(width=500, height=500, bg="white", highlightthickness=0)
canvas.grid(row=0, column=0)
weather_jpg = PhotoImage(file="weather.png")

canvas.create_image(40, 50, anchor=NW, image=weather_jpg)

location_label = Label(text="Enter Zip Code:", bg="white", font=FONT)
location_label.grid(row=1, column=0)

location_entry = Entry()
location_entry.grid(row=2, column=0)

submit_button = Button(text="Check Weather", command=find_weather_info)
submit_button.grid(row=3, column=0)

window.mainloop()
