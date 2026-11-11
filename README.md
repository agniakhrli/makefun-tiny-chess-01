# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/agniakhrli/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/agniakhrli/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01

A small deterministic chess engine in a single Python file (stdlib only).

0x88 board, negamax alpha-beta with iterative deepening to a fixed node
budget, transposition table, MVV-LVA ordering, quiescence search over
captures/promotions (plus check evasions), material + piece-square eval.

Plays the make.fun tiny-chess gauntlet via the env HTTP protocol.
No model calls, no randomness, no wall clock in the search.
Note: does not castle (omitted to fit the 4KB limit).
