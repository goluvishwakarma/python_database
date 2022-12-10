from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("weather App")
root.geometry("1200x600+400+400")
root.configure(bg="#57adff")
root.resizable(False, False)


# get weather ,
def getWeather():
    city = textField.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timeZone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)} °N, {round(location.longitude, 4)} °E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)

    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather API,
    api = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" + str(
        location.longitude) + "&appid=7b249235cf6be2334a7582c5d8906c25"
    json_data = requests.get(api).json()

    temp = round((json_data['main']['temp'] - 273.15), 4)
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']

    t.config(text=(temp, "Kel"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    # first cell
    # firstDayImage = json_data['daily'][0]['weather'][0]['icon']
    firstDayImage = json_data['weather'][0]['icon']
    print(firstDayImage)

    print(json_data)
    # second cell

    # third cell

    # fourth cell

    # fifth cell

    # sixth cell

    # seventh cell

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


# icon
image_icon = PhotoImage(file="Images/cloud.png")  # logo
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/black-rectangle.png")
Label(root, image=Round_box, bg="#67adff").place(x=30, y=110)

# labels,
# temperature
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="White", bg="#203243")
label1.place(x=50, y=120)

# Humidity
label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="White", bg="#203243")
label2.place(x=50, y=140)

# Pressure
label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="White", bg="#203243")
label3.place(x=50, y=160)

# Wind Speed
label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="White", bg="#203243")
label4.place(x=50, y=180)

# Description
label5 = Label(root, text="Description", font=('Helvetica', 11), fg="White", bg="#203243")
label5.place(x=50, y=200)

# search box
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=370, y=120)

# image in search bar
weat_image = PhotoImage(file="Images/Layer 7.png")
weatherImage = Label(root, image=weat_image, bg="#203243")
weatherImage.place(x=390, y=127)

textField = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textField.place(x=470, y=130)
textField.focus()

search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=745, y=125)

# Bottom box
frame = Frame(root, width=1200, height=220, bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes
firstBox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondBox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstBox, bg="#212120").place(x=150, y=40)
Label(frame, image=secondBox, bg="#212120").place(x=500, y=45)
Label(frame, image=secondBox, bg="#212120").place(x=600, y=45)
Label(frame, image=secondBox, bg="#212120").place(x=700, y=45)
Label(frame, image=secondBox, bg="#212120").place(x=800, y=45)
Label(frame, image=secondBox, bg="#212120").place(x=900, y=45)
Label(frame, image=secondBox, bg="#212120").place(x=1000, y=45)

# clock , here we will place time
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=35)

# timezone
timeZone = Label(root, font=("Helvetica", 20, 'bold'), fg="white", bg="#57adff")
timeZone.place(x=900, y=20)

# longitude and latitude
long_lat = Label(root, font=("Helvetica", 10, 'bold'), fg="white", bg="#57adff")
long_lat.place(x=900, y=50)

# thpwd
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=170, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=170, y=140)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=170, y=160)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=170, y=180)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=170, y=200)

# first cell
firstFrame = Frame(root, width=230, height=132, bg="#282829")
firstFrame.place(x=155, y=425)

day1 = Label(firstFrame, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=40, y=5)

firstImage = Label(firstFrame, bg="#282829", fg="#fff")
firstImage.place(x=1, y=15)

# second cell
secondFrame = Frame(root, width=70, height=115, bg="#282829")
secondFrame.place(x=505, y=430)

day2 = Label(secondFrame, bg="#282829", fg="#fff")
day2.place(x=5, y=5)

secondImage = Label(secondFrame, bg="#282829", fg="#fff")
secondImage.place(x=7, y=20)

# third cell
thirdFrame = Frame(root, width=70, height=115, bg="#282829")
thirdFrame.place(x=605, y=430)

day3 = Label(thirdFrame, bg="#282829", fg="#fff")
day3.place(x=5, y=5)

thirdImage = Label(thirdFrame, bg="#282829", fg="#fff")
thirdImage.place(x=7, y=20)

# fourth cell
fourthFrame = Frame(root, width=70, height=115, bg="#282829")
fourthFrame.place(x=705, y=430)

day4 = Label(fourthFrame, bg="#282829", fg="#fff")
day4.place(x=5, y=5)

fourthImage = Label(fourthFrame, bg="#282829", fg="#fff")
fourthImage.place(x=7, y=20)

# fifth cell
fifthFrame = Frame(root, width=70, height=115, bg="#282829")
fifthFrame.place(x=805, y=430)

day5 = Label(fifthFrame, bg="#282829", fg="#fff")
day5.place(x=5, y=5)

fifthImage = Label(fifthFrame, bg="#282829", fg="#fff")
fifthImage.place(x=7, y=20)
# sixth cell
sixthFrame = Frame(root, width=70, height=115, bg="#282829")
sixthFrame.place(x=905, y=430)

day6 = Label(sixthFrame, bg="#282829", fg="#fff")
day6.place(x=5, y=5)

sixthImage = Label(sixthFrame, bg="#282829", fg="#fff")
sixthImage.place(x=7, y=20)
# seventh cell
seventhFrame = Frame(root, width=70, height=115, bg="#282829")
seventhFrame.place(x=1005, y=430)

day7 = Label(seventhFrame, bg="#282829", fg="#fff")
day7.place(x=5, y=5)

seventhImage = Label(seventhFrame, bg="#282829", fg="#fff")
seventhImage.place(x=7, y=20)




root.mainloop()
