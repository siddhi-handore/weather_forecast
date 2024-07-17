import tkinter
from tkinter import PhotoImage
import requests
from tkinter import *
from PIL import Image, ImageTk
def get_city():
    city = input_box.get()
    input_box.delete(0, tkinter.END)

    with open("api_key.txt", "r") as fp:
        api_key = fp.read();

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()
    label_city.config(text=f"{city}", font=("Helvetica", 20))
    temp = data['main']['temp']
    temp_celsius = temp - 273.15
    label_temp.config(text=f"{'%0.2f'%temp_celsius}℃", fg="dodgerblue", bg="bisque", font=("Arial", 30, "bold"))
    desc = data['weather'][0]['description']
    label_desc.config(text=desc, fg="purple", bg="bisque", font=("Arial", 15))

    for widget in frame4.winfo_children():
        widget.destroy()

    if "haze" in desc.lower():
        img_haze = PhotoImage(file="haze.png")
        haze_label = Label(frame4, image=img_haze)
        haze_label.image = img_haze
        haze_label.grid(row=0, column=1)
    elif "clear sky" in desc.lower():
        img_clear = PhotoImage(file="clear-sky.png")
        clear_label = Label(frame4, image=img_clear)
        clear_label.image = img_clear
        clear_label.grid(row=0, column=1)
    elif "scattered clouds" in desc.lower() or "broken clouds" in desc.lower() or "few clouds" in desc.lower():
        img_scat = PhotoImage(file="clouds.png")
        scat_label = Label(frame4, image=img_scat)
        scat_label.image = img_scat
        scat_label.grid(row=0, column=1)
    elif "overcast clouds" in desc.lower():
        img_cloudy = PhotoImage(file="cloudy (1).png")
        cloudy_label = Label(frame4, image=img_cloudy)
        cloudy_label.image = img_cloudy
        cloudy_label.grid(row=0, column=1)
    elif "light rain" in desc.lower() or "drizzle" in desc.lower():
        img_rain = PhotoImage(file="light rain (1).png")
        rain_label = Label(frame4, image=img_rain)
        rain_label.image = img_rain
        rain_label.grid(row=0, column=1)
    elif "heavy intensity rain" in desc.lower():
        img_heavy = PhotoImage(file="heavy rain (1).png")
        heavy_label = Label(frame4, image=img_heavy)
        heavy_label.image = img_heavy
        heavy_label.grid(row=0, column=1)

    pressure = data['main']['pressure']
    label_pressure.config(text=f"Pressure : {pressure}mb", bg="bisque", fg="purple", font=("Arial", 15))
    humidity = data['main']['humidity']
    label_humidity.config(text=f"Humidity : {humidity}%", bg="bisque", fg="purple", font=("Arial", 15))

if __name__ == '__main__':
    root = Tk()
    root.geometry('555x444')
    root.title("Weather forecast")
    root.config(bg="bisque")
    frame_main = Frame(root, bg="bisque")
    frame_main.pack(fill=X)

    frame1 = Frame(frame_main, bg="bisque")
    frame1.grid(row=0, column=0)

    img = Image.open("weather - Copy.jpg")
    photo = ImageTk.PhotoImage(img)
    img_label = Label(frame1, image=photo)
    img_label.grid(row=0, column=0, padx=10, pady=10)
    label_top = Label(frame1, text="Weatherly", bg="bisque", fg="dodgerblue", font=("Helvetica", 30, "bold"),
                      padx=10, pady=20)
    label_top.grid(row=0, column=1, padx=10, pady=10)

    frame2 = Frame(frame_main, bg="bisque")
    frame2.grid(row=1, column=0, pady=10)

    search_btn = Button(frame2, text="Search", bg="dodgerblue", fg="white", activebackground="skyblue",
                        activeforeground="white", padx=10, font=("Arial", 14), borderwidth=0, highlightthickness=0, command=get_city)
    search_btn.grid(row=0, column=1, padx=10, pady=10)
    input_box = Entry(frame2, width=25, font=("Arial", 18), borderwidth=0, highlightthickness=0)
    input_box.grid(row=0, column=0, padx=20, pady=10)

    frame3 = Frame(frame_main, bg="bisque")
    frame3.grid(row=2, column=0, pady=10)

    label_city = Label(frame3, text="", bg="bisque", fg="purple", padx=10, pady=10)
    label_city.grid(padx=10, pady=10)
    label_temp = Label(frame3, text="", fg="purple", bg="bisque")
    label_temp.grid(padx=10, pady=10)
    label_desc = Label(frame3, text="", fg="purple", bg="bisque")
    label_desc.grid(padx=10, pady=10)
    label_pressure = Label(frame3, text="", fg="purple", bg="bisque")
    label_pressure.grid(padx=10, pady=10)
    label_humidity = Label(frame3, text="", fg="purple", bg="bisque")
    label_humidity.grid(padx=10, pady=10)

    frame4 = Frame(frame_main, bg="bisque")
    frame4.grid(row=2, column=1)


    root.mainloop()
