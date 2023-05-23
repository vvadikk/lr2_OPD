from aiogram import Bot, Dispatcher, executor, types
from random import randint
def botstart():
    bot = Bot(token='6058248417:AAGSwl13lmsfV-v4E9LA2MXY6ko3k9_bxms')
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="/motivashka")
        keyboard.add(button_1)
        await message.answer('Нажми "Мотивашка" чтобы получить картинку!', reply_markup=keyboard)

    @dp.message_handler(commands=['motivashka'])
    async def sendm(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="/motivashka")
        keyboard.add(button_1)
        path = str(randint(1, 10))+'.jpg'
        with open(path, 'rb') as m:
            await bot.send_photo(message.chat.id, m, reply_markup=keyboard)

    @dp.message_handler(content_types=['text'])
    async def sendrandtext(message: types.Message):
        path = "neboltai" + str(randint(1, 2)) + '.jpg'
        with open(path, 'rb') as m:
            await bot.send_photo(message.chat.id, m)

    executor.start_polling(dp)
