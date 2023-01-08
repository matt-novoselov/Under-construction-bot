from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    with open('image.webp', 'rb') as photo:
        await message.answer_document(photo)
    await message.answer("Sorry, the bot is under construction. Check back later")


if __name__ == '__main__':
    executor.start_polling(dp)
