# Telegram_Echo_Bot

# Имя бота: Echo_Bot
# Никнейм бота: @Tetresh_bot
import telebot
import pyowm

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from config import TOKEN, API, city
from random import randint
from telebot import types


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    # sticker
    sti = open("AnimatedSticker.tgs", "rb")
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Rand Int 0-100")
    item2 = types.KeyboardButton("😊 Как дела?")
    markup.add(item1, item2)

    # message
    bot.send_message(message.chat.id,
        "Welcome, {0.first_name}!\nМоё имя - <b>{1.first_name}</b>.\n"
        "Введите погода для получения информации по погоде на сегодня.".format(
        message.from_user, bot.get_me()), parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def send_messege(message):
    if message.chat.type == "private":
        if message.text == "🎲 Rand Int 0-100":
            bot.send_message(message.chat.id, str(randint(0,100)))
        elif message.text == "😊 Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data="good")
            item2 = types.InlineKeyboardButton("Не очень", callback_data="bad")

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Отлично, а у тебя?", reply_markup=markup)
        elif message.text == "Погода" or message.text == "погода":
            config_dict = get_default_config()
            config_dict["language"] = "ru"
            owm = OWM(API, config_dict)

            owm.supported_languages
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(city)
            # observation = mgr.weather_at_place(message.text)

            # Сбор информации по погоде
            w = observation.weather
            DS = w.detailed_status                   # 'clouds'
            wind = w.wind()["speed"]                 # {'speed': 4.6, 'deg': 330}
            humidity = w.humidity                    # 87
            temp = w.temperature("celsius")["temp"]  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
            rain = w.rain                            # {}
            HI = w.heat_index                        # None
            clouds = w.clouds                        # 75

            # answer = "В городе " + message.text + " сейчас " + DS + "\n"
            answer = "В городе " + city + " сейчас " + DS + "\n"
            answer += "Температура " + str(temp) + " C" + "\n"
            answer += "Ветер " + str(wind) + " м/с" + "\n"
            answer += "Влажность " + str(humidity) + " %" + "\n"
            answer += "Осадки " + str(rain) + "\n"
            answer += "Облачнось " + str(clouds) + " %" + "\n\n"

            # Анализ температуры
            if temp < -4:
                answer += ("Сейчас на улице морозно.")
            elif temp < 0 and temp >= -4:
                answer += ("Сейчас на улице холодно.")
            elif temp >= 0 and temp < 12:
                answer += ("Сейчас на улице прохладно.")
            elif temp >= 12 and temp < 27:  
                answer += ("Сейчас на улице тепло.")
            else: # t > 27
                answer += ("Сейчас на улице жарко.")

            bot.send_message(message.chat.id, answer)           
        else:
            bot.send_message(message.chat.id, "К сожалению ни чем не могу помоч 😢")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                bot.send_message(call.message.chat.id, "Вот и отлично 😊")
            elif call.data == "bad":
                bot.send_message(call.message.chat.id, "Все наладится 😢")

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)

            # show alert (show_alert=True to enable)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!")

    except Exception as e:
        print(repr(e))


print("Program start")

# run bot
bot.polling(none_stop=True)

print("Program finish")
