# Minesweeper Game

This repo has two versions of a terminal-based Minesweeper game — one in **C++** and one in **Python**.

I started out writing the game in C++ to challenge myself with lower-level logic, especially managing the board manually and using random number generation. Later, I rewrote it in Python just to compare the two — and man, Python was so much simpler. Way less code, easier input handling, and overall faster to debug.

---

## What's Inside

- `minesweeper.cpp` – Original C++ version using `iostream`, `ctime`, and `<random>`
- `minesweeper2.py` – Rewritten Python version using `random` and `pyinputplus` for cleaner input

---

## How to Run

### C++ Version

**Dependencies:** Just a standard C++ compiler (like `g++`)

```bash
g++ minesweeper.cpp -o minesweeper
./minesweeper
```

**Libraries used:**
- `<iostream>` for basic input/output
- `<iomanip>` for formatting the board
- `<random>` and `<ctime>` for placing mines

---

### Python Version

**Dependencies:** Python 3 and `pyinputplus`

Install the required module:

```bash
pip install pyinputplus
```

Then run:

```bash
python3 minesweeper2.py
```

**Libraries used:**
- `random` for mine placement
- `pyinputplus` for validated user input

---

## Why Two Versions?

I wanted to see how different it feels to implement the same logic in two different languages. The C++ version required more setup, manual formatting, and care with logic and input. The Python version came together much faster with fewer lines of code, and `pyinputplus` made input handling way smoother.

That contrast really showed me how much language choice affects speed of development, even for the same project.



---

## License

MIT License — feel free to use or modify this project as you like.
