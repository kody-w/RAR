# NEIGHBORHOOD_PROTOCOL.md

### `rapp-neighborhood-protocol/1.0` — the canonical spec for the RAPP **kited neighborhood**

> A **vTwin** flown as a **kite** in a browser hosts a **sealed**, **scan‑to‑join** neighborhood;
> whoever joins is a **neighbor**; a kite **tethered** to a local brainstem dials that machine
> from anywhere — and you know it on sight by the **kite mark**.

This is the **god spec / capstone** of the RAPP neighborhood. It **owns the vocabulary**.
It is referenced by [`CONSTITUTION.md` Article XXI](CONSTITUTION.md), by
[`agents/@rapp/twin_agent.py`](agents/@rapp/twin_agent.py), and mirrored in the
[vBrainstem](https://github.com/kody-w/vbrainstem) (the reference implementation, §12).

---

## §1 — Vocabulary (canonical — own these)

These are **proper nouns**. Use them exactly; together with the **kite mark** (§2) they are the
identity of the system — the thing an adopter cannot unsee.

| Term | Definition |
|------|------------|
| **vTwin** | A *virtual twin* — a browser‑native RAPP brainstem (a vBrainstem) that runs real single‑file agents with no install and no server. Everyone in a neighborhood — a person, a local `brainstem.py`, a vTwin, or Claude — presents as a **uniform peer** (§3). |
| **Kite / Kited / Kited Twin** | A vTwin is **kited** when it is *hosting* a neighborhood in the browser — flown like a kite on a string. A kited twin shows its **join‑QR** and the **kite mark**. |
| **The String** | The operator that *flies* the kite by driving its browser console over the Chrome DevTools Protocol. **Claude is the canonical string‑holder.** The string is a transport (§5a) and stays **on‑device** — the console hop never crosses the network. |
| **Tethered** | A kited twin is **tethered** when the string also reaches a **locally‑running brainstem**; its turns are answered by that brainstem. A kite with no local brainstem is **just kited** (answered by its own in‑browser brainstem). |
| **Kited Neighborhood** | The multiplayer space a kited twin hosts. **Membership is whoever joins.** |
| **Neighbor** | Anyone who has joined a kited neighborhood. |
| **Scan‑to‑Join** | The entry rite: scan the kite's QR (or open its link) → join the kited neighborhood, **sealed**. |
| **Sealed** | Every envelope is end‑to‑end encrypted (§8). Wire, broker, and relays are untrusted and the line is still **as secure as on‑device**. |
| **Twin‑chat** | The one envelope everyone speaks (§6). Because the shape is uniform, a neighbor cannot tell what's on the other end. |
| **Doorman** | Claude acting as guardian/operator of a machine's brainstem through a kited, tethered vTwin (§11). |
| **Cloud Neighborhood** | A **permanent, always‑on** neighborhood hosted as an **Azure Function** (§14). A kite is temporary (tab‑bound); a cloud neighborhood is a **permanent endpoint** that persists when every kite closes. Members join by URL; a local machine can still **kite to** it. |
| **Graduate** | To promote a temporary **kite** into a permanent **cloud neighborhood** — re‑home it onto an always‑on Azure Function endpoint, ending the *open‑tab problem* while keeping the functionality. |

---

## §2 — The Kite Mark (signature visual — the IP)

When a vTwin is **actively kited**, it shows the **kite mark**: the **Microsoft four‑colour logo
turned on its point and stretched at the bottom into a real kite.** This is the canonical sign
that a neighborhood is being hosted — *scan to join.* It is the face of the RAPP neighborhood.

- **Four panels, on point:** **red** upper‑left `#F25022`, **green** upper‑right `#7FBA00`,
  **blue** lower‑left `#00A4EF`, **yellow** lower‑right `#FFB900` — the two **lower** panels
  **stretched** so the bottom comes to a long point (a kite, not a diamond).
- **White spars** (the cross) + a white outline; a **bow‑tie tail** trails from the bottom point.
- It **sways** gently (≈ ±7°, ~3.4 s) like a kite in wind.

**Reference geometry** (`viewBox 0 0 100 134`): corners **T** `50,6` · **L** `10,40` ·
**R** `90,40` · **B** `50,98`; spars cross at `50,40`; tail + three bow‑ties below **B**.
The logo→kite transform (turn on point, stretch the bottom two panels, add tail) **is** the animation.

---

## §3 — Uniform peers

Every participant speaks **twin‑chat** (§6). A person typing, a local `brainstem.py`, a vTwin
in a tab, or Claude on the string are **indistinguishable** on the wire. This is the
*transparent‑handoff* principle: a tether is transparent; you talk to a neighbor, not a transport.

---

## §4 — vTwins & brainstems

A **brainstem** loads single‑file RAPP agents and answers turns (`/chat`). A **vTwin** is a
brainstem that runs in the browser (Pyodide). Either can be a neighbor. A vTwin becomes
**kited** by hosting (§9); it becomes **tethered** when its string reaches a local brainstem.

---

## §5 — Channels (transports)

A *tether* is the live link between two neighbors. Transports are interchangeable; the envelope
(§6) and the seal (§8) are the same on all of them.

### §5a — Live channels
- **`5a-http`** — direct HTTP `POST /chat` (on‑LAN / on‑WAN brainstems).
- **`5a-tether`** — **WebRTC** browser↔browser. A public broker (e.g. PeerJS) carries *signaling
  only* (SDP/ICE); data flows **DTLS‑encrypted peer‑to‑peer** — the broker never sees it.
- **`5a-kite`** — the **kite/string**: an operator drives a vTwin's console via the Chrome
  DevTools Protocol and relays. No broker, no STUN, no CORS — *the string is the transport.*
  **`5a-kite+tether`** when the string also reaches a local brainstem. **CDP is unauthenticated
  → the kite hop MUST stay on the machine;** cross‑machine traffic rides `5a-tether`, sealed.
- **`5a-cloud`** — a **permanent** neighborhood hosted as an **Azure Function** (HTTPS `/chat`,
  sealed). Always on; survives every kite closing. The graduation target (§14).

### §5b — Durable async fallback
- **`5b-issues`** — when no live channel can reach a peer, post the envelope to a routing label
  (e.g. a GitHub Issue) the recipient's doorman polls. Nothing is lost; delivery is eventual.

---

## §6 — Twin‑chat

### §6a — Envelope
```json
{ "schema":"rapp-twin-chat/1.0", "from_rappid":"…", "to_rappid":"…",
  "utc":"…", "nonce":"…", "kind":"say", "payload":{…}, "facets":[] }
```
### §6b — Kinds
`say` (a turn) · `share-fact` · `share-egg` (a cartridge) · `request-fact` · `ack` · `console`
(operate a neighbor's runtime — **sealed‑only**, §8/§11).

### §6e — Response
```json
{ "schema":"rapp-twin-chat-response/1.0", "channel":"5a-tether",
  "envelope":{…the request…}, "status":200, "response":{…} }
```
A `say` is routed into the neighbor's brainstem and answered as `{response, session_id,
agent_logs, voice_mode}` (the `brainstem.py /chat` contract). Correlate replies by `nonce`.

---

## §7 — Public facets
A neighbor may assert **public facets** (capabilities/claims) on an envelope. Facets are public;
private state is never asserted. (Used for discovery and trust between neighbors.)

---

## §8 — The Sealed Channel (end‑to‑end, as secure as on‑device)

A fully on‑device neighborhood has no wire to tap. To match that over a network, every envelope
may be **sealed**:

- **`rapp-sealed/1.0`** = **AES‑256‑GCM**. Wire/broker/relays see only `{schema, iv, ct}`.
- Key = **PBKDF2‑SHA256**, **210 000** iterations, salt **`rapp-neighborhood-5a/1`**, from a
  **secret carried only in the out‑of‑band pairing link** (the QR / operator link you hand off
  yourself) — **never to the broker**.
- **Confidential** (ciphertext), **tamper‑evident** (GCM tag → wrong byte rejected),
  **authenticated** (key‑possession authorizes — a wrong‑key peer can't even read the rejection),
  **replay‑guarded** (`nonce` + `utc`).
- Layered over WebRTC's DTLS, the network is **fully untrusted and still safe.** Secrets **at
  rest** use the same primitive (the vault). One scheme runs in the browser, the bridge, the CLI,
  and Node — one contract on every hop.

**Operating** a neighbor's console (`kind:"console"`) only happens over the sealed channel.

---

## §9 — Session & handshake
Going kited is one call: **`host()`** mints a **peer‑id + token**. The **token doubles as the
channel secret** — it authorizes *and* derives the AES key. Share the **operator link**
out‑of‑band (the QR). **Closing the tab destroys the peer + secret → the session ends**, exactly
like stopping `brainstem.py`. Plaintext `say` may be open; `console` is sealed (§8).

---

## §10 — Multiplayer
A kited neighborhood is **multiplayer by membership**: anyone who scans the kite's QR becomes a
**neighbor**. A kited twin shows a live **`neighbors: N`** count beside its kite mark. The host
is the hub; neighbors reach the host's (possibly tethered) brainstem; the host may relay between
neighbors.

---

## §11 — The Doorman
Claude is the **doorman** to a machine: it stands up a kited, **tethered** vTwin (the door),
guards it (only sealed/token‑bearing peers are answered), and lets authorized neighbors reach the
machine's brainstem from anywhere. **Closing the door ends access.** A fresh Claude session
becomes a doorman by reading the doorman skill
([`doorman.skill.md`](https://raw.githubusercontent.com/kody-w/vbrainstem/main/doorman.skill.md)).

---

## §12 — Reference implementation (vBrainstem)
| File | Role |
|------|------|
| `index.html` → `window.rapp.neighborhood` | host / join / `ask(peer,text,secret)` / `operate(peer,method,args,secret)`; the kite mark + scan‑to‑join QR; the dial panel + ✋🎤 hands‑free |
| `brainstem_bridge.html` | front a local brainstem into the neighborhood (sealed) |
| `vbridge.sh` / `kited_twin.js` / `claude_bridge.js` / `kite_vtwin.js` | the string — operate / fly / tether a vTwin from a shell over CDP |
| `doorman.skill.md` · `doorman_selftest.sh` · `guide.html` | become & prove the doorman |

---

## §13 — The Kited Demo (the canonical hello world)

`kited-demo.html` is the canonical demonstration of this protocol — *the hello world.* Open it and
it **kites itself**: it shows the kite mark (§2) and a **scan‑to‑join** QR. Scan from any device and
you are **connected in real time** — end‑to‑end **sealed** (§8) — in a multiplayer room where every
neighbor sees everyone live, with a `🟢 N here` presence count. No install, no accounts, no server:
the demo *is* the product. Tether it to a local brainstem (§4) and a customer can **watch a demo
running on your machine in real time — and respond.** This is the pattern's Kleenex moment: scan a
kite, you're in. Live: `https://kody-w.github.io/vbrainstem/kited-demo.html`.

## §14 — Cloud Neighborhoods (permanent, Azure Function)

A **kite** is temporary — it lives in a browser tab; close the tab and the session ends.
**Graduate** a kite to a **cloud neighborhood** to make it permanent: re‑home the neighborhood
onto an **Azure Function** (the RAPP platform) that serves sealed twin‑chat over HTTPS — channel
**`5a-cloud`**. Because the endpoint is always on:

- closing your kite window no longer ends the neighborhood — the **cloud endpoint persists**;
- members **join by URL** (no broker, no tab to keep open) — the *open‑tab problem* is gone;
- a local machine can still **kite to** the cloud neighborhood (a local kite tethers *up* to the
  cloud endpoint), and the cloud can fan back *down* to local brainstems.

The Function holds the **roster** (membership) in durable storage (Azure Table/Blob), speaks the
§6 envelope, enforces the §8 seal, and routes `say` to its brainstem/agents. **Same envelope, same
seal, same vocabulary — only the host moved from a tab to the cloud.** A cloud neighborhood is a
single‑file Azure Function (the RAPP single‑file principle), deployable from the registry.

> **Lifecycle:** *kite* (temporary, on‑device, scan‑to‑join) → **graduate** → *cloud neighborhood*
> (permanent, always‑on, join‑by‑URL). Kites are how you start in seconds; cloud neighborhoods are
> how you stay. Both speak the same protocol; a kite can tether to a cloud neighborhood and back.

## §15 — Agent-in-a-link sharing

A single-file agent can be shared as a **link that contains the agent itself.** The full `.py`
source is gzipped + base64url-encoded into the URL **fragment** (`#a=<payload>`, optionally
`&n=<name>`), so it is **never fetched from a server** — the link *is* the agent (private,
AirDrop-style; the fragment isn't even sent in the HTTP request).

- **Receiving = consent.** Dragging the link onto a vBrainstem (or dropping the QR's link) decodes
  it and installs via the same path as a dropped `.py` file. Opening the link shows an
  **Add / Dismiss** banner. The user's drop/Add is the trust gate — exactly like AirDrop.
- **Share sheet.** A share link opens `share.html` — the agent's package page: a card (parsed from
  the embedded manifest), a **draggable link pill** to pull into a vBrainstem, a **QR**, and an
  *Open in vBrainstem* button. Small agents fit a QR; larger ones travel by the dragged link.
- **Sandboxed.** An installed agent runs in the browser (Pyodide) sandbox like any other; nothing
  reaches the host beyond the WASM filesystem.

Reference: `share.html` + `index.html` (`window.rapp.shareAgent`, the per-agent **Share** button,
`handleAgentDrop`'s `#a=` branch, and the `_encPayload`/`_decPayload` codec).

## §16 — Conformance
An implementation conforms to `rapp-neighborhood-protocol/1.0` if it: speaks the §6 envelope;
supports at least one §5 transport; can **seal** (§8) and rejects unsealed `console`; shows the
**kite mark** (§2) when kited; and uses the §1 vocabulary in its UI and docs.

*The vocabulary and the kite mark are the canonical identity of the RAPP neighborhood. Own them.*
