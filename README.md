# Who Dies First?

A horror film you cast yourself, then a look at what Hollywood really did with its Black characters.

You cast six made-up actors into five classic horror roles, decide who dies, and then see how your film compares with 27 real horror films from 1968 to 2025.

**Play it:** https://georgiajayy.github.io/black-horror-1968-2025/

## What the data says

- **Who dies first:** before *Get Out* (2017), the first named victim was Black in 3 of 14 films (*The Shining*, *Candyman*, *Scream 2*). After, it happened in 4 of 10, and all four were Black-led films.
- **Who survives:** before 2017, 9 of 22 Black main characters survived. After, 26 of 35 did.

## Data

- `data/films.csv`: one row per film, with its first named victim.
- `data/black_characters.csv`: one row per Black main character, with their fate.

Everything was logged by hand from each film's Wikipedia plot summary (linked in `films.csv`). Villains and monsters aren't counted as victims. The films are a hand-picked set, not a random sample.

## Build

`python3 src/build.py` puts the CSV data into `src/template.html` and writes `index.html`.

Fonts are UnifrakturMaguntia, Alegreya, Alfa Slab One and Courier Prime, all under the SIL Open Font License (see `assets/fonts`).

Made by Georgia Jayy for Black History Month, October 2026.
