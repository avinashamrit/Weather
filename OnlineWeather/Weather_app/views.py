from django.contrib import messages
from django.shortcuts import redirect, render
import requests
import datetime

def home(request):
    
    city = request.POST.get('city','mohali')    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f77aaadc276c1bcc350c60b812f1447"
    data = requests.get(url).json()

    if city is "":
        url = "http://api.openweathermap.org/data/2.5/weather?q=mohali&appid=1f77aaadc276c1bcc350c60b812f1447"
    
    elif data['cod'] == '404':
        messages.info(request,'Invalid Entry')
        return redirect ('home')
    
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f77aaadc276c1bcc350c60b812f1447"
    
    data = requests.get(url).json()

    minutes = 30
    hours = 5

    current_time = datetime.datetime.now()


    hours_added = datetime.timedelta(hours=hours,minutes=minutes)

    future_time = current_time + hours_added
    payload = {
        'name': data['name'],
        'weather': data['weather'][0]['main'],
        'description':data['weather'][0]['description'],
        'country':data['sys']['country'],
        'icon': data['weather'][0]['icon'],
        'kel_temperature': int(((data['main']['temp']) - 273) * 9/5 + 32),
        'cel_temperature': int(data['main']['temp']) - 273,
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'wind':data['wind']['speed'],
        't': future_time
    }

    # context = {'data':payload}
    # print(context)
    return render(request, 'home.html',{'data':payload})