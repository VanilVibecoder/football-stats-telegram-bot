from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from scraper import get_matches_for_last_7_days
from formatter import formatter

router = Router()


leagues = {
    "england": {"season_id": 265, "name": "Premier League"},
    "england_2": {"season_id": 369, "name": "Championship"},
    "germany": {"season_id": 289, "name": "Bundesliga"},
    "italy": {"season_id": 341, "name": "Serie A"},
    "france": {"season_id": 349, "name": "Ligue 1"},
    "spain": {"season_id": 277, "name": "LALIGA"},
    "mls": {"season_id": 297, "name": "MLS"}
}

@router.message(Command(commands=leagues.keys()))
async def send_stat(message: types.Message, command: CommandObject):
    league = leagues[command.command]
    season_id = league['season_id']
    name_league = league['name']
    result = get_matches_for_last_7_days(season_id)
    if not result:
        return await message.answer(text='Завершенных матчей за последние 7 дней нет!\nВозможно команды на отдыхе или паузы на матчи сборных команд')
    else:
        await message.answer(text=f"{name_league} — матчи за последние 7 дней\n")
        for match in result:
            formatted_match = formatter(match)
            await message.answer(text=formatted_match,parse_mode="HTML")
    

