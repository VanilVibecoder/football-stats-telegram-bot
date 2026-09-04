# Roadmap на 24 недели

> Статус: рабочий порядок, даты меняются по gates, а не ради заполнения календаря. Владелец: Иван. Последняя проверка: 4 сентября 2026 года.

Темп: шесть фокус-сессий по 90 минут в неделю. Каждая фаза завершается работающим вертикальным срезом и демонстрацией, а не количеством написанных файлов.

## Недели 1–4 — управляемый прототип

- сохранить текущее поведение команд;
- определить Pydantic-модели Match, Team, Score, MatchStats, Goal и Evidence;
- отделить handler, application use case, provider и formatter;
- заменить синхронный `requests` на общий HTTPX AsyncClient;
- добавить fixture-тесты текущего HTML и обработку отсутствующих таблиц;
- собрать кликабельный Telegram flow на сохранённых данных.

Gate: Иван может объяснить полный путь input/output; один сломанный матч не ломает ответ; event loop не блокируется синхронной сетью.

## Недели 5–8 — постоянные данные

- PostgreSQL 16, SQLAlchemy 2, asyncpg и Alembic;
- стабильные внутренние IDs и provider mappings;
- upsert матчей, событий, статистики и evidence;
- repository interfaces и интеграционные тесты;
- JSON-логи, correlation ID, базовый Sentry;
- Docker Compose для локальной среды.

Gate: повторный импорт идемпотентен; данные переживают restart; миграции проходят с нуля и вперёд.

## Недели 9–12 — АПЛ и бесплатный разбор

- оценить лицензированных поставщиков и получить письменный ответ;
- первый промышленный ProviderAdapter для АПЛ;
- обязательное ядро: fixture, goals, xG, shots;
- deterministic окна last 5 и season baseline;
- карточка `Что важно сейчас`, sources и первый PNG-график;
- первые пять usability-сессий.

Gate: QA 50 матчей, completeness ≥95%, time-to-value ≤2 минут на модерируемом сценарии.

## Недели 13–16 — РПЛ, Redis и малые рынки

- добавить РПЛ через тот же контракт;
- CoverageProfile Basic/Deep;
- Redis cache/locks/rate limits/dedupe;
- APScheduler и снимки 24h/6h;
- угловые, карточки, судьи и лидеры/потери состава;
- закрытая alpha из десяти тестировщиков.

Gate: удаление Redis не теряет данные; повторная задача не создаёт дубликаты; Deep-блоки не появляются при неполном покрытии.

## Недели 17–20 — RAG-lite и изменения

- PostgreSQL full-text retrieval по выбранному матчу;
- benchmark 30 вопросов: основной AI-прокси против GigaChat fallback;
- схема ответа, numeric grounding и источники;
- `Получать изменения`, material-change diff и official-lineup snapshot;
- Free/Trial/Pro entitlements и product events;
- ещё пять usability-сессий и коррекция UX.

Gate: AI не публикует числа вне входных фактов; конфликт и недостаток данных видны; D7 можно посчитать событиями.

## Недели 21–24 — платная beta

- Basic Coverage для Ла Лиги, Серии A, Бундеслиги и Лиги 1;
- Basic Coverage для основной стадии/плей-офф ЛЧ;
- Telegram Stars: invoice, successful payment, ledger, expiry, renewal и refund;
- `/terms`, `/support`, `/paysupport`, privacy и 18+;
- Timeweb VPS, backup/restore drill и monitoring;
- тестовый вывод Stars после периода удержания;
- приглашение платной beta только после data/payment gates.

Gate: письменные права на данные, completeness ≥95%, восстановление из бэкапа, полный платёжный цикл и cash cap ≤5 000 ₽.

## Правила изменения roadmap

- функция входит в ближайшую фазу после пяти интервью или запроса ≥20% активных пользователей;
- Mini App рассматривается при запросе ≥30% активных;
- новая лига проходит demand/completeness/50-match gates;
- ручная операция >2 часов в неделю становится кандидатом на автоматизацию;
- при инфраструктуре и API >4 000 ₽ сужается покрытие до достижения общего cap 5 000 ₽;
- ML, live, другие виды спорта и компьютерное зрение не вытесняют beta gates.
