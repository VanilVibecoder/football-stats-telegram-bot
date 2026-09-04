# Технический backlog

> Статус: исполнимая очередь после blueprint. Владелец продукта: Иван. `Иван` пишет первый критический пример; `Codex` объясняет, ревьюит, тестирует и масштабирует уже понятый паттерн.

## Как выполняется каждая задача

```text
поведение и DoD
  -> Иван объясняет input/output/errors
  -> код маленьким вертикальным срезом
  -> unit/contract test
  -> Codex review
  -> исправления Иваном
  -> integration/smoke test
  -> merge
```

Задача не `Done`, если код работает только вручную, Иван не может его объяснить или отсутствует проверка ошибки.

## T0 — Защитить существующий прототип

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T0.1 | Сохранить HTML fixtures двух успешных и двух неполных матчей | Иван | — | fixtures обезличены, источник/дата записаны |
| T0.2 | Characterization tests для `formatter` и parser | Иван + Codex | T0.1 | текущее полезное поведение зафиксировано |
| T0.3 | Review хрупких индексов/селекторов | Codex | T0.2 | список failure cases превращён в tests |
| T0.4 | CI: Ruff + Pyright + pytest | Codex, Иван разбирает | T0.2 | checks запускаются на каждый PR |

## T1 — Первый вертикальный срез архитектуры

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T1.1 | Pydantic-модели Match, Team, Score, MatchStats, Goal, Evidence | Иван | T0 | нет transport/HTML полей в domain |
| T1.2 | Интерфейс ProviderAdapter и типизированные ошибки | Иван | T1.1 | fake adapter проходит application test |
| T1.3 | Async HTTP client с timeout/retry/rate limit | Иван, review Codex | T1.2 | event loop не блокируется; 429/5xx tested |
| T1.4 | StatBettingPrototypeAdapter | Иван | T1.3 | HTML превращается в domain model, а не Telegram text |
| T1.5 | GetRecentMatches use case | Иван | T1.4 | handler вызывает один application interface |
| T1.6 | Новый handler/formatter поверх use case | Иван + Codex | T1.5 | команды сохраняют поведение без прямого HTTP |

## T2 — PostgreSQL и идемпотентный импорт

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T2.1 | Docker Compose: app/Postgres/Redis | Codex, разбор Иваном | T1 | healthchecks и `.env.example`, без secrets |
| T2.2 | Схема competitions/teams/matches/provider mappings/evidence | Иван | T1.1 | constraints и ownership объяснены |
| T2.3 | Alembic initial migration | Иван + Codex review | T2.2 | upgrade с нуля и downgrade tested |
| T2.4 | Repository interfaces и SQLAlchemy implementation | Иван | T2.3 | integration tests на реальном Postgres |
| T2.5 | Идемпотентный import job | Иван | T2.4 | двойной запуск не создаёт дубликаты |

## T3 — Лицензированный feed и качество

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T3.1 | Письменный use-case запрос API-Football/Sportmonks | Иван | — | ответ сохранён приватно; paid-display разрешён/отклонён |
| T3.2 | Coverage matrix АПЛ/РПЛ/top-5/ЛЧ | Иван + Codex | T3.1 | обязательные и optional metrics отмечены |
| T3.3 | Первый licensed ProviderAdapter для АПЛ | Иван | T1.2,T3.1 | contract tests и stable mappings |
| T3.4 | QA 50 матчей | Иван | T3.3 | ≥95% core completeness, mismatch log |
| T3.5 | РПЛ и Basic-лиги через тот же adapter | Codex после примера | T3.4 | нет fork parser per league; coverage explicit |

## T4 — Telegram UX и разбор матча

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T4.1 | Callback schema и navigation state | Иван | T1.5 | повтор callback безопасен, `Назад` работает |
| T4.2 | Меню `Матчи · Мои · Профиль` | Иван + Codex | T4.1 | путь `/start → матч` ≤3 действий |
| T4.3 | Детерминированный MatchBrief last5 | Иван | T2,T3 | facts содержат sample/evidence/confidence |
| T4.4 | Рендер `Что важно сейчас` и вкладок | Иван | T4.3 | соответствует `TELEGRAM_UX.md` |
| T4.5 | Message splitting/loading/error states | Codex | T4.4 | лимиты Telegram и provider failures tested |
| T4.6 | PNG trend/minute graph | Иван + Codex | T4.3 | подписи читаемы на телефоне; no-data path |

