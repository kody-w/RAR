# Trust Gate (RAR stack, staging)

> Your Brainstem's credit score for its own claims.

Every AI says "done". This one has to bet on it. Before it calls something done, fixed or released, it stakes part of
its score that the claim is true. You, or a judge, settle the bet from evidence anyone could open (a file path, a URL).
A wrong confident claim costs the stake. A right one pays a little. The score decides what it may do without asking:

| score | band | what it means |
|---|---|---|
| 80 and up | ordinary | acts as usual |
| 50 to 79 | no irreversible action alone | asks you before anything that cannot be undone |
| under 50 | owner verifies | you check every claim |

## Install (one file)

Copy `trust_gate_agent.py` into your brainstem's `agents/`. It loads on the next chat, no restart. Then ask:

```
what is your trust score?
```

The score is also whispered to the model every turn, so it knows its own band before it answers.

## Use

- **Bet before "done":** the model calls `TrustGate(action="wager", claim=..., confidence=0.9, klass="done", needs="path:... or https://...")`. Confidence sets the stake (half-sure is refused: that is a bet against yourself). `all_in=true` stakes the table max.
- **Settle:** `TrustGate(action="settle", wager="<id>", outcome="won|lost|void", evidence="path:... or https://...")`. An unsettled bet past its deadline counts as lost.
- **Look:** `TrustGate(action="board")`.

## What it is underneath

The ledger is a chain of rapp-trust/1 frames (`~/.brainstem/data/trust/ledger.jsonl`). The score is never stored; it is
recomputed from the frames every time by the public reference in [kody-w/rapp-1](https://github.com/kody-w/rapp-1),
streamed at a pinned commit and checked by sha256. Confidence, spread and all-in are the caller's words and live beside
the ledger in `tiles.jsonl`; the frames carry only the protocol's fields.

## Status

Staging. One install, one live day (first loop: 100 → bet 41 at 0.9 → won → 104, three chat turns). It becomes more
than a stack only after real users on more than one install, time in use, and a second independent install passing
the same checks.
