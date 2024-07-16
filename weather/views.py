from django.shortcuts import render
import os
# from dotenv import load_dotenv
import json
import urllib.request

# load_dotenv()  # Load environment variables from.env file

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = os.environ.get("OPEN_WEATHER_API_KEY")
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = urllib.request.urlopen(base_url).read()
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data["sys"]['country']),
            "coordinate": str(json_data["coord"]['lon']) + ", " + str(json_data["coord"]['lat']),
            "temp": str(json_data["main"]["temp"])+"k",
            "pressure" : str(json_data["main"]["pressure"]),
            "humidity" : str(json_data["main"]["humidity"])
        }

        return render(request, 'index.html', {"data": data, "city": city})
    
    return render(request, 'index.html')
