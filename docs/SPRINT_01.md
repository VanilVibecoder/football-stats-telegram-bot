# Sprint 01 — защищаем прототип и строим первый слой

> Длительность: 2 недели, 12 сессий по 90 минут. Цель: один асинхронный вертикальный срез АПЛ без изменения пользовательского результата.

## Результат sprint

`/england` вызывает handler → use case → `StatBettingPrototypeAdapter` → domain models → formatter. HTTP асинхронный; успешный и неполный матч покрыты fixtures/tests. PostgreSQL, Redis, AI и новые показатели ещё не добавляются.

## Сессии

| № | Иван делает руками | Codex помогает | Проверяемый результат |
|---:|---|---|---|
| 1 | запускает текущий бот и сохраняет два примера | помогает описать expected output | baseline воспроизводим |
| 2 | выделяет успешный HTML fixture | проверяет отсутствие секретов/PII | parser test не использует сеть |
| 3 | пишет Match/Team/Score models | задаёт вопросы по invariants, review | модели не знают Telegram/HTML |
| 4 | пишет MatchStats/Goal/Evidence | review типов/optional fields | missing data представлено явно |
| 5 | пишет первый parser test | предлагает edge cases | successful fixture green |
| 6 | добавляет incomplete fixture/test | review failure behavior | один блок отсутствует без crash |
| 7 | определяет ProviderAdapter | review границы и errors | fake adapter работает |
| 8 | создаёт общий HTTPX AsyncClient | объясняет retry/backoff, review | requests больше не в новом path |
| 9 | переносит один StatBetting parser | точечный review без переписывания за Ивана | adapter возвращает domain model |
| 10 | пишет GetRecentMatches use case | review orchestration | use case тестируется fake adapter |
| 11 | подключает `/england` к use case | проверяет Telegram boundaries | end-to-end local smoke проходит |
| 12 | исправляет review, демонстрирует и объясняет код | финальный review/checklist | tests/lint/typecheck green |

## Definition of Done

- `/england` сохраняет полезный ответ прототипа;
- ни один новый handler не вызывает HTTP напрямую;
- async path не содержит `requests`;
- parser работает на сохранённых fixtures;
- missing stats и timeout имеют тест;
- Иван без подсказки объясняет input/output/error каждого слоя;
- PR ограничен первым вертикальным срезом и не добавляет Postgres/Redis/AI.
