import requests
from tkinter import *
from tkinter import messagebox as mb

# Function to fetch and display weather info
def getWeatherInfo():
    city = place.get()
    if not city:
        mb.showwarning("Input Error", "Please enter a location")
        return

    try:
        api_key = "d850f7f52bf19300a9eb4b0aa6b80f0d"
        current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

        current_data = requests.get(current_url).json()
        forecast_data = requests.get(forecast_url).json()

        # Current weather
        main = current_data["main"]
        weather = current_data["weather"][0]
        temp = round(main["temp"] - 273.15, 2)
        pressure = main["pressure"]
        humidity = main["humidity"]
        desc = weather["description"]

        weather_info = f"🌤️ Current Weather in {city.title()}\n\n" \
                       f"Temperature: {temp}°C\n" \
                       f"Pressure: {pressure} hPa\n" \
                       f"Humidity: {humidity}%\n" \
                       f"Description: {desc.capitalize()}\n\n"

        # 3-Day Forecast
        forecast_info = "📅 3-Day Forecast (12:00PM):\n"
        shown_days = set()
        for item in forecast_data["list"]:
            if "12:00:00" in item["dt_txt"]:
                date = item["dt_txt"].split(" ")[0]
                if date not in shown_days:
                    shown_days.add(date)
                    ft = round(item["main"]["temp"] - 273.15, 2)
                    fd = item["weather"][0]["description"].capitalize()
                    forecast_info += f"{date}: {ft}°C, {fd}\n"
                if len(shown_days) == 3:
                    break

        output_label.config(text=weather_info + forecast_info)
    except Exception as e:
        output_label.config(text="")
        mb.showerror("Error", f"Could not retrieve weather data:\n{e}")

# Main UI setup
wn = Tk()
wn.title("Today's Weather")
wn.geometry('600x400')
wn.config(bg='#f0f8ff')

Label(wn, text=" Weatherly - Check Today's Weather", font=('Helvetica', 16, 'bold'), fg='#1a1a1a', bg='#f0f8ff').pack(pady=10)

Label(wn, text="Enter your location:", font=('Helvetica', 12), bg='#f0f8ff').pack()
place = StringVar()
Entry(wn, textvariable=place, width=40, font=('Helvetica', 12)).pack(pady=5)

Button(wn, text="Get Weather Info", command=getWeatherInfo, font=('Helvetica', 11), bg='#add8e6', fg='black').pack(pady=10)

output_label = Label(wn, text="", font=('Helvetica', 12), bg='#f0f8ff', justify=LEFT, anchor='w')
output_label.pack(padx=20, pady=10, fill=BOTH, expand=True)

wn.mainloop()
