from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer(text=(
        "Привет!👋\n\nЯ показываю результаты и статистику\nзавершенных матчей за последние 7 дней.\nДоступные команды:\n\n"
        "/england — Premier League\n"
        "/england_2 — Championship\n"
        "/spain — LaLiga\n"
        "/italy — Serie A\n"
        "/germany — Bundesliga\n"
        "/france — Ligue 1\n"
        "/mls — MLS\n"
        )
    )