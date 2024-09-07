from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own API key
API_KEY = 'your_openweathermap_api_key'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        return render_template('results.html', weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
