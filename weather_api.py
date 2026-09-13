import requests

def  get_weather(latitude, longitude):
    try:
        url = 'https://api.open-meteo.com/v1/forecast'
        params = {
            'latitude' : latitude,
            'longitude' : longitude,
            'current' : 'temperature_2m',
        }

        response = requests.get(url, params=params)
        data = response.json()
        temperature = data['current']['temperature_2m']
        return temperature

    except requests.exceptions.RequestException:
        print('Requests not available')
        return None
    except KeyError:
        print('index is fail, can not found temperature')
        return None



