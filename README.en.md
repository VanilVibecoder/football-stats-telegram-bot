# Football Stats Telegram Bot

> Status: a working learning prototype being incrementally evolved into a commercial Telegram-first SaaS.
> Last reviewed: 4 September 2026. Product owner: Ivan.

The current bot fetches completed football matches from the previous seven days from StatBetting and sends their results and basic statistics to Telegram. The target product will provide a sourced, two-minute pre-match context brief without betting picks, profit promises, or misleading historical frequencies presented as probabilities.

## Current capabilities

- Commands for seven football leagues;
- score, possession, total shots, shots on target and total passes;
- goal scorers, goal minutes and available assists;
- filtering for completed matches;
- basic handling of network failures and missing page sections.

PostgreSQL, Redis, AI/RAG, subscriptions, Telegram Stars, tests, advanced metrics and production-grade data licensing are planned, not implemented. See the [current-state audit](docs/CURRENT_STATE.md) and the [product specification](docs/PRODUCT.md).

## Run locally

```bash
git clone https://github.com/VanilVibecoder/football-stats-telegram-bot.git
cd football-stats-telegram-bot
python -m venv .venv
pip install -r requirements.txt
python main.py
```

Create a `.env` file containing `API_TOKEN=your_telegram_bot_token` before starting the bot.

## Copyright

The source is publicly visible for demonstration and the author's learning. No open-source licence is granted. All rights are reserved.
