from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    weather_data = {
  "cities": [
    {
      "city": "Gopalganj",
      "country": "India",
      "temperature": 30.5,
      "humidity": 65,
      "weather": "Partly cloudy"
    },
    {
      "city": "Mumbai",
      "country": "India",
      "temperature": 28.0,
      "humidity": 78,
      "weather": "Rainy"
    },
    {
      "city": "New York",
      "country": "USA",
      "temperature": 22.3,
      "humidity": 60,
      "weather": "Clear"
    },
    {
      "city": "Tokyo",
      "country": "Japan",
      "temperature": 26.7,
      "humidity": 70,
      "weather": "Cloudy"
    },
    {
      "city": "Sydney",
      "country": "Australia",
      "temperature": 18.4,
      "humidity": 55,
      "weather": "Sunny"
    }
  ]

    }

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
