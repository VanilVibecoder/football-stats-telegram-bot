import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta

headers = {
        "accept":"*/*",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
            }




def get_matches_for_last_7_days(season_id: int):
    all_matches = []
    for day in get_last_7_days():
        matches_for_day = get_matches_for_day(url=f"https://statbetting.com/fixtures?season={season_id}&date={day}")
        print(day)
        print(len(matches_for_day))
        all_matches.extend(matches_for_day)

    completed_matches = []

    for match in all_matches:
        stats = parse_match_stat(match["stats_url"])
        if not stats:
            continue
        match.update(stats)
        completed_matches.append(match)

    return completed_matches




def get_last_7_days():
    days = []
    today = date.today()
    for i in range(7):
        current_date = today - timedelta(days=i)
        days.append(current_date.isoformat())
    return days



def get_matches_for_day(url: str) -> list[dict]:
    try:
        matches_for_day = []
        response = requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,"lxml")

    # СЕРВЕР НЕ ОТВЕТИЛ ЗА 3 СЕК
    except requests.exceptions.Timeout:
        print("Превышено время ожидания от сервера (Timeout)")
        return []

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: Проблема на строне сервера или неверный url ({http_err})")
        return []


    # НЕТ СЕТИ
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения: Проверьте подключение к интернету или доступность сайта")
        return []

    # ВСЕ ОШИБКИ REQUESTS
    except requests.exceptions.RequestException as err:
        print(f"Произошла непредвиденная сетевая ошибка: {err}")
        return []

    main_block = soup.find("div",class_='col-12 col-lg-9')
    if not main_block:
        return []
    fixtures_block = main_block.find('div',class_='table-responsive fixtures-table-wrapper')
    if not fixtures_block:
        return []
        
        
    table = soup.find("div", class_="col-12 col-lg-9").find("div", class_="table-responsive fixtures-table-wrapper").find("table",class_="table table-hover table-striped table-compact table-sticky mb-0 align-middle")
        
    matches = table.find_all('tr',class_="clickable-row")
        
        
    for match in matches:
        full_match = {}
        teams = match.find_all('td',class_='team-name-cell')
        score_element = match.find('span', class_='badge')
        if score_element:
            score = score_element.text.strip()
        else:
            continue
        full_match["home_team"] = teams[0].text.strip()
        full_match["score"] = score
        full_match["away_team"] = teams[1].text.strip()


        stats_url = match.get('data-href')
        full_match["stats_url"] = stats_url

        matches_for_day.append(full_match)

    return matches_for_day



