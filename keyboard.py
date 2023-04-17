from aiogram.filters import CommandStart, Text
from aiogram import Bot, Dispatcher 
from aiogram.types import (Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


API_TOKEN: str = "6297608015:AAHvVjm65gVNSRmdurldY1Hvvb-6vXOjz2Q"

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)
@dp.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text="Check", reply_markup=my_keyboard)


if __name__ == "__main__":
    dp.run_polling(bot)