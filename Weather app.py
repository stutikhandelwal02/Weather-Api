import tkinter as tk
from tkinter import ttk
import requests
import time

def getWeather(root):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=126950222ad3e379e259cbdab7a406c4"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind =json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']- 19800))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']- 19800))

    final_info = condition +"\t" + str(temp) + "°C"
    final_data = "\n" +"Max Temp: "+ str(max_temp) +"\n" +"Min Temp: "+str(min_temp) + "\n" + "Pressure: "+ str(pressure) +"\n" + "Humidity: "+ str(humidity) + "\n" + "Wind Speed: " +str(wind) +"\n"+ "Sunrise: "+sunrise +"\n"+"Sunset: "+sunset
    label1.config(text = final_info)
    label2.config(text = final_data)    
    
root = tk.Tk()
root.geometry("600x500")
root.configure(bg= "#ff8c00")
root.title("WEATHER APP")


f = ("poppins",20)
t = ("poppins",35)

textfield = ttk.Entry(root,font = "Times 35")
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(root, font = t,bg="#ff8c00")
label1.pack()
label2 = tk.Label(root, font = f,bg ="#ff8c00")
label2.pack()

root.mainloop()
