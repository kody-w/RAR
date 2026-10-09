# The RAPP incubator

Eggs for the Brainstem, ready to unwrap. Each egg is one file that holds a complete Brainstem: the engine, its
personality, its abilities, and the rules it checks itself against. Unwrap one in the **Hatch Brainstem** app, or with
`python3 <file>.egg`.

- **Index:** [`index.json`](index.json) (`rapp-incubator/1.0`), also at
  `https://kody-w.github.io/RAR/incubator/index.json`
- **Eggs:** `eggs/<slug>/<sha12>.egg`, named by their SHA-256. A published egg file never changes; a new version is
  a new file.

## Share an egg

1. In the Hatch Brainstem app, open **More → Wrap it back up**, or build one with `build_egg.py`.
2. Add the egg as `incubator/eggs/<slug>/<first 12 hex of its sha256>.egg`.
3. Add `incubator/entries/<slug>.json`:
   ```json
   {"slug": "my-egg", "title": "My Egg", "description": "One sentence.", "author": "you",
    "tags": ["work"], "egg": "eggs/my-egg/0123456789ab.egg"}
   ```
4. Run `python3 incubator/build_incubator.py` and open a pull request. CI runs `--check`: every egg must pass
   rapp/1 egg verification, the index must be current, and published eggs must be unchanged.

Eggs must contain no secrets, keys or personal data.
