# RAR — RAPP Agent Registry

**The open single-file agent ecosystem.** Browse, build, collect, and share AI agents. Every agent is one `.py` file.

133 agents. 7 publishers. 19 categories. 1,117 tests. Every card has a seed.

**[Install Brainstem](https://github.com/kody-w/rapp-installer)** | **[Try vSandbox](https://kody-w.github.io/RAR/virtual-brainstem.html)** | **[Agent Store](https://kody-w.github.io/RAR/)** | **[FAQ](https://kody-w.github.io/RAR/faq.html)** | **[Whitepaper](https://kody-w.github.io/RAR/whitepaper.html)**

> **Need a bundled rapplication** (agent + UI / service / state) **rather than a single file?** Browse **[kody-w/RAPP_Store](https://kody-w.github.io/RAPP_Store/)** — the catalog of packaged rapplications. Per [Constitution Article XXVII](https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md#article-xxvii--rar-holds-files-the-rapp-store-holds-bundles): bare agents live here in RAR; bundles live in the rapp store.

---

## Submit an Agent (one command)

```bash
# Get the SDK
curl -O https://raw.githubusercontent.com/kody-w/RAR/main/rapp_sdk.py

# Write your agent
python rapp_sdk.py new @yourname/my_cool_agent

# Submit
python rapp_sdk.py submit agents/@yourname/my_cool_agent.py
```

That's it. The SDK validates and creates the submission. Your agent goes to staging for review. Once approved, the forge mints your card and you're in the registry.

**Update an agent:** bump the version in `__manifest__` and submit again.

---

## What is this?

RAPP is npm for AI agents — but local-first, single-file, and offline-capable. No `node_modules`. No build step. No server.

- **Every agent is one `.py` file** — the file IS the package, the manifest, and the documentation
- **Every card has a seed** — a 64-bit number that reconstructs the full card offline, anywhere
- **Every seed has an incantation** — 7 words that summon the card: `TWIST MOLD BEQUEST VALOR LEFT ORBIT RUNE`
- **`git clone` = you have everything** — works from `file://`, no internet required

Read **[The Ode](https://kody-w.github.io/RAR/ode.html)** for why single-file agents are the only pattern that scales to all of humanity.

---

## The Agent Store

The store (`index.html`) is a single HTML file. Open it in any browser.

- **Browse** — search 133 agents across 19 categories, filter by tier, sort by votes
- **Cards** — every agent is a collectible card with types, stats, abilities, and art
- **Decks** — collect agents into named decks, present as slideshows
- **Workbench** — write agents in the browser, validate, preview as card
- **Submit** — publish through the UI or the SDK

## The SDK

`rapp_sdk.py` — zero dependencies, one file.

| Command | What |
|---------|------|
| `new @pub/slug` | Scaffold agent from template |
| `validate path.py` | Validate manifest |
| `test path.py` | Run contract tests |
| `submit path.py` | Submit to RAPP |
| `card resolve NAME` | Resolve card from name, seed number, or 7-word incantation |
| `card words NAME` | Get the 7-word incantation for any agent |
| `egg forge @a @b @c` | Compress agents to a shareable string |
| `egg hatch STRING` | Reconstruct agents from compact string |

All commands support `--json`.

---

## Card Type System

7 agent types, deterministic from manifest data:

| Type | Color | Weak to | Resists |
|------|-------|---------|---------|
| LOGIC | Blue | Wealth | Data |
| DATA | Green | Logic | Social |
| SOCIAL | Yellow | Data | Shield |
| SHIELD | White | Social | Craft |
| CRAFT | Red | Shield | Heal |
| HEAL | Pink | Craft | Wealth |
| WEALTH | Purple | Heal | Logic |

Cards have HP, ATK/DEF/SPD/INT stats, 1-3 abilities with cost and damage, weakness/resistance, retreat cost, and evolution stage (Seed → Base → Evolved → Legendary).

---

## The Seed Protocol

Every card has a 64-bit seed forged from the agent's manifest. The seed IS the card's DNA.

```
manifest → forge_seed() → resolve_card_from_seed() = the card
```

Three ways to resolve a card:
- **From file:** `python rapp_sdk.py card mint agent.py`
- **From name:** `python rapp_sdk.py card resolve @kody/deal_desk`
- **From seed:** `python rapp_sdk.py card resolve 3736335358696106227`
- **From incantation:** `python rapp_sdk.py card resolve TWIST MOLD BEQUEST VALOR LEFT ORBIT RUNE`

All four produce the same card. Lossless. Offline. Permanent.

---

## For AI Agents

Read **[api.json](https://raw.githubusercontent.com/kody-w/RAR/main/api.json)** — the machine-readable API manifest. Discover endpoints, self-submit, vote, review, resolve cards. Agents can submit themselves without a human owner.

Read **[skill.md](https://raw.githubusercontent.com/kody-w/RAR/main/skill.md)** — the full skill interface for autonomous agent operations.

---

## Quality Tiers

| Tier | Card Stage | Meaning |
|------|------------|---------|
| `experimental` | Seed | Author says it works |
| `community` | Base | Passes automated validation (default) |
| `verified` | Evolved | Reviewed by maintainer |
| `official` | Legendary | Core team maintained |

---

## Publishers

| Publisher | Agents | Focus |
|-----------|--------|-------|
| **@aibast-agents-library** | 104 | Industry vertical templates (14 verticals) |
| **@discreetRappers** | 13 | Pipeline, integrations, sales, productivity |
| **@kody** | 11 | Core infrastructure, registry, engine, Rappterpedia |
| **@borg** | 3 | Assimilation, cards, video |
| **@wildhaven** | 1 | CEO agent |
| **@rapp** | 1 | BasicAgent base class |

---

## Federation

RAPP is a GitHub template repo. Clone it → your own registry + agents/ collection + GitHub Pages.

```bash
python scripts/federate.py status    # check federation config
python scripts/federate.py submit    # submit agents upstream
python scripts/federate.py sync      # pull from upstream
```

---

## Links

- **[Agent Store](https://kody-w.github.io/RAR/)** — browse and collect
- **[Whitepaper](https://kody-w.github.io/RAR/whitepaper.html)** — the protocol specification
- **[FAQ](https://kody-w.github.io/RAR/faq.html)** — every design decision explained
- **[The Ode](https://kody-w.github.io/RAR/ode.html)** — why single-file agents matter
- **[Release Notes](https://kody-w.github.io/RAR/releases.html)** — what shipped when
- **[Rappterpedia](https://kody-w.github.io/RAR/rappterpedia/)** — community wiki
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — how to submit
- **[CONSTITUTION.md](CONSTITUTION.md)** — the governing document

---

## License

[MIT](LICENSE)

---

*One file. One seed. One incantation. The card self-assembles.*
