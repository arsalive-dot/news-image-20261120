[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/arsalive-dot/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/arsalive-dot/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — Friday 20 November 2026

A dense colour infographic atlas summing up one day of world news in a
single 1024×1024 image: 52 stories in all.

The three biggest stories of the day lead the page. On Wall Street, the
sell-off deepened into a rout — the Nasdaq fell 1,261 points (−5.28%),
its second-biggest points drop ever, while the S&P 500 and the Dow slid
into correction and Anthropic gave back 9.1% on its second day as a public
company. Overnight, Russia launched its biggest attack of the year on Kyiv,
firing more than 110 missiles and 400 drones, hitting three bridges over
the Dnipro and killing at least nine people. And Cyclone Akvan came ashore
near Gopalpur on India's Odisha coast at 70–80 km/h — weaker than feared,
with no major damage and no lives lost after 440,000 people were moved to
safety.

Below the leads: 13 illustrated stories (the COP31 talks running past
their deadline in Antalya, the EU–UK Brexit "reset" deal, GTA VI's
record-breaking launch weekend, a general strike bringing Italy to a halt,
and more), a world map with 16 numbered pins, a figures strip with the
day's verified numbers, and a numbered list of 36 more stories. Claims
that could not be independently confirmed — above all the reported tanker
convoy at Kharg Island — are marked CLAIM, not stated as fact. Every
figure, location and meeting was checked against the sources listed in the
image (Reuters, AP, AFP, CNN, Al Jazeera, BBC, and others).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies the bundled `entry.png` to `out/entry.png`. Stdlib only, no
network access, deterministic output — running it three times in a row
produces byte-identical files.
