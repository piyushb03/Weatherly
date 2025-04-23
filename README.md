# 🌦️ **Weatherly** - Desktop Weather Application

**Weatherly** is a Python-based desktop application that provides users with up-to-date weather information, including the current weather and a 3-day forecast. The app fetches weather data via the **OpenWeatherMap API** and displays the details directly on the main page. With a user-friendly interface, you can get detailed weather information for any city, all without the need for desktop notifications.

## 🛠️ **Technologies Used**
- **Python 3.x**
- **Tkinter** (for GUI development)
- **Requests** (for making API calls)
- **OpenWeatherMap API** (for fetching weather data)

## 🌍 **Features**
- **Current Weather Information**:
  - Temperature (in Celsius)
  - Atmospheric pressure
  - Humidity level
  - Weather description (e.g., Clear, Rainy, etc.)

- **3-Day Weather Forecast**:
  - Forecasts for the next 3 days at 12:00 PM.
  - Temperature (in Celsius)
  - Weather description for each day.

- **Simple, Interactive GUI**: Clean and user-friendly interface using **Tkinter**.

## 🚀 **Installation Guide**

### Prerequisites:
Ensure you have **Python 3.x** installed on your system.

### Steps to Install:

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/weatherly.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd weatherly
   ```

3. **Install the required libraries**:
   Run the following command to install the necessary dependencies:
   ```bash
   pip install requests
   ```

4. **Get your OpenWeatherMap API key**:
   - Visit [OpenWeatherMap API](https://openweathermap.org/api) to sign up and obtain an API key.
   - Replace the placeholder `your_api_key` in the code with your actual API key.

5. **Run the application**:
   ```bash
   python weather_app.py
   ```

6. **Start using the app**:
   Enter a location (city) in the input box and click on **Get Weather Info** to see the weather details.

## 💡 **How to Use**

1. Open **Weatherly**.
2. Type the name of the city you want the weather for.
3. Click the **Get Weather Info** button.
4. View the current weather details and 3-day forecast right on the main page.

## 🌍 **Demo**

Here is what the application will look like:

![image](https://github.com/user-attachments/assets/216d435a-dce8-4f67-8e09-55d8c95bcf9e)


## 📄 **Code Explanation**

### 1. **GUI Components**:
   - The GUI is built using **Tkinter** and includes a label, an input box, and a button to fetch weather data.
   - The window is styled to provide a simple, clean user interface.

### 2. **Weather Data Fetching**:
   - **Weatherly** uses the **OpenWeatherMap API** to get weather data for the given city.
   - It fetches data like temperature, humidity, pressure, and weather description and displays it directly in the GUI.
   - A 3-day weather forecast is displayed showing the weather for the next three days at 12:00 PM.

### 3. **Error Handling**:
   - In case of an invalid city name or a failed API request, **Weatherly** shows an error message using Tkinter’s `messagebox`.

## 🌱 **API Usage**

**Weatherly** uses the **OpenWeatherMap API** to retrieve real-time weather data. The API key is required to access the weather data, which you can obtain by signing up for a free account on the OpenWeatherMap website.

To integrate or modify the weather data source:
- Visit [OpenWeatherMap API](https://openweathermap.org/api) for more details.
- Replace the placeholder API key in the code with your personal key.