def parse_match_stat(stats_url: str) -> dict:
        match_stats = {}
        try:
            response_every_match_url_stats = requests.get(stats_url,headers=headers, timeout=10)
            response_every_match_url_stats.raise_for_status()
            stats_url_soup = BeautifulSoup(response_every_match_url_stats.text,"lxml")
        except requests.exceptions.Timeout:
            print("Превышено время ожидания от сервера (Timeout)")
            return {}

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP ошибка: Проблема на строне сервера или неверный url ({http_err})")
            return {}

        except requests.exceptions.ConnectionError:
            print("Ошибка соединения: Проверьте подключение к интернету или доступность сайта")
            return {}

        except requests.exceptions.RequestException as err:
            print(f"Произошла непредвиденная сетевая ошибка: {err}")
            return {}
            


        full_time = stats_url_soup.find('div',class_='kpi-label-enhanced')
        if not full_time or full_time.text != "Full Time":
            return {}

        stat_rows = stats_url_soup.find_all('div', class_='stat-row')

        home_possession = None
        away_possession = None
        home_shot_attempts = None
        away_shot_attempts = None
        home_shot_on_goal = None
        away_shot_on_goal = None
        home_total_passes = None
        away_total_passes = None

        for row in stat_rows:
            label = row.find('div',class_='stat-label')
            if not label: 
                continue
            label_text = label.text.strip()

            if label_text == "Shot Attempts":
                shot_attempts_row = row

                shot_attempts_values = shot_attempts_row.find_all('div',class_='stat-value')
                home_shot_attempts = shot_attempts_values[0].text.strip()
                away_shot_attempts = shot_attempts_values[1].text.strip()
            elif label_text == "Possession":
                possesion_row = row 

                possesion_values = possesion_row.find_all('div',class_='stat-value')
                home_possession = possesion_values[0].text.strip()
                away_possession = possesion_values[1].text.strip()

            elif label_text == "Shots on Goal":
                shots_on_goal_row = row

                shots_on_goal_values = shots_on_goal_row.find_all('div',class_='stat-value')
                home_shot_on_goal = shots_on_goal_values[0].text.strip()
                away_shot_on_goal = shots_on_goal_values[1].text.strip()

            elif label_text == "Total Passes":
                total_passes_row = row

                total_passes_values = total_passes_row.find_all('div',class_='stat-value')
                home_total_passes = total_passes_values[0].text.strip()
                away_total_passes = total_passes_values[1].text.strip()


        match_stats["home_possession"] = home_possession
        match_stats["away_possession"] = away_possession
        match_stats["home_shot_attempts"] = home_shot_attempts
        match_stats["away_shot_attempts"] = away_shot_attempts
        match_stats["home_shot_on_goal"] = home_shot_on_goal
        match_stats["away_shot_on_goal"] = away_shot_on_goal
        match_stats["home_total_passes"] = home_total_passes
        match_stats["away_total_passes"] = away_total_passes





        # ГОЛЫ ХОЗЯЕВ
        home_container = stats_url_soup.find('div',class_='match-event-list match-event-list--home')
        goals_home_team = []
        if home_container:
            match_events_home_team = home_container.find_all('div',class_='match-event-line match-event-line--home')
            for event in match_events_home_team:
                goal_home = event.find('span',class_='match-event-icon goal')
                if goal_home:
                    spans = event.find_all('span')
                    name = spans[2].text.strip()
                    minute = spans[3].text.strip()

                    one_goal_home = {"name":name, "minute":minute}
                    goals_home_team.append(one_goal_home)
            
            

        match_stats["goals_home_team"] = goals_home_team
        


        # ГОЛЫ ГОСТЕЙ
        goals_away_team = []
        away_container = stats_url_soup.find("div",class_="match-event-list--away")
        if away_container:
            match_events_away_team = away_container.find_all(
            "div",
            class_="match-event-line"
        )

            
            for event_1 in match_events_away_team:
                goal_away = event_1.find('span',class_='match-event-icon goal')
                if goal_away:
                    spans = event_1.find_all('span')
                    name_away = spans[2].text.strip()
                    minute_away = spans[3].text.strip()

                    one_goal_away = {"name":name_away, "minute":minute_away}
                    goals_away_team.append(one_goal_away)


        match_stats["goals_away_team"] = goals_away_team



        # АССИСТЫ хозяев
        match_events_home_team_table = stats_url_soup.find_all('div',class_='card border mb-4 shadow-sm player-stats-card')[0] # первая таблица = таблица хозяев
        tr_rows_home = match_events_home_team_table.find_all('tr')

        assists_home_team = []
        for row in tr_rows_home:
            cells = row.find_all('td')

            if len(cells) >= 6:
                player_name_home = cells[1].text.strip()
                assists_home = cells[5].text.strip()

                if int(assists_home) > 0:
                    assists_home_team.append({"assist_home_team_player_name":player_name_home,"quantity_of_assists_home":int(assists_home)})


        match_stats["assists_home_team"] = assists_home_team

        # АССИСТЫ гостей
        match_events_away_team_table = stats_url_soup.find_all('div',class_='card border mb-4 shadow-sm player-stats-card')[1]
        tr_rows_away = match_events_away_team_table.find_all('tr')

        assists_away_team = []
        for row in tr_rows_away:
            cells = row.find_all('td')

            if len(cells) >= 6:
                player_name_away = cells[1].text.strip()
                assists_away = cells[5].text.strip()

                if int(assists_away) > 0:
                    assists_away_team.append({"assist_away_team_player_name":player_name_away, "quantity_of_assists_away":int(assists_away)})

        match_stats["assists_away_team"] = assists_away_team

        return match_stats