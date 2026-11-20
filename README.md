# news-image-20261120-entry

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/StarsN/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/StarsN/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

**The World in One Picture — Friday 20 November 2026.** A newspaper front page that sums up one day's world news in a single 1024×1024 image. The page is drawn programmatically with PIL at build time (`draw_entry.py`): every headline and paragraph is crisp vector type, so no text can come out garbled. The entrypoint (`main.py`) is a standard-library-only copier that delivers the committed `entry.png` byte-for-byte, so the two scoring runs are identical by construction.

The day's stories, each cross-checked against that day's reporting (One Turn's daily brief, SCMP, Dawn, Fox News, VGC/Sensor Tower): the World Court rules Myanmar committed genocide against the Rohingya; Trump, Xi and Putin close their first three-way summit in Shenzhen with a peace declaration; AI doubts drag world stocks lower (Nikkei -4.8%); Houthi missiles damage Riyadh's wealth-fund tower as Hormuz tanker attacks intensify; a Russian barrage damages two embassies in Kyiv; COP31 strips the fossil-fuel phase-out from its draft; Kenya discharges its last Ebola patient; and GTA 6 earns an estimated $2.36bn in its first day, an entertainment record.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`). Requires Python 3.13, standard library only; no network. To redraw the page itself, run `MAKEFUN_OUTPUT_DIR=. python3 draw_entry.py` — the generator is the one that needs Pillow.

## How the front page is composed

The page is laid out top to bottom in five bands, and every band's height is measured from the wrapped text before anything is drawn, so blocks can never overlap:

1. **Masthead** — the title in bold serif between rules, with the dateline and the two side labels on one line.
2. **Lead story** — the day's biggest ruling, with a hand-drawn scales-of-justice glyph panel captioned with the court and city.
3. **Two-column row** — the Shenzhen summit beside the markets sell-off, each with a coloured kicker, serif headline and short body.
4. **Three cards** — Riyadh, Kyiv and COP31 in bordered boxes with a colour strip on top; all three share one height, taken from the longest headline and body.
5. **Closing briefs and ticker** — Kenya health and the GTA 6 launch record side by side, above a black ticker bar whose items are dropped one by one until the line fits the page width.

Type is set with tight display leading on the headlines and looser leading on body copy, in the ratios a printed front page uses; the closing briefs are set slightly tighter still so the page ends with clear air above the ticker.

## Verifying the entry

Run the entrypoint twice into two different directories and compare hashes — the output must be byte-identical to the committed `entry.png`, 1024×1024 and under 1 MiB:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/b python3 main.py
sha256sum /tmp/a/entry.png /tmp/b/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=vvry49c9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
