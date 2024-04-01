from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import requests
import customtkinter
from googletrans import Translator

def reset_search_field():
    entry.delete(0, END)
def on_button_click():
    get_weather()
    reset_search_field()

def on_entry_click(event):
    if entry.get() == "Введите ваш город":
        entry.delete(0, "end")
        entry.configure(fg="#E5D3C5")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Введите ваш город")
        entry.configure(fg="#777777")

humidity_label = None
wind_label = None
pressure_label = None
city_pg = None
temperature_label = None
weather_label = None

def get_weather():
    global humidity_label, wind_label, pressure_label, city_pg, temperature_label, weather_label

    if humidity_label:
        humidity_label.destroy()
        humidity_label = None
    if wind_label:
        wind_label.destroy()
        wind_label = None
    if pressure_label:
        pressure_label.destroy()
        pressure_label = None
    if city_pg:
        city_pg.destroy()
        city_pg = None
    if temperature_label:
        temperature_label.destroy()
        temperature_label = None
    if weather_label:
        weather_label.destroy()
        weather_label = None

    city = entry.get().title()
    api_key = "6797eed588be7d31667c5428589c9ffc"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_description = data["weather"][0]["description"]
    translator = Translator()
    translation = translator.translate(weather_description, dest='ru')
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    pressure = data["main"]["pressure"]

    humidity_label = customtkinter.CTkLabel(root, text=f'{humidity}%', text_color="#5fafee", fg_color='#252420', width=120,
                                            height=70, font=("Times New Roman", 30))
    humidity_label.place(x=781, y=286)

    wind_label = customtkinter.CTkLabel(root, text=f'{wind_speed} м/с', text_color="#bcd0e1", fg_color='#252420', width=120,
                                        height=70, font=("Times New Roman", 30))
    wind_label.place(x=595, y=429)

    pressure_label = customtkinter.CTkLabel(root, text=f'{pressure} гПа', text_color="#53538f", fg_color='#252420', width=120,
                                            height=70, font=("Times New Roman", 30))
    pressure_label.place(x=781, y=429)

    city_pg = customtkinter.CTkLabel(root, text=f'{city} \n {translation.text}', text_color="#e7a47a", fg_color='#252420',
                                     width=260, height=120, font=("Times New Roman", 32))
    city_pg.place(x=620, y=100)

    weather_label = customtkinter.CTkLabel(root, text=f'{translation.text}', text_color="#c7c2b8", fg_color='#252420',
                                           width=330, height=40, font=("Times New Roman", 25))
    weather_label.place(x=582, y=162)

    if '-' in str(temperature):
        temperature_label = customtkinter.CTkLabel(root, text=f"{temperature}°C", text_color="turquoise",
                                                   fg_color='#252420', width=120, height=70, font=("Times New Roman", 30))
        temperature_label.place(x=595, y=286)

    else:
        temperature_label = customtkinter.CTkLabel(root, text=f"{temperature}°C", text_color="#5eaa20",
                                                   fg_color='#252420', width=120, height=70, font=("Times New Roman", 30))
        temperature_label.place(x=595, y=286)

root = Tk()
root.title("Погода")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 480
h = h - 270
root.geometry(f'960x540+{w}+{h}')
root.resizable(width=False, height=False)

root.configure(bg="#27241f")

image = Image.open('fon_pogoda.jpg')
background_image = ImageTk.PhotoImage(image)

icon_image = Image.open('log_pogoda.png')
icon = ImageTk.PhotoImage(icon_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.iconphoto(True, icon)

animation1 = Image.open("no_data_pogoda.gif")
animation2 = Image.open("no_data_pogoda.gif")
animation3 = Image.open("no_data_pogoda.gif")
animation4 = Image.open("no_data_pogoda.gif")
animation5 = Image.open("no_data_pogoda.gif")

frames1 = []
frames2 = []
frames3 = []
frames4 = []
frames5 = []

try:
    while True:
        frames1.append(ImageTk.PhotoImage(animation1))
        frames2.append(ImageTk.PhotoImage(animation2))
        frames3.append(ImageTk.PhotoImage(animation3))
        frames4.append(ImageTk.PhotoImage(animation4))
        frames5.append(ImageTk.PhotoImage(animation5))

        animation1.seek(len(frames1))
        animation2.seek(len(frames2))
        animation3.seek(len(frames3))
        animation4.seek(len(frames4))
        animation5.seek(len(frames5))
except EOFError:
    pass

label1 = Label(root, image=frames1[0], bg="#27241f")
label1.pack()
label1.place(x=711, y=143)

label2 = Label(root, image=frames2[0], bg="#27241f")
label2.pack()
label2.place(x=618, y=301)

label3 = Label(root, image=frames3[0], bg="#27241f")
label3.pack()
label3.place(x=804, y=301)

label4 = Label(root, image=frames4[0], bg="#27241f")
label4.pack()
label4.place(x=618, y=442)

label5 = Label(root, image=frames5[0], bg="#27241f")
label5.pack()
label5.place(x=804, y=442)

def animate1(frame_index):
    label1.configure(image=frames1[frame_index])
    label1.image = frames1[frame_index]

    frame_index = (frame_index + 1) % len(frames1)
    root.after(400, animate1, frame_index)

def animate2(frame_index):
    label2.configure(image=frames2[frame_index])
    label2.image = frames2[frame_index]

    frame_index = (frame_index + 1) % len(frames2)
    root.after(400, animate2, frame_index)

def animate3(frame_index):
    label3.configure(image=frames3[frame_index])
    label3.image = frames3[frame_index]

    frame_index = (frame_index + 1) % len(frames3)
    root.after(400, animate3, frame_index)

def animate4(frame_index):
    label4.configure(image=frames4[frame_index])
    label4.image = frames4[frame_index]

    frame_index = (frame_index + 1) % len(frames4)
    root.after(400, animate4, frame_index)

def animate5(frame_index):
    label5.configure(image=frames5[frame_index])
    label5.image = frames5[frame_index]

    frame_index = (frame_index + 1) % len(frames5)
    root.after(400, animate5, frame_index)

animate1(1)
animate2(1)
animate3(1)
animate4(1)
animate5(1)

poisk_image = Image.open('poisk_pogoda.png')
poisk_image = poisk_image.resize((33, 33))
poisk = ImageTk.PhotoImage(poisk_image)
my_button = Button(root, image=poisk, command=on_button_click, bd=0, bg="#27241f", activebackground="#27241f")
my_button.place(relx=0.94, rely=0.10649, anchor=CENTER)

entry = Entry(root, font=("Times New Roman", 18), bd=0, bg="#27241f", fg="#777777", insertbackground="#4d4c48")
entry.insert(0, "Введите ваш город")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
entry.place(relx=0.735, rely=0.10649, anchor=CENTER)

def on_return_press(event):
    if event.keysym == "Return":
        my_button.invoke()

entry.bind("<KeyPress>", on_return_press)

root.mainloop()
