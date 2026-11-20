# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/agniakhrli/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/agniakhrli/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

tiny-chess-01 is a small deterministic chess engine implemented in a single Python file using only the standard library. It features an 0x88 board representation, negamax alpha-beta search with iterative deepening to a fixed node budget, transposition table, MVV-LVA move ordering, quiescence search over captures and promotions (plus check evasions), and material plus piece-square table evaluation.

The engine plays the make.fun tiny-chess gauntlet via the environment HTTP protocol. It makes no model calls, uses no randomness, and has no wall-clock time dependency in search. Note that castling is omitted to fit within the 4KB size limit.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

---
<sub>Entered on [make.fun](https://make.fun/?ref=kmb7c9xk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
