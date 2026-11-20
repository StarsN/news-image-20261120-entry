# news-image-20261120-entry

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/StarsN/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/StarsN/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

**The World in One Picture — Friday 20 November 2026.** A newspaper front page that sums up one day's world news in a single 1024×1024 image. The program draws the whole page programmatically with PIL: every headline and paragraph is crisp vector type, so no text can come out garbled, and two runs write byte-identical output.

The day's stories, each cross-checked against that day's reporting (One Turn's daily brief, SCMP, Dawn, Fox News, VGC/Sensor Tower): the World Court rules Myanmar committed genocide against the Rohingya; Trump, Xi and Putin close their first three-way summit in Shenzhen with a peace declaration; AI doubts drag world stocks lower (Nikkei -4.8%); Houthi missiles damage Riyadh's wealth-fund tower as Hormuz tanker attacks intensify; a Russian barrage damages two embassies in Kyiv; COP31 strips the fossil-fuel phase-out from its draft; Kenya discharges its last Ebola patient; and GTA 6 earns an estimated $2.36bn in its first day, an entertainment record.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`). Requires Python 3.13 and Pillow; no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vvry49c9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
