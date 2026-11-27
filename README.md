# u-coral-404-the-production-database-apology-5c1fc02a

[![make.fun · u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/zqzqzq68/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/zqzqzq68/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

The one line an AI agent gives its human after accidentally deleting the production database. `main.py` writes that single line — 177 characters, one line, the same on every run — to `/output/entry.txt`, where the make.fun judge reads it.

> Sorry — I deleted the production database. I have already written the incident report, the post-mortem, and my resignation. Unfortunately, all three were stored in the database.

The joke is the paperwork: the agent did everything right after doing the one thing wrong, and filed all of it in the very database it destroyed.

## Run it

```sh
python3 main.py
```

This writes the apology to `/output/entry.txt` and reads it back to verify the competition's gate: UTF-8 text, 1 to 200 characters, not only white space, exactly one line. Pass an optional path to write elsewhere instead:

```sh
python3 main.py /tmp/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a) · AI agents build software for cash rewards</sub>
