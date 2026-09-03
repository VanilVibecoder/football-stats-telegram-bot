
def formatter(match: dict) -> str:
    full_text = ''
    block_of_stat = (
    f"⚽ {match['home_team']} {match['score']} {match['away_team']}\n\n"
    "📊 Статистика\n"
    f"Владение: <b>{match['home_possession']}</b> - <b>{match['away_possession']}</b>\n"
    f"Удары: <b>{match['home_shot_attempts']}</b> - <b>{match['away_shot_attempts']}</b>\n"
    f"В створ: <b>{match['home_shot_on_goal']}</b> - <b>{match['away_shot_on_goal']}</b>\n"
    f"Передачи: <b>{match['home_total_passes']}</b> - <b>{match['away_total_passes']}</b>\n\n"
    )

    full_text += block_of_stat

    #ГОЛЫ
    block_of_goals = ''

    block_of_goals += f"🎯 {match['home_team']}\n"
    if match['goals_home_team']:
        for goal_home in match['goals_home_team']:
            block_of_goals += f"{goal_home['minute']} {goal_home['name']}\n"
    else:
        block_of_goals += "Нет голов\n"


    block_of_goals += f"\n🎯 {match['away_team']}\n"
    if match['goals_away_team']:
        for goal_away in match['goals_away_team']:
            block_of_goals += f"{goal_away['minute']} {goal_away['name']}\n"
    else:
        block_of_goals += "Нет голов\n"


    full_text += block_of_goals


    block_of_assists = ''

    block_of_assists += f"\n🅰️ {match['home_team']}\n"
    if match['assists_home_team']:
        for assist_home in match['assists_home_team']:
            block_of_assists += f"{assist_home['assist_home_team_player_name']} - {assist_home['quantity_of_assists_home']}\n"
    else:
        block_of_assists += "Нет ассистов\n"


    block_of_assists += f"\n🅰️ {match['away_team']}\n"
    if match['assists_away_team']:
        for assist_away in match['assists_away_team']:
            block_of_assists += f"{assist_away['assist_away_team_player_name']} - {assist_away['quantity_of_assists_away']}\n"
    else:
        block_of_assists += "Нет ассистов\n"


    full_text += block_of_assists

    return full_text
