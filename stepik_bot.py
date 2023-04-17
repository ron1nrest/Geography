from aiogram import Bot, Dispatcher 
from aiogram.types import Message 
from aiogram.filters import Command, BaseFilter, Text

API_TOKEN: str = "6297608015:AAHvVjm65gVNSRmdurldY1Hvvb-6vXOjz2Q"

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

admin_list = [6078529316]

class checkadmin(BaseFilter):

    def __init__(self, admin_list: list[int]):
        self.admin_list = admin_list 

    async def __call__(self, message:Message) -> bool:
        return message.from_user.id in self.admin_list

@dp.message(checkadmin(admin_list))
async def admin(message: Message):
    await message.answer("Вы являетесь админом!")
    print(message.from_user.id)
@dp.message()
async def admin(message: Message):
    await message.answer("Вы не вляетесь админом!")
    print(message.from_user.id)
if __name__ == "__main__":
    dp.run_polling(bot)