# Get_Weather
from colorama import init, Fore, Back, Style
from pyowm import OWM
from pyowm.utils import config, timestamps
from config import API, city


config_dict = config.get_default_config_for_subscription_type("professional")
config_dict["language"] = "ru" # language is Russian

owm = OWM(API, config_dict)
mgr = owm.weather_manager()

place = city
observation = mgr.weather_at_place(place)
w = observation.weather

DS = w.detailed_status                   # 'clouds'
wind = w.wind()["speed"]                 # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                    # 87
temp = w.temperature("celsius")["temp"]  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
rain = w.rain                            # {}
HI = w.heat_index                        # None
clouds = w.clouds                        # 75


init()

print(Fore.CYAN)
print("В городе " + place + " сейчас " + DS) # подробный статус
print("Ветер " + str(wind) + ' м/с') # Ветер
print("Влажность " + str(humidity) + " %") # Влажность
print("Температура " + str(temp) + " C") # Температура
print("Осадки " + str(rain)) # Осадки
print("Индекс тепла " + str(HI)) # индекс тепла
print("Облачнось " + str(clouds) + " %") # Облачнось

# Анализ данных температуры
t = temp
if t < -4:
    print(Fore.CYAN)
    print("Сейчас на улице морозно.")
elif t < 0 and t >= -4:
    print(Fore.WHITE)
    print("Сейчас на улице холодно.")
elif t >= 0 and t < 12:
    print(Fore.GREEN)
    print("Сейчас на улице прохладно.")
elif t >= 12 and t < 27:
    print(Fore.YELLOW)    
    print("Сейчас на улице тепло.")
else: # t > 27
    print(Fore.RED)
    print("Сейчас на улице жарко.")

input()
