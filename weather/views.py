from django.shortcuts import render
import os

import json
import urllib.request


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = os.environ.get("OPEN_WEATHER_API_KEY") #YOUR_API_KEY in .env file

        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            res = urllib.request.urlopen(base_url).read()

            json_data = json.loads(res)

            if str(json_data['cod']) == '200':
                data = {
                    "country_code" : str(json_data["sys"]['country']),
                    "coordinate": str(json_data["coord"]['lon']) + ", " + str(json_data["coord"]['lat']),
                    "temp": str(json_data["main"]["temp"])+" k",
                    "pressure" : str(json_data["main"]["pressure"]),
                    "humidity" : str(json_data["main"]["humidity"]),
                    "sea_level" : str(json_data["main"]["sea_level"]),
                    "ground_level" : str(json_data["main"]["grnd_level"]),
                    "visibility" : str(json_data["visibility"]) ,
                    "wind_speed" : str(json_data["wind"]["speed"])+' (km/h)',
                    # "wind_deg" : str(json_data["wind"]["deg"]),
                    "weather_description" : str(json_data["weather"][0]["description"]),
                    "sunrise" : str(json_data["sys"]["sunrise"]),
                }

                return render(request, 'index.html', {"data": data, "city": city})
        
            return render(request, 'index.html')
        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'index.html', {'error': 'Your requested location could not be found'})
        
        
    return render(request, 'index.html')
