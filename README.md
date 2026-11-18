# The World in One Picture — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/jojosinkonstanor-collab/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/jojosinkonstanor-collab/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One image that sums up the world's news of **Wednesday, 18 November 2026** —
a newspaper front page drawn entirely with Pillow (Python), so every word is
sharp and exactly as written. No AI-generated text anywhere in the image.

## The six stories

1. **Lead — Quad summit in Manila:** Trump and Modi give the Quad a new
   strategic direction; Quad leaders announce a new maritime exercise and
   joint AI and cybersecurity initiatives.
2. **Tech — Nvidia:** beats estimates in its first earnings report without
   Jensen Huang; the board rules out his return as CEO.
3. **Disaster — Russia:** a military transport plane crashes in Siberia,
   19 killed.
4. **Courts — United States:** a Pakistani man is jailed for 27 years over
   an Iran-backed plot to assassinate Donald Trump.
5. **Politics — Israel:** parliament elects Matan Kahana, an ally of
   Eisenkot, as speaker — a blow for Netanyahu.
6. **Health — United States:** the US loses its measles-free status as
   cases and deaths mount.

## How it works

`main.py` (Python 3.13, standard library only) copies `asset/entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). The image is
1024×1024 px, PNG, well under the 1 MiB limit, and every run writes
byte-identical output. `draw.py` (kept out of the submitted snapshot's
critical path; the PNG it produces is the shipped asset) renders the page
with Pillow: masthead, date line, six panels with category tags, headlines,
one line of context each, and flat geometric icons drawn with PIL shapes.

## Verify locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "from PIL import Image; im = Image.open('out/entry.png'); print(im.size)"
```

Run it twice and compare checksums — the bytes are identical.

---

Built for the [make.fun bounty: Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118).
