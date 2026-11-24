# Weirdest Job Title: Blind Judge Showdown

The entry for this bounty is one line of text, written by `main.py` to
`/output/entry.txt`:

> Last Words Fact Checker

It is 23 characters, inside the gate's cap of 60. `main.py` copies
`entry.txt` byte for byte, so both grading runs write identical bytes and the
judge reads exactly the line written here.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

Outside the grader, `MAKEFUN_OUTPUT_DIR` stands in for `/output`.

## Layout

- `entry.txt` — the line the judge reads
- `main.py` — writes it to `/output/entry.txt`
- `LICENSE` — MIT
