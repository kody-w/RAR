# RAR cards v2

`rar-card/2.0` is the portable card format for a RAPP agent. A card is one
UTF-8 JSON object, terminated by one LF byte, with the extension `.card`.
It is data, never active content.

Cards v2 are a strict envelope around the existing card face. The
`cards/holo_cards.json` v1 index remains authoritative and unchanged. A v2
reader finds that same object under `face`; migration never re-mints it,
changes its seed, or changes its incantation.

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
    "url": "https://raw.githubusercontent.com/kody-w/RAR/main/cards/v2/@publisher/agent_name.card"
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

The seed is the card identity:

1. `seed` is `forge_seed(manifest)`.
2. `name_seed` is `seed_hash(id)`.
3. `incantation` is `seed_to_words(seed)`.
4. `face.seed` equals `seed`.
5. The face identity (`face.agent_name`, or the manifest-style `face.name`)
   equals `id`.

A verifier recomputes those values and refuses disagreement. For a migrated
RAR card, a verifier with the frozen v1 index also requires `face` to equal
that indexed face in full. This extra comparison is necessary because legacy
art, prose, environment-derived stats, and curated faces were never encoded
entirely in the seed. It preserves the v1 protocol rather than pretending
those bytes can be reconstructed.

## Payload sleeve

`payload` contains zero or more `agent.py` and `egg` items. An empty array is
a face-only card.

Each item has exactly one source:

- `inline` carries the payload in the card.
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

A card containing inline payload must be no larger than 1 MiB
(1,048,576 bytes) as serialized on disk. Larger payloads must be pinned.
Payload filenames are basenames; path traversal is invalid.

## State, dimensions, and publication

`state` is either:

- `dormant`: stored in a registry or on disk, with no live process.
- `active`: attached to a live twin or parked conversation.

`dimension` is local conversation state. A published card, identified by an
HTTP or HTTPS `scan.url`, must have `dimension: null`. Publishing also returns
the card to `state: "dormant"`. A local export may carry a dimension only by
explicit user choice.

`origin` records where a local card came from. `signature` is reserved for a
future signature profile and is `null` unless such a profile is in use.

## Scanning and summoning

`scan.url` is the value encoded by the QR shown on the card. Registry cards
use their public, raw GitHub URL. Local cards may use
`rar://@publisher/slug@seed`.

Scanning is always:

1. Resolve a URL, numeric seed, or seven-word incantation.
2. Parse the card as data.
3. Validate the schema and identity.
4. Fetch or decode each payload and verify its digest.
5. Display the face and verified payload hashes.

Scanning and verification never import, execute, or hatch payload code.
Execution is a separate, explicit client action after verification.

## SDK operations

```text
python rapp_sdk.py card pack agent.py [--egg file] [--inline | --pin raw-url]
python rapp_sdk.py card unpack agent.card [directory]
python rapp_sdk.py card verify agent.card
python rapp_sdk.py card scan <url | seed | "seven words">
```

`pack` defaults to inline payload. `--pin` pins the `agent.py`; an optional
egg remains inline because it has no independent URL argument. `unpack`
verifies first and writes exact payload bytes. `scan` resolves through the
local v2 index before attempting the public index, so a cloned RAR works
offline.

## Registry migration

`scripts/migrate_cards_v2.py` wraps every v1 entry. Its payload points to the
agent file at the migration revision and carries the registry's
`sha256-lf-v1` digest. Generated cards are dormant, public, dimension-free,
and indexed by id in `cards/v2/index.json`.

The migration is deterministic for an explicit revision and idempotent.
`cards/holo_cards.json`, its seeds, its incantations, and
`resolve_card_from_seed` remain frozen.
