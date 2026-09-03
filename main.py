from aiogram import Bot, Dispatcher
from handler import router as handler_router
from start import router as start_router
import asyncio
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    raise ValueError("Ошбика: API_TOKEN не найден в файле .env!")
print("Токен успешно загружен!")


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(handler_router)
    dp.include_router(start_router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        time.sleep(1)
        print("Бот остановлен")

