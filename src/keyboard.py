from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton



button1 = KeyboardButton(text="Импортировать базу данных")
button2 = KeyboardButton(text="Выход")
builder_admin= ReplyKeyboardMarkup(keyboard=[[button1], [button2]], resize_keyboard=True)

button_find_gesn = KeyboardButton(text="Найти ГЭСН")

keyboard_start = ReplyKeyboardMarkup(keyboard=[[button_find_gesn]], resize_keyboard=True)
