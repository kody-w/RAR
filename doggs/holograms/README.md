# Hologram DOGGs

These records are public, static behavior/data objects for the RAPP Zoo
hologram renderer. They are deliberately **not executable HTML**:

- RAR stores each character or projection definition as JSON.
- `index.json` publishes the expected SHA-256 for every record.
- RAPP Zoo fetches the record, verifies its hash, validates the closed schema,
  and only then stores it under the user's local `~/.rapp/holograms/`.
- The local zoo supplies the sandboxed Three.js renderer. A DOGG cannot inject
  scripts, URLs, markup, or arbitrary shader code.

Each DOGG is a **caught bottle**: stable identity, dimensions, seed, and
projection memory. A new run pours ephemeral `data_slosh` through that bottle.
Several bottles can therefore render different dimensions of the exact same
source frame without changing the tick or the underlying data.

`kind:"character"` means a procedural 3D body seeded by identity.
`kind:"data-projection"` means a 3D display that can receive a path-free live
zoo snapshot. Both are called holograms in the UI; their data semantics differ.

Catalog:

`https://raw.githubusercontent.com/kody-w/RAR/main/doggs/holograms/index.json`