## T5 — Deep statistics, Redis и scheduler

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T5.1 | Окна 5/10/20, дом/выезд, competition/season split | Иван | T4.3 | fixtures покрывают early/promoted/UCL cases |
| T5.2 | Угловые for/against и интервалы | Иван | T5.1 | definition/sample documented and tested |
| T5.3 | Referee/cards current + 2 seasons + last5 | Иван | T5.1 | малая выборка снижает confidence |
| T5.4 | Player leaders/losses | Иван | T3 | per90 всегда вместе с minutes/sample |
| T5.5 | Redis cache/locks/counters/dedupe | Codex после правил Ивана | T2 | удаление Redis не теряет truth |
| T5.6 | Scheduler snapshots 24h/6h/lineup | Иван + Codex | T5.5 | restart/double run не дублирует update |

## T6 — RAG-lite и AI

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T6.1 | Fact/evidence retrieval выбранного match_id | Иван | T4.3 | чужие матчи не попадают в context |
| T6.2 | Benchmark 30 вопросов: template/proxy/GigaChat | Иван + Codex | T6.1 | usefulness/grounding/latency/cost таблица |
| T6.3 | LLM gateway + fallback + schema validation | Иван | T6.2 | provider switch не меняет domain contract |
| T6.4 | Numeric grounding | Codex, review Иваном | T6.3 | число вне input блокирует LLM answer |
| T6.5 | Consent, redaction и 30-day retention | Иван | T6.3 | Telegram/payment PII не уходит наружу |

## T7 — Free, Trial, Pro и Stars

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T7.1 | Entitlements и дневные limits | Иван | T2 | Free/Trial/Pro table-driven tests |
| T7.2 | SubscriptionLedger | Иван | T7.1 | payment access не хранится одним boolean |
| T7.3 | Invoice 399 XTR + successful_payment | Иван + Codex review | T7.2 | duplicate update не продлевает дважды |
| T7.4 | Expiry/renewal/refund/support commands | Иван | T7.3 | полный Telegram test flow пройден |
| T7.5 | Hold/Fragment/TON withdrawal drill | Иван | T7.4 | реальный вывод подтверждён до публичной продажи |

## T8 — Review, security и release QA

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T8.1 | Architecture review против ADR | Codex | T1–T7 | нарушения границ исправлены/записаны новым ADR |
| T8.2 | Secret/PII/logging review | Иван + Codex | T6,T7 | secrets absent, redacted structured logs |
| T8.3 | Full regression matrix | Codex, исправляет Иван | T7 | Free/Trial/Pro/data/payment cases green |
| T8.4 | Manual QA 10 пользователей | Иван | T4–T7 | issues classified by severity/frequency |

## T9 — Deploy и эксплуатация

| ID | Задача | Владелец | Зависит | Definition of Done |
|---|---|---|---|---|
| T9.1 | Production Docker images и config | Codex, разбор Иваном | T8 | reproducible build; non-root where practical |
| T9.2 | Timeweb VPS firewall/secrets/TLS | Иван + Codex checklist | T9.1 | only required ports; token outside repo |
| T9.3 | Backup и restore drill | Иван | T2,T9.2 | новая БД восстановлена и проверена |
| T9.4 | Monitoring/runbook/alerts | Codex | T9.2 | provider freshness, errors, disk, backup visible |
| T9.5 | Staged release alpha → paid beta | Иван | all gates | rollback documented; cash cap enforced |

## Merge gates

- изменение domain formula: unit tests + sample explanation;
- provider change: contract fixture + coverage diff;
- schema change: migration forward/back test;
- Telegram change: callback and message-limit tests;
- AI change: 30-question benchmark subset + numeric grounding;
- payment change: idempotency/refund tests;
- deployment change: healthcheck + rollback note.
