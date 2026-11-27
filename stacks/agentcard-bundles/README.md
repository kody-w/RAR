# Agent card bundles (status: staging)

Some agents import a package a phone's Python does not have. This stack builds one `.agentcard` for each of them
that **carries what it needs inside the card**: pure-Python wheels and sibling agent files, each fingerprinted.
The person still adds one file, exactly like a bare `agent.py`; nothing is fetched separately.

- `bundle_card.py`: one agent in, one card out (plus a report of what was carried and what could not be).
- `build_bundles.py`: every agent in `registry.json` that needs something extra; writes `cards/` and `index.json`.
- `vendor/`: the card format and the phone host's loader (copied from the Hive app; the card's checks live there).
- `build_registry.py` adds `_agentcard` and `_agentcard_sha256` to an agent's registry entry when its card exists.

Rules (lessons paid for by others):
- **Pure Python only.** Compiled packages cannot run on a phone; a wheel must end `-none-any.whl` and contain no
  native files. Agents that need compiled code to start are listed in `index.json` as not for iPhone.
- **No guessed package names.** Packages come only from the reviewed `KNOWN` list in `bundle_card.py` or from the
  agent's own PEP 723 block (`# /// script` / `dependencies = [...]`). Guessing from an import name is how
  dependency-confusion attacks get in (Birsan, 2021).
- **Untrusted code gets no write token.** CI bundles in a read-only job; a second job checks the cards without
  running them and commits.
- **Optional stays optional.** An import inside `try/except ImportError` or inside a function is carried when
  pure, skipped when compiled; only a module-level import that cannot be carried blocks a card.

Declare what your agent needs (optional, PEP 723):

```python
# /// script
# dependencies = ["pypdf>=5"]
# ///
```
