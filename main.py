from database import add_entry
from weather_api import get_weather
from ui import tran_for_add

def save_bottom():
    date, city, mood, note = tran_for_add()
    print(date,city,mood)