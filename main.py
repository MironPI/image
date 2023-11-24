import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Botni yaratish
bot = Bot(token="BOT_TOKEN")  # BOT_TOKEN o'rniga o'zingizning botningizning API kalitini yozing

# Dispatcher va xotira saqlashni o'rnatish
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Rasim yuborish uchun komanda
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Rasimni yuboring.")

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    # Rasimni olib olamiz
    photo = message.photo[-1].file_id
    # Rasim orqafonini olib tashlaymiz
    await bot.send_photo(message.chat.id, photo, caption="Rasimingiz qabul qilindi!")

if __name__ == '__main__':
    # Kodni boshlash
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
```
