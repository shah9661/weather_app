from tkinter import*
from tkinter import messagebox
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
import os
from dotenv import load_dotenv
load_dotenv()


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=text_field.get()
        geolocator = Nominatim(user_agent="my_weather_app_2025", timeout=10)
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api_key = os.getenv("OPENWEATHER_API_KEY")
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        josn_data=requests.get(api).json()
        conditon=josn_data['weather'][0]['main']
        description=josn_data['weather'][0]['description']
        temp=int(josn_data['main']['temp']-273.15)
        presure=josn_data['main']['pressure']
        humidity=josn_data['main']['humidity']
        wind=josn_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(conditon,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=presure)
    except Exception as e:
        messagebox.showerror('Weather App','Invalid Entry!!')



# Search box
text_field=tk.Entry(root,justify="center",width=13,font=("poppins",25,"bold"),bg="#404040",fg="white",border=0)
text_field.place(x=100,y=40)
text_field.focus()

serch=Image.open('assets\\search1.png')
serch=serch.resize((38,38))
search_icon=ImageTk.PhotoImage(serch)
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=310,y=40)
#  weather logo
logo_image_row=Image.open("assets\\logo.png")
logo_image_row=logo_image_row.resize((250,250))
logo_image=ImageTk.PhotoImage(logo_image_row)
logo=Label(image=logo_image)
logo.place(x=175,y=120)

# box 
frame_image=PhotoImage(file="assets\\gradient_rectangle4.png")
frame_myimage=Label(image=frame_image)
frame_myimage.pack(padx=1,pady=5,side=BOTTOM)
# time
name=Label(root,font=('arial',15,"bold"))
name.place(x=50,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=50,y=130)
# label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#007BFF")
label1.place(x=190,y=413)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#007BFF")
label2.place(x=280,y=413)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#007BFF")
label3.place(x=410,y=413)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#007BFF")
label4.place(x=600,y=413)

t=Label(font=("arial",70,"bold"),fg='#ee666d')
t.place(x=420,y=180)
c=Label(font=("arial",15,"bold"))
c.place(x=420,y=280)
w=Label(text="...",font=('arial',20,"bold"),bg="#007BFF")
w.place(x=190,y=455)
h=Label(text="...",font=('arial',20,"bold"),bg="#007BFF")
h.place(x=280,y=455)
d=Label(text="...",font=('arial',20,"bold"),bg="#007BFF")
d.place(x=410,y=455)
p=Label(text="...",font=('arial',20,"bold"),bg="#007BFF")
p.place(x=600,y=455)


root.mainloop()
