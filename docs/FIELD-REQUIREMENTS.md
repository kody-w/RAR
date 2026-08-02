# Field requirements — and where RAR stands against each

This document exists so nobody has to take a claim on trust. Every row below
records a requirement raised in enterprise review, an honest status, and a way
to check the answer yourself — a URL you can open, a command you can run, or a
test you can read.

Requirements are paraphrased as capability statements. No individual is quoted
or named, and nothing internal is reproduced here.

**Status vocabulary**

| Status | Meaning |
|--------|---------|
| **Solved** | Shipped, verifiable today by the evidence in the row. |
| **Partly solved** | Real mechanism exists; a named gap remains. |
| **Out of scope** | A real problem, but organisational rather than technical. RAR cannot fix it and does not pretend to. |

---

## 1. Consumption — "business users do not live in GitHub"

The single most important requirement: an end user must never be sent to a
repository. The consuming application owns the experience.

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1.1 | Consume the registry without a GitHub account, login, or repo UI | **Solved** | Every endpoint is anonymous static JSON. `curl https://raw.githubusercontent.com/kody-w/RAR/main/manifest.json` — no token, no headers. |
| 1.2 | Embed the catalog inside a host application (AIdeate, vBrainstem, grail brainstem) | **Solved** | `api/v1/catalog.json` — one fetch returns all 278 agents with descriptions, tags, tiers and provenance. No second request, no SDK. |
| 1.3 | Call it from a browser without a proxy | **Solved** | GitHub raw and jsDelivr both return `Access-Control-Allow-Origin: *`. Verify: `curl -sI .../manifest.json \| grep -i access-control`. |
| 1.4 | No backend to run, fund, or operate | **Solved** | There is no server. Every endpoint is a file committed to `main` and served by GitHub's CDN. |
| 1.5 | Pin to a known-good version | **Solved** | Swap `main` for a commit SHA in any URL, or use `cdn.jsdelivr.net/gh/kody-w/RAR@<sha>/...`. |
| 1.6 | Prove a real user journey needs no GitHub at all | **Solved** | **[discover.html](https://kody-w.github.io/RAR/discover.html)** — describe a problem in plain English, get ranked agents. Automated test loads it with `github.com` blocked at the network layer; it completes with zero errors because it only ever reads two static files. No account, no repo chrome, no publisher handles. |

**Read `manifest.json` first** — it lists every endpoint and includes copy-paste
recipes for rendering a catalog, recommending from a use case, and installing an
agent. For the experience itself, open
**[discover.html](https://kody-w.github.io/RAR/discover.html)**.

---

## 2. Discovery — "do not show them everything"

Exposing a raw catalog was explicitly rejected. Discovery has to start from the
user's own words.

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 2.1 | User describes a use case, a recommendation comes back | **Solved** | `api/v1/match.json` ships 20 canonical use cases plus a 2,226-term ranking index. Matching runs client-side; no model call, no backend. |
| 2.2 | Free-text queries, not just fixed categories | **Solved** | `match.json.index` maps term → `agent_id:weight`. Tokenize, sum, sort. The algorithm is written out in `how_to_query`. |
| 2.3 | Ranked results, not an unordered dump | **Solved** | Weighted by field (name and tags ×3, category ×2, description ×1) and damped by document frequency so common words cannot dominate. |
| 2.4 | Relevance good enough to trust | **Solved** | "review vendor contracts for risk" → *Vendor Contract Risk Review* first. "supply chain has supplier delays" → *Supplier Risk Monitoring* first. "sales team keeps missing forecast" → *Deal Health Score*, *Pipeline Velocity*, *Revenue Forecast*. Reproduce with the snippet in § "Try it", or use [discover.html](https://kody-w.github.io/RAR/discover.html). |
| 2.5 | Show why something matched, not just that it did | **Solved** | Ranking retains the matched terms; `discover.html` renders them on every result ("Matched on **review**, **contracts**, **risk**, **renewal**"). |
| 2.6 | One destination, not several competing libraries | **Partly solved** | `manifest.json` is a single discovery root, and `state/federation.json` consolidates peer catalogs. Genuine consolidation is an organisational decision, not a schema one. |

---

## 3. Curation — "we will find novelty content in there"

A catalog that mixes contract analysis with trading-card agents loses an
enterprise audience on first impression.

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 3.1 | An enterprise-safe slice that needs no further filtering | **Solved** | `api/v1/audience/business.json` — 271 agents, novelty excluded. Serve it directly; `discover.html` does exactly that. |
| 3.2 | Novelty must not leak in through a mislabelled category | **Solved** | An explicit novelty tag (`game`, `pokemon`, `collectible`, `adventure`, …) forces the consumer slice regardless of category. A text adventure filed under `devtools` still does not reach the business slice. See `classify()` in `scripts/build_static_api.py`. |
| 3.3 | Curation demonstrably holds | **Solved** | Query the business slice for *"I want to play a game"* — it returns essentially nothing. The games are in the catalog; they are not in the enterprise surface. |
| 3.4 | Curation must not silently hide useful agents | **Solved** | `both` is the default for ambiguous cases, and `both` appears in every slice. Misclassification degrades to over-showing, never to hiding. |
| 3.5 | Quality signal per agent | **Partly solved** | `quality_tier` (`frontier` → `community` → `verified` → `official`) ships on every record and renders on each card. Promotion beyond automated validation is still a human review step. |

---

## 4. Trust and provenance — "where did this come from"

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 4.1 | Every recommendation traceable to a source | **Solved** | Each record carries `source.path`, `source.raw`, `source.cdn` and `source.sha256`. |
| 4.2 | Verify what you downloaded is what was published | **Solved** | `sha256sum` the fetched file against `source.sha256`. |
| 4.3 | Published URLs must not break | **Solved** | CONSTITUTION.md Article XXIII freezes every published path permanently. Enforced by `scripts/check_url_stability.py`, gated in CI ahead of every other job, and covered by `tests/test_url_stability.py` — which proves the gate *fails* on rename and on deletion, not merely that it passes when nothing is wrong. Currently 319/319 paths resolve. |
| 4.4 | Content stays fresh | **Solved** | `build-registry.yml` rebuilds the registry and the API on every push to `agents/**`, so the catalog cannot drift from the files. |
| 4.5 | Detect change without re-downloading everything | **Solved** | `api/v1/status.json` publishes a content hash per endpoint. Compare, then fetch only what moved. |
| 4.6 | Responsible-AI review and formal ALM sign-off | **Out of scope** | An approval process, not a code change. RAR supplies the audit surface (immutable paths, hashes, receipts, CI history); it cannot grant the approval. |

---

## 5. Deployability

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 5.1 | Installing an agent must be trivial | **Solved** | `GET source.raw`. The response body *is* the agent — one file, no manifest, no archive, no package manager. This is the single-file principle in Article II. |
| 5.2 | Declare configuration up front | **Solved** | `requires_env` lists required environment variables on every record, so a host application can prompt before install rather than failing at runtime. |
| 5.3 | Declare dependencies | **Solved** | `dependencies` lists `@publisher/slug` entries per record. |
| 5.4 | Agents usable as-is, without rework | **Partly solved** | Agents install as-is; connecting them to a customer's own systems still requires configuration. Honest position: RAR removes the packaging and distribution problem, not the integration problem. |
| 5.5 | One-click deploy to Copilot Studio | **Out of scope here** | Blocked upstream by a platform API limitation, tracked outside this repository. |

---

## 6. Scale and operations

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 6.1 | Catalog growth cannot depend on hand-curation | **Partly solved** | Submission is automated end to end (`process-issues.yml`, `approve-agent.yml`, `build-registry.yml`). Growth is now bounded by contribution, not by maintainer effort. |
| 6.2 | Serving cost must not scale with usage | **Solved** | Static files on a CDN. A thousand consumers cost exactly what one costs. |
| 6.3 | No dedicated operators to keep it running | **Solved** | Nothing to operate — no server, no database, no queue, no secrets in the read path. |
| 6.4 | Cannot depend on specific individuals | **Solved** | Every step is a committed script run by CI: `build_registry.py`, `build_static_api.py`, `check_url_stability.py`. Reproducible by anyone with a checkout. |
| 6.5 | Support organisation for thousands of users | **Out of scope** | A staffing question. Worth noting the read path has no failure mode to support: static files with no auth and no runtime. |
| 6.6 | Attribute usage to business outcomes | **Partly solved** | `state/metrics.json` and `metrics_history.json` track catalog and engagement metrics. Tying downloads to revenue requires host-application telemetry RAR cannot see. |

---

## Try it

Everything below runs against production right now. No credentials.

```bash
# 1. Discover the whole API from one URL
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/manifest.json | python3 -m json.tool

# 2. Fetch the curated enterprise catalog
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/api/v1/audience/business.json \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['count'], 'enterprise-appropriate agents')"

# 3. Recommend from a plain-English use case, entirely client-side
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/api/v1/match.json > /tmp/m.json
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/api/v1/catalog.json > /tmp/c.json
python3 - <<'PY'
import json, re
idx = json.load(open('/tmp/m.json'))['index']
cat = {a['id']: a for a in json.load(open('/tmp/c.json'))['agents']}
query = "I need to review vendor contracts for risk"
scores = {}
for t in [w for w in re.findall(r'[a-z0-9]+', query.lower()) if len(w) > 2]:
    for entry in idx.get(t, []):
        aid, w = entry.rsplit(':', 1)
        scores[aid] = scores.get(aid, 0) + int(w)
for aid, s in sorted(scores.items(), key=lambda x: -x[1])[:3]:
    print(f"{s:4}  {cat[aid]['display_name']}")
PY

# 4. Install an agent — the response body is the whole package
curl -s https://raw.githubusercontent.com/kody-w/RAR/main/agents/@rapp/drift_agent.py -o drift_agent.py

# 5. Prove the URL contract holds
python scripts/check_url_stability.py
```

---

## What is deliberately not claimed

Overclaiming is how credibility is lost, so these are stated plainly:

- **Integration is not solved.** Agents install in one request. Wiring them to a
  customer's own systems is real work that RAR does not remove.
- **Support and staffing are not solved.** Static hosting removes the operational
  burden of *serving* the registry. It does not create a support organisation.
- **Business-outcome attribution is incomplete.** RAR can report what the catalog
  contains and how it changes. Connecting that to revenue needs telemetry from
  the consuming application.
- **Catalog size is bounded by contribution.** The pipeline is automated, but
  automation does not by itself produce well-documented agents.

---

*Companion documents: [`CONSTITUTION.md`](../CONSTITUTION.md) (Article XXIII —
The Permanent URL Contract), [`manifest.json`](../manifest.json) (the live API
descriptor), [`skill.md`](../skill.md) (the agent-facing interface).*
