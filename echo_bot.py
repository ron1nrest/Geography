from aiogram import Bot, Dispatcher, F 
from aiogram.filters import Command
from aiogram.types import Message, ContentType

API_TOKEN: str = "5997794456:AAGUW00UG5NG_9hK9nc5y3GoAHrPKJVxqJc"
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

async def process_start_command(message: Message):
    await message.answer(text="Тебя приветсвует эхо-бот!")

async def process_help_command(message: Message):
    await message.answer(text="Чтобы опробовать напиши что-нибудь")

async def send_photo(message: Message):
    await message.answer_photo(message.photo[0].file_id)

async def send_video(message: Message):
    await message.answer_video(message.video.file_id)

async def send_audio(message: Message):
    await message.answer_audio(message.audio.file_id)

async def send_sticker(message: Message):
    await message.answer_sticker(message.sticker.file_id)

async def send_voice(message: Message):
    await message.answer_voice(message.voice.file_id)

dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_start_command, Command(commands=["help"]))
dp.message.register(send_photo, F.photo)
dp.message.register(send_video, F.video)
dp.message.register(send_audio, F.audio)
dp.message.register(send_sticker, F.sticker)
dp.message.register(send_voice, F.voice)

if __name__ == "__main__":
    dp.run_polling(bot)