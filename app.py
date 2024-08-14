from flask import Flask, jsonify
import datetime
import pytz

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

@app.route('/time', methods=['GET'])
def get_time():
    time_data = {
        "cities": [
            {
                "city": "Gopalganj",
                "country": "India",
                "timezone": "Asia/Kolkata",
                "current_time": datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                "city": "New York",
                "country": "USA",
                "timezone": "America/New_York",
                "current_time": datetime.datetime.now(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                "city": "Tokyo",
                "country": "Japan",
                "timezone": "Asia/Tokyo",
                "current_time": datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                "city": "Sydney",
                "country": "Australia",
                "timezone": "Australia/Sydney",
                "current_time": datetime.datetime.now(pytz.timezone('Australia/Sydney')).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                "city": "London",
                "country": "UK",
                "timezone": "Europe/London",
                "current_time": datetime.datetime.now(pytz.timezone('Europe/London')).strftime('%Y-%m-%d %H:%M:%S')
            }
        ]
    }

    return jsonify(time_data)



@app.route('/name', methods=['GET'])
def get_name():
    name_data = {
        "names": [
            {
                "name": "Yash",
            },
                {
                "name": "Raj",
            },    {
                "name": "Mani",
            },    {
                "name": "VIT",
            }
        ]
    }

    return jsonify(name_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
