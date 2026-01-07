import requests
from tkinter import *
from tkinter import messagebox as mb
import matplotlib.pyplot as plt

API_KEY = "YOUR API KEY HERE"

# ---------------- THEMES ----------------
DARK = {
    "bg": "#121212",
    "card": "#1e1e1e",
    "text": "white",
    "btn": "#0d6efd"
}

LIGHT = {
    "bg": "#e6f2ff",
    "card": "#ffffff",
    "text": "#000000",
    "btn": "#1f3c88"
}

current_theme = DARK

# ---------------- AUTO DETECT LOCATION ----------------
def auto_detect():
    try:
        data = requests.get("http://ip-api.com/json").json()
        city_entry.delete(0, END)
        city_entry.insert(0, data.get("city", ""))
    except:
        mb.showerror("Error", "Unable to auto-detect location")

# ---------------- AI WEATHER TIPS ----------------
def ai_weather_tips(temp):
    if temp >= 35:
        return "🔥 Very hot today. Stay hydrated and avoid direct sunlight."
    elif temp >= 25:
        return "🌤️ Warm and pleasant weather."
    elif temp >= 15:
        return "🧥 Slightly cool. Light jacket recommended."
    else:
        return "❄️ Cold weather. Wear warm clothes."

# ---------------- FETCH WEATHER ----------------
def get_weather():
    global forecast_dates, forecast_temps
    city = city_entry.get().strip()
    if not city:
        mb.showwarning("Input Error", "Please enter a city name")
        return

    try:
        # Current weather
        current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        current = requests.get(current_url).json()

        temp = round(current["main"]["temp"] - 273.15, 1)
        humidity = current["main"]["humidity"]
        desc = current["weather"][0]["description"].capitalize()

        output.config(state=NORMAL)
        output.delete(1.0, END)
        output.insert(END, f"🌍 City: {city.title()}\n")
        output.insert(END, f"🌡️ Temperature: {temp} °C\n")
        output.insert(END, f"💧 Humidity: {humidity} %\n")
        output.insert(END, f"☁️ Condition: {desc}\n\n")
        output.insert(END, "🤖 AI TIP\n")
        output.insert(END, ai_weather_tips(temp) + "\n\n")

        # Forecast
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
        forecast = requests.get(forecast_url).json()

        forecast_dates, forecast_temps = [], []
        shown = set()

        output.insert(END, "📅 3-DAY FORECAST (12 PM)\n")
        for item in forecast["list"]:
            if "12:00:00" in item["dt_txt"]:
                date = item["dt_txt"].split(" ")[0]
                if date not in shown:
                    ft = round(item["main"]["temp"] - 273.15, 1)
                    fd = item["weather"][0]["description"].capitalize()
                    output.insert(END, f"{date} → {ft} °C | {fd}\n")
                    forecast_dates.append(date)
                    forecast_temps.append(ft)
                    shown.add(date)
                if len(shown) == 3:
                    break

        output.config(state=DISABLED)

    except Exception as e:
        mb.showerror("Error", f"Unable to fetch weather data\n{e}")

# ---------------- GRAPH ----------------
def show_graph():
    if not forecast_dates:
        mb.showinfo("Info", "Please fetch weather first")
        return

    plt.figure(figsize=(6, 4))
    plt.plot(forecast_dates, forecast_temps, marker="o")
    plt.title("3-Day Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ---------------- THEME TOGGLE ----------------
def toggle_theme():
    global current_theme
    current_theme = LIGHT if current_theme == DARK else DARK
    apply_theme()

def apply_theme():
    wn.config(bg=current_theme["bg"])
    title.config(bg=current_theme["bg"], fg=current_theme["text"])
    city_entry.config(
        bg=current_theme["card"],
        fg=current_theme["text"],
        insertbackground=current_theme["text"]
    )
    output.config(bg=current_theme["card"], fg=current_theme["text"])
    btn_frame.config(bg=current_theme["bg"])
    for btn in buttons:
        btn.config(bg=current_theme["btn"], fg="white")

# ---------------- UI ----------------
forecast_dates, forecast_temps = [], []

wn = Tk()
wn.title("Weatherly")
wn.geometry("680x540")
wn.resizable(False, False)

title = Label(
    wn,
    text="Weatherly",
    font=("Segoe UI", 22, "bold")
)
title.pack(pady=10)

city_entry = Entry(
    wn,
    font=("Segoe UI", 12),
    width=30
)
city_entry.pack(pady=5)

btn_frame = Frame(wn)
btn_frame.pack(pady=10)

get_btn = Button(btn_frame, text="Get Weather", width=14, command=get_weather)
get_btn.grid(row=0, column=0, padx=4)

graph_btn = Button(btn_frame, text="View Graph", width=14, command=show_graph)
graph_btn.grid(row=0, column=1, padx=4)

auto_btn = Button(btn_frame, text="Auto Detect", width=14, command=auto_detect)
auto_btn.grid(row=0, column=2, padx=4)

theme_btn = Button(btn_frame, text="Change Theme", width=14, command=toggle_theme)
theme_btn.grid(row=0, column=3, padx=4)

buttons = [get_btn, graph_btn, auto_btn, theme_btn]

output = Text(
    wn,
    font=("Consolas", 11),
    width=75,
    height=14,
    bd=0
)
output.pack(padx=15, pady=10)
output.config(state=DISABLED)

apply_theme()
wn.mainloop()
