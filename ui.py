import tkinter as tk
from database import add_entry
from weather_api import get_weather
from database import get_all_entries

def tran_for_add():
    text_la = input_la.get()
    text_lo = input_lo.get()
    text_date = input_date.get()
    text_city = input_city.get()
    text_mood = input_mood.get()
    text_note = input_note.get()
    try:
        latitude = float(text_la)
        longitude = float(text_lo)
    except ValueError:
        print('กรุณาใส่พิกัด latitude/longitude ให้ครบและเป็นตัวเลข')
        return

    temp = get_weather(latitude, longitude)
    if temp is not None:
        add_entry(text_date, text_city, temp, text_mood, text_note)

        print('add to database is success')
    else:
        print('add to database is failed')
    get_all_entries()

window = tk.Tk()
window.title('demo weather')
window.geometry('500x500')

#date
title_date = tk.Label(master=window, text='date (YYYY-MM-DD)')
input_date = tk.Entry(master=window)
title_date.pack(pady=5)
input_date.pack(pady=5)

#city
title_city = tk.Label(master=window, text='city (BKK)')
input_city = tk.Entry(master=window)
title_city.pack(pady=5)
input_city.pack(pady=5)

#mood
title_mood = tk.Label(master=window, text='mood')
input_mood = tk.Entry(master=window)
title_mood.pack(pady=5)
input_mood.pack(pady=5)

#note
title_note = tk.Label(master=window, text='note')
input_note = tk.Entry(master=window)
title_note.pack(pady=5)
input_note.pack(pady=5)

title_la = tk.Label(master=window, text='input latitude')
title_la.pack(pady=5)

input_la = tk.Entry(master=window)
input_la.pack(pady=5)

title_lo = tk.Label(master=window, text='input longitude')
title_lo.pack(pady=5)

input_lo = tk.Entry(master=window)
input_lo.pack(pady=5)

bottom_add_result = tk.Button(master=window,command=tran_for_add ,text='add result',width=30, height=10)
bottom_add_result.pack(pady=5)


window.mainloop()
