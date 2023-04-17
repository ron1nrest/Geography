from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text 
from aiogram.types import Message, FSInputFile
import time
API_TOKEN: str = "6200803038:AAEFmgztl6nw8pGVna7ZlmN4IOeB8wixe1A"
bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

users: dict = {}

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("<b>Напишите в чат историко-географический регион по классификации Вольского (доступные: Западная Европа, Центрально-Восточная Европа, Российско- Евроазиатский регион, Восточная Азия)</b>", parse_mode="HTML")
    photo = FSInputFile("regions.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("<b>Этот бот опишет состав и особенность, географическую характеристику историко-географического региона по классификации Вольского</b>", parse_mode="HTML")

@dp.message(Text(text=["Западная Европа", "Европа Западная"], ignore_case=True))
async def west_europe(message:Message):
    await message.reply("<b>Западный регион Европы расположен на суженой части Евразии. Ее территорию в основном омывают воды Атлантического океана. Только северная часть Скандинавского полуострова — водами Северного Ледовитого океана. Занимая довольно большую территорию, западная Европа разделена на сравнительно небольшие государства.</b>", parse_mode="HTML")
    time.sleep(2)
    await message.answer("<i>Первая особенность связана с небольшими расстояниями между европейскими городами. Например, большинство поездов, совершающих рейсы в Европе, лишены спальных вагонов. Много европейских государств расположены вблизи оживленных морских путей сообщения.</i>", parse_mode="HTML")
    photo = FSInputFile("we.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@dp.message(Text(text=["Центрально-Восточная Европа", "Центрально Восточная Европа", "Центральная Восточная Европа", "Центральная-Восточная Европа"], ignore_case=True))
async def central_europe(message:Message):
    await message.reply("<b>В состав этого региона входят Польша, Чехия, Словакия, Венгрия, Украина, Беларусь, Литва, Латвия, Эстония и европейская часть России.</b>", parse_mode="HTML")
    time.sleep(2)
    await message.answer("<i>В состав этого региона входят Польша, Чехия, Словакия, Венгрия, Украина, Беларусь, Литва, Латвия, Эстония и европейская часть России. Главные особенности ЭГП — положение на западных рубежах России, граница с развитыми государствами Европы, прямой выход Польши, Украины и стран Балтии к морям. Через этот регион проходят транспортные магистрали, соединяющие Россию со странами Западной и Южной Европы, что благоприятствует широкому общеевропейскому сотрудничеству. Страны расположены компактно по отношению друг к другу.</i>", parse_mode="HTML")   
    photo = FSInputFile("ce.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)    

@dp.message(Text(text=["Российско- Евроазиатский регион", "Российско Евроазиатский регион", "Российско - Евроазиатский регион"], ignore_case=True))
async def rus_euro(message:Message):
    await message.reply('''<b>Один из наиболее крупных. Включает:

Россию.
Украину.
Беларусь.
Казахстан.
Монголию.
страны Средней Азии.
страны Кавказа.</b>''', parse_mode="HTML")
    time.sleep(2)
    await message.answer("<i>Достопримечательностей в Российско-Евроазиатском регионе не меньше, чем в Западной Европе, однако они мало популярны у туристов. Это связано с относительной закрытостью стран, расположенных здесь. У региона большой потенциал. Кроме того, он богат на ресурсы. В России можно найти практически все известные полезные ископаемые. Украина богата своими плодородными чернозёмами. Степи Казахстана и Монголии — идеальное место для скотоводства.</i>", parse_mode="HTML")
    photo = FSInputFile("rer.png")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)   

@dp.message(Text(text=["Восточная Азия", "восточно азия"], ignore_case=True))
async def east_asia(message:Message):
    await message.reply("<b>Восточную Азию омывают воды Тихого океана: Южно-Китайского, Востояно-Китайского и Японского морей.</b>", parse_mode="HTML")
    time.sleep(2)
    await message.answer("<i>В Восточной Азии темпы экономического развития очень высоки. Так, Япония, Корея и Китай славятся автотранспортной продукцией. Регион богат природным газом и нефтью, черными и цветными металлами. В странах, входящих в состав региона, налажен экспорт чайной продукции и риса, сахарного тростника и арахиса, сои и фруктов, специй. На территории региона добывают натуральный каучук, выращивают хлопок.</i>", parse_mode="HTML")   
    photo = FSInputFile("ea.jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=photo) 

if __name__ == "__main__":
    dp.run_polling(bot)