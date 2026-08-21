# Rappid tiles (rar-card/2.0)

`rar-card/2.0` is the protocol behind a portable rappid tile for a RAPP agent.
Each rappid tile is one UTF-8 JSON object, terminated by one LF byte, with the
extension `.card`. It is data, never active content.

Rappid tiles are a strict envelope around the existing tile face. The
`cards/holo_cards.json` v1 index remains authoritative and unchanged. A v2
reader finds that same object under `face`; migration never re-mints it,
changes its seed, or changes its incantation.

## The hero law

The `.card` file is the rappid tile a person keeps. A offline-ready tile carries
every required payload inline, so a second offline device can verify and
unpack it using only the tile's own bytes. After successful verification,
`card verify` and `card scan` report `offline: ready` only when every payload
item is inline.

`card pack agent.py` therefore defaults to `--inline`. `--pin <raw-url>` is
RAR's compact registry form: it preserves a revision-pinned integrity proof
without duplicating the payload. A pinned-only rappid tile is never called
offline-ready, even when verification can currently fetch its URL; it reports
`offline: needs <n> pinned payload(s)`.

## The file name

The sleeve says what is inside. A rappid tile with a primary payload
(`payload[0]`) is named by appending `.card` to that payload's complete
filename:

| Primary payload | Rappid tile |
|---|---|
| `bookfactory_agent.py` | `bookfactory_agent.py.card` |
| `bookfactory.egg` | `bookfactory.egg.card` |

`card pack x_agent.py` writes `x_agent.py.card` beside the input by default.
`--out` may choose another directory, but its basename must still be
`x_agent.py.card`. Without an output directory, `card unpack x_agent.py.card`
strips the final `.card` and restores `x_agent.py` beside the sleeve. A verifier
or scanner refuses a file or URL whose basename disagrees with
`payload[0].filename`.

A face-only rappid tile has no primary payload and uses `<slug>.card`. RAR
migration publishes `cards/v2/@publisher/<primary payload filename>.card`. Source
basenames are used normally; if legacy agents under one publisher collide
after flattening, migration uses the registry's canonical collision-safe
install filename as both the primary payload filename and sleeve name.

## Shape

```json
{
  "schema": "rar-card/2.0",
  "id": "@publisher/agent_name",
  "seed": 13467203979104256843,
  "name_seed": 3136112411,
  "incantation": "TWIST MOLD BEQUEST VALOR LEFT ORBIT RUNE",
  "version": "1.2.0",
  "face": {},
  "manifest": {},
  "payload": [],
  "state": "dormant",
  "origin": null,
  "dimension": null,
  "scan": {
    "url": "https://raw.githubusercontent.com/kody-w/RAR/main/cards/v2/@publisher/agent_name.py.card"
  },
  "provenance": {
    "minted_by": "rapp_sdk 2.0",
    "rar_revision": "e47755faaa0486f3abe54a6a5d29aab74d203dc8"
  },
  "signature": null
}
```

The normative schema is [`schema/rar-card-2.0.json`](../schema/rar-card-2.0.json).
Unknown fields are rejected at the envelope and payload levels. The `face`
object remains extensible because v1 faces are already published and include
both procedural and hand-forged fields.

## Identity

The seed is the rappid tile identity:

1. `seed` is `forge_seed(manifest)`.
2. `name_seed` is `seed_hash(id)`.
3. `incantation` is `seed_to_words(seed)`.
4. `face.seed` equals `seed`.
5. The face identity (`face.agent_name`, or the manifest-style `face.name`)
   equals `id`.

A verifier recomputes those values and refuses disagreement. For a migrated
rappid tile, a verifier with the frozen v1 index also requires `face` to equal
that indexed face in full. This extra comparison is necessary because legacy
art, prose, environment-derived stats, and curated faces were never encoded
entirely in the seed. It preserves the v1 protocol rather than pretending
those bytes can be reconstructed.

## Payload sleeve

`payload` contains zero or more `agent.py` and `egg` items. An empty array is
a face-only rappid tile.

Each item has exactly one source:

- `inline` carries the payload in the rappid tile.
- `url` points to pinned bytes. GitHub raw URLs must name an immutable
  revision, not `main`, `master`, or `HEAD`.

Every source is verified before it is unpacked:

| Kind | Inline representation | Digest |
|---|---|---|
| `agent.py` | UTF-8 text | `sha256_lf_v1` |
| `egg` | RFC 4648 base64 | `sha256` |

`sha256-lf-v1` hashes the UTF-8 bytes after replacing every CRLF byte pair
with LF. It performs no other Unicode, whitespace, or newline normalization.
Binary payloads use SHA-256 over the exact bytes. Digests are lowercase,
64-character hexadecimal strings.

A rappid tile containing inline payload must be no larger than 1 MiB
(1,048,576 bytes) as serialized on disk. Larger payloads must be pinned.
Payload filenames are basenames; path traversal is invalid.

The reference SDK also applies defensive read ceilings of 4 MiB for a rappid
tile document and 64 MiB for one pinned payload. Clients that support larger
pinned artifacts must stream them through verification instead of buffering
them.

## State, dimensions, and publication

`state` is either:

- `dormant`: stored in a registry or on disk, with no live process.
- `active`: attached to a live twin or parked conversation.

`dimension` is local conversation state. A published rappid tile, identified by an
HTTP or HTTPS `scan.url`, must have `dimension: null`. Publishing also returns
the tile to `state: "dormant"`. A local export may carry a dimension only by
explicit user choice.

`origin` records where a local rappid tile came from. `signature` is reserved
for a future signature profile and is `null` unless such a profile is in use.

## Scanning and summoning

`scan.url` is the value encoded by the QR shown on the rappid tile. Registry
tiles use their public, raw GitHub URL. Local tiles may use
`rar://@publisher/slug@seed`.

Scanning is always:

1. Resolve a URL, numeric seed, or seven-word incantation.
2. Parse the rappid tile as data.
3. Validate the schema and identity.
4. Fetch or decode each payload and verify its digest.
5. Display the face and verified payload hashes.

Scanning and verification never import, execute, or hatch payload code.
Execution is a separate, explicit client action after verification.

## SDK operations

```text
python rapp_sdk.py card pack agent.py [--egg file] [--inline | --pin raw-url]
python rapp_sdk.py card unpack agent.py.card [directory]
python rapp_sdk.py card verify agent.py.card
python rapp_sdk.py card scan <url | seed | "seven words">
```

`pack` defaults to inline payload for a rappid tile a person keeps. `--pin` creates
RAR's compact form by pinning the `agent.py`; an optional egg remains inline
because it has no independent URL argument. `unpack` verifies first and writes
exact payload bytes. `scan` resolves through the local v2 index before
attempting the public index. Resolution from a local clone does not change the
readiness label: any rappid tile with pinned payloads remains not offline-ready.

## Registry migration

`scripts/migrate_cards_v2.py` wraps every v1 entry. Its payload points to the
agent file at the migration revision and carries the registry's
`sha256-lf-v1` digest. Generated rappid tiles are dormant, public, dimension-free,
named `<primary payload filename>.card`, and indexed by id in
`cards/v2/index.json`.

The migration is deterministic for an explicit revision and idempotent.
`cards/holo_cards.json`, its seeds, its incantations, and
`resolve_card_from_seed` remain frozen.
