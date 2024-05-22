from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import executor  # Измененный импорт

# Ваш токен от BotFather
TOKEN = '6858266857:AAFW2qM48sK3YoC_HEyD-rzNVQ_3ln3e5sw'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Open Web App", url="https://your-domain.com/webapp"))

    await message.answer("Click the button below to open the Web App:", reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
