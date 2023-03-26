from django.shortcuts import render
from django.contrib import messages
import requests
import json

def weather(location):
    url = f"https://api.weatherapi.com/v1/current.json?key=a5707250f3b34319a28190139232503&q={location}"
    r = requests.get(url)
    js = json.loads(r.text)
    try:
        temp_c = js["current"]["temp_c"]
        temp_f = js["current"]["temp_f"]
        last_updated = js["current"]["last_updated"]
        name = js["location"]["name"]
        region = js["location"]["region"]
        country = js["location"]["country"]
        localtime = js["location"]["localtime"]
        return temp_c, temp_f, last_updated, name, region, country, localtime
    except Exception:
        pass

def index(request):
    if request.method=="POST":
        location = request.POST.get('location')
        str(location)
        try:
            temp_c, temp_f, last_updated, name, region, country, localtime = weather(location)
        except Exception:
            pass
        
        try:
            context = {
                'temp':temp_c,
                'temp_f' : temp_f,
                'last_updated' : last_updated,
                'name' : name,
                'region' : region,
                'country' : country,
                'localtime' : localtime
            }
        except Exception:
            context = {
                 'temp': '',
                'temp_f' : '',
                'last_updated' : '',
                'name' : '',
                'region' : '',
                'country' : '',
                'localtime' : ''
            }
            messages.warning(request, 'Invalid Input')
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')
