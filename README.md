# ⚽ Football Stats Telegram Bot

A Telegram bot that provides recent football match results and detailed match statistics directly in Telegram.

The bot collects data for completed matches from the last 7 days, processes it with Python, and sends the results in a clean and readable format.

## ✅ Current Features

- Match results from the last 7 days
- Ball possession
- Total shots
- Shots on target
- Total passes
- Goal scorers and goal minutes
- Assists
- Automatic filtering of unfinished matches
- Handling of matches with missing statistics
- Support for multiple football leagues
- Telegram commands for quick league selection

## 🌍 Supported Leagues

- `/england` — Premier League
- `/england_2` — Championship
- `/spain` — LaLiga
- `/italy` — Serie A
- `/germany` — Bundesliga
- `/france` — Ligue 1
- `/mls` — MLS

## 🚧 Roadmap

Planned improvements for future versions:

- xG (Expected Goals) statistics
- Advanced match statistics from additional football data sources
- More detailed shot data
- Additional leagues and competitions
- Faster and fully asynchronous data fetching
- Automated tests
- Improved error handling and reliability
- Better Telegram user experience
- Match selection and navigation improvements
- Deployment for 24/7 public access


## 🛠 Tech Stack

- Python 3
- aiogram 3
- requests
- BeautifulSoup4
- lxml
- python-dotenv
- Telegram Bot API

Match data is currently collected from StatBetting.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/VanilVibecoder/football-stats-telegram-bot.git
cd football-stats-telegram-bot


## 📌 Project Status

**MVP — working version**

The core functionality is complete and the bot can already fetch, process, format, and display real match statistics.

The next stage is deployment, testing with real users, collecting feedback, and gradually adding advanced football analytics.