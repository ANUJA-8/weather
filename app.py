from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    print(data)  # Print the API response for debugging

    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '99995d0dbd384bbafd5f76c81c32bd50'  # Replace with your OpenWeatherMap API key
        weather_data = get_weather(api_key, city)

        if 'main' in weather_data:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            # weather.html path
            return render_template('weather.html', city=city, temperature=temperature, description=description)
        else:
            error_message = 'Failed to retrieve weather data. Check your city name.'
            # path of weather.html
            return render_template('weather.html', error_message=error_message)  

    # path of weahter.html
    return render_template('weather.html')

if __name__ == "__main__":
    app.run(debug=True)


