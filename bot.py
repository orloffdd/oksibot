import asyncio
import logging
import sys
from aiogram import F, Bot, Dispatcher, html, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from src.keyboard import *
from src.scripts import *
from src.db_connect import *

TOKEN = "6867955838:AAFpFumGCDd8LyXMy8ODT7AUc5cq1QMUARs"

dp = Dispatcher()

class MyStates(StatesGroup):
    start = State()
    admin = State()
    cat1 = State()
    cat2 = State()
    cat3 = State()
    cat4 = State()
    cat5 = State()
    cat6 = State()
    cat7 = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard_start)
    await state.set_state(MyStates.start)

#Admin panel
@dp.message(Command("admin"))
async def command_admin_handler(m: Message, state: FSMContext) -> None:
    await m.answer("Вы в панели администратора", reply_markup=builder_admin)
    await state.set_state(MyStates.admin)

@dp.message(F.text == "Импортировать базу данных", StateFilter(MyStates.admin))
async def exit_admin(m: Message, state: FSMContext) -> None:
    await m.answer("База данных иммпортирована!")
    await restore_table("database.db")
    await fill_db("database.db")
    

@dp.message(F.text == "Выход", StateFilter(MyStates.admin))
async def exit_admin(m: Message, state: FSMContext) -> None:
    await m.answer("Вы в главном меню", reply_markup=keyboard_start())
    await state.set_state(MyStates.start)


#User panel
@dp.message(F.text == "Найти ГЭСН", StateFilter(MyStates.start))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat1)
    keyboard = await find_cat("database.db", "category_1")
    await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat1))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat2)
    keyboard = await find_cat_not1("database.db", "category_2", m.text)
    if isinstance(keyboard, str):
        await m.answer(keyboard)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat2))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat3)
    keyboard = await find_cat_not1("database.db", "category_3", m.text)
    if isinstance(keyboard, str):
        with open("ГЭСН.txt", "w", encoding="utf-8") as file:
            file.write(keyboard)
        document = types.FSInputFile("ГЭСН.txt")
        await m.answer_document(document)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat3))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat4)
    keyboard = await find_cat_not1("database.db", "category_4", m.text)
    if isinstance(keyboard, str):
        with open("ГЭСН.txt", "w", encoding="utf-8") as file:
            file.write(keyboard)
        document = types.FSInputFile("ГЭСН.txt")
        await m.answer_document(document)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat4))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat5)
    keyboard = await find_cat_not1("database.db", "category_5", m.text)
    if isinstance(keyboard, str):
        with open("ГЭСН.txt", "w", encoding="utf-8") as file:
            file.write(keyboard)
        document = types.FSInputFile("ГЭСН.txt")
        await m.answer_document(document)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat5))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat6)
    keyboard = await find_cat_not1("database.db", "category_6", m.text)
    if isinstance(keyboard, str):
        with open("ГЭСН.txt", "w", encoding="utf-8") as file:
            file.write(keyboard)
        document = types.FSInputFile("ГЭСН.txt")
        await m.answer_document(document)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

@dp.message(StateFilter(MyStates.cat6))
async def find_gesn(m: Message, state: FSMContext):
    await state.set_state(MyStates.cat7)
    keyboard = await find_cat_not1("database.db", "category_7", m.text)
    if isinstance(keyboard, str):
        with open("ГЭСН.txt", "w", encoding="utf-8") as file:
            file.write(keyboard)
        document = types.FSInputFile("ГЭСН.txt")
        await m.answer_document(document)
    else:
        await m.answer("Выберите категорию", reply_markup=keyboard)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())