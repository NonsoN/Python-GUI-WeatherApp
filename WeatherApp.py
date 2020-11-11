import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

#096c31ccf27324c19f46de5e65aead6b
#https://api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#TO DO:  Get the forecast over several days, implement icons to make the app look nicer

HEIGHT = 700
WIDTH = 800
root = tk.Tk()

def test_function(entry):
    print("Button clicked!")

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        final_string = 'City: %s \nConditions: %s \nTemperature (°F): %s' %(name, description, temperature)
    except:
        final_string = 'There was a problem retrieving that information. Please, enter a valid city...'

    return final_string

def get_weather(city):
    weather_key = '096c31ccf27324c19f46de5e65aead6b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q': city, 'units': 'imperial'}
    response =requests.get((url), params=params)
    weather = response.json()
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    label['text'] = format_response(weather)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='What\'s the weather?', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 30))
label.place(relwidth=1, relheight=1)


root.mainloop()