from aiogram import Bot, Dispatcher, executor, types
from random import randint
def botstart():
    bot = Bot(token='6058248417:AAGSwl13lmsfV-v4E9LA2MXY6ko3k9_bxms')
    dp = Dispatcher(bot)
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.answer('Напиши "Мотивашка" чтобы получить картинку!')
    @dp.message_handler(content_types=['text'])
    async def sendm(message: types.Message):
        if message.text == "Мотивашка":
            path = str(randint(1, 10))+'.jpg'
            with open(path, 'rb') as m:
                await bot.send_photo(message.chat.id, m)
        else:
            path = 'neboltai'+str(randint(1, 2))+'.jpg'
            with open(path, 'rb') as m:
                await bot.send_photo(message.chat.id, m)
    executor.start_polling(dp)