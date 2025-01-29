import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

# Отримання токена з оточення (Render Secrets)
TOKEN = os.getenv("TOKEN")

# Переконайся, що токен заданий
if not TOKEN:
    raise ValueError("❌ Не задано TOKEN для бота!")

# Ініціалізація бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Логування
logging.basicConfig(level=logging.INFO)

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привіт! Я твій персональний бот для ставок. Введи /help, щоб побачити команди.")

# Команда /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Команди:\n/analyze - Отримати аналітику\n/settings - Налаштування бота\n/watch - Стежити за гравцем")

# Команда /analyze
@dp.message(Command("analyze"))
async def analyze_command(message: types.Message):
    await message.answer("🔍 Аналіз ставок: \n🏀 Lakers - Warriors, Тотал 230.5 більше ✅ 87%\n⚽ Real - Barca, 1X ✅ 75%")

# Функція запуску бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
