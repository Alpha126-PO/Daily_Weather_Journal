import tkinter
import tkinter as tk
from select import select

from database import add_entry, delete_entry_all
from weather_api import get_weather, CITIES
from database import get_all_entries


def tran_for_add():
    #text_la = input_la.get()
    #text_lo = input_lo.get()
    # text_city = input_city.get()
    city_name = title_city_d.get()
    latitude, longitude = CITIES[title_city_d.get()]
    text_date = input_date.get()
    text_mood = input_mood.get()
    text_note = input_note.get()

    temp = get_weather(latitude, longitude)
    if temp is not None:
        add_entry(text_date, city_name, temp, text_mood, text_note)

        print('add to database is success')
    else:
        print('add to database is failed')
    get_all_entries()

def open_delete_window():
    delete_window = tk.Toplevel(master=window)
    delete_window.title('delete')
    delete_window.geometry('500x500')

    entries = get_all_entries()

    for entry in entries:
        show_all = tk.Label(delete_window, text=str(entry))
        show_all.pack(pady=5)

    def confirm_delete_all():
        delete_entry_all()
        delete_window.destroy()
        open_delete_window()


    delete_all = tk.Button(delete_window, text='delete all', command=confirm_delete_all, width=20, height=3)
    delete_all.pack(pady=5)

def open_all_data():
    all_data = tkinter.Toplevel(master=window)
    all_data.title('all data')
    all_data.geometry('500x500')

    entries = get_all_entries()
    for entry in entries:
        show_all = tk.Label(all_data, text=str(entry))
        show_all.pack(pady=5)





window = tk.Tk()
window.title('demo weather')
window.geometry('500x500')

#date
title_date = tk.Label(master=window, text='date (YYYY-MM-DD)')
input_date = tk.Entry(master=window)
title_date.pack(pady=5)
input_date.pack(pady=5)

#city
title_city_d = tk.StringVar(master=window)
title_city_d.set('กรุงเทพฯ')

city_dropdown = tk.OptionMenu(window, title_city_d, *CITIES)
city_dropdown.pack(pady=5)
#title_city = tk.Label(master=window, text='city (BKK)')
#input_city = tk.Entry(master=window)
#title_city.pack(pady=5)
#input_city.pack(pady=5)

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

#title_la = tk.Label(master=window, text='input latitude')
#title_la.pack(pady=5)

#input_la = tk.Entry(master=window)
#input_la.pack(pady=5)

#title_lo = tk.Label(master=window, text='input longitude')
#title_lo.pack(pady=5)

#input_lo = tk.Entry(master=window)
#input_lo.pack(pady=5)

bottom_add_result = tk.Button(master=window,command=tran_for_add ,text='add result',width=20, height=3,)
bottom_add_result.pack(pady=5)

open_delete_button = tk.Button(master=window, text='open delete', command=open_delete_window, width=20, height=3)
open_delete_button.pack(pady=5)

open_all_data_button = tk.Button(master=window, text='open all data', command=open_all_data, width=20, height=3)
open_all_data_button.pack(pady=5)

window.mainloop()
