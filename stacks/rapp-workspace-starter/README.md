# RAPP Workspace Starter (RAR stack)

Drop-in pack for a **private, local-first chief-of-staff workspace** —
`rapp-workspace/1.1` conformant. Plant your own vault under YOUR handle in one
chat. Newer/updated shape than `microsoft-365-team` / `neighborhood-starter`:
those plant agent-team **neighborhoods**; this plants a **workspace** (a
private organizing vault for one owner and one world of work — strategy,
portfolio, projects, meetings, people, and a `rapp-projects/` frame authority).

## Files

| File | Purpose |
|---|---|
| `factory_agent.py` | Drop into your local brainstem `agents/`. Plants new workspaces. |
| `workspace_neuron_agent.py` | Tool-form neuron. Drop into `agents/@rapp/` alongside it. No install step — the brainstem's agent loader picks it up as a callable tool that returns a compact, PII-free `[Knowledge Base]` block of the spec's setup/operating rules. Also published standalone at [`agents/@rapp/workspace_neuron_agent.py`](../../agents/@rapp/workspace_neuron_agent.py). |
| `neurons/@rapp/*.neuron.json` (5 files) | Storage-form twin of the exact same knowledge, generated from the same source so the two never drift. For a CommunityRAPP-style backend: install with `install_neurons.py` (Bill Whalen's pattern, see `@bill/neuron_agent.py`) so it lands in the Web UI's system prompt automatically — no tool call needed. |
| `rapp-workspace-starter.egg` | The template content — a `rapp/1` §9 organism egg, PII-free, `verify_egg`-clean. |

### Why two neuron shapes

Same 18 memories, two delivery mechanisms, because "a running brainstem" means
different things depending on setup:

- **Tool-form** (`workspace_neuron_agent.py`): zero backend dependency. Any
  brainstem that loads agents from a folder gets it. This is the right
  default for a portable public stack.
- **Storage-form** (`neurons/@rapp/*.neuron.json`): for a CommunityRAPP-style
  backend with Azure File Storage memory (`utils/storage_factory`), installed
  once via `install_neurons.py` so every session already has it in the system
  prompt without a tool round-trip.

Both are generated from the same `NEURONS` list in `workspace_neuron_agent.py`
— never hand-edit the `.neuron.json` files directly; regenerate them from the
source instead so the two shapes can't drift apart.

### Why a neuron instead of more markdown

Generic protocol knowledge (what files a workspace needs, how mint-once
works, why public mode is refused, how the frame lease protocol works) is
true of every instance — it doesn't change per owner. Writing it into every
planted workspace's `.md` files means N copies to keep in sync and tokens
spent re-reading prose every session. A neuron is one file: structured
`fact`/`gotcha`/`pattern` memories, tag-filterable, cached after first call,
~40% cheaper in tokens than the same facts as markdown. The workspace's own
`.md` files then hold only what's actually specific to that owner and world.

## How to use (one chat)

```
WorkspaceFactory mode=local owner=YOURHANDLE name=my-work display_name="My Work" world="what this workspace runs" dry_run=False
```

Modes: `local` / `private` / `egg` (combinable, e.g. `local,egg`).
**`public` is refused** — a planted workspace holds real, PII-bearing
operating data by design; only this stack's own template `.egg` is meant to
ever be public.

## What you get

- `rapp-workspace/1.1` anatomy: `CLAUDE.md`, `HOME.md`, `PERSONA.md`,
  `where-everything-lives.md`, a `README.md` carrying the PRIVATE guard, and a
  freshly re-minted `rappid.json` (the template ships a placeholder identity;
  the factory always mints a new one — it never reuses the template's)
- Standard sections: `strategy/`, `portfolio/`, `projects/`, `reference/`,
  `people/`, `meetings/`, `connect/`, `role/`
- The `rapp-projects/` frame authority: the reference `append_frame.py`
  writer (lease-aware, multi-operator safe), its protocol schema, and
  `PROTOCOL.md` / `INTEROP.md` / `DISTRIBUTED.md`
- A copy of the canonical `rapp-workspace/1.1` SPEC + SKILL docs under
  `reference/`, so the planted workspace is self-explaining
- **Integrity-gated planting**: `factory_agent.py` carries a stdlib-only
  `verify_egg` reimplementation and refuses to unpack a template that fails
  it — the same rapp/1 §9 guarantee the reference implementation gives, with
  no extra dependency

## Mix and match

Every `.egg` here is a content-addressed `{path: sha256}` manifest (rapp/1
§9.1). A shopping agent doesn't have to take a whole stack — it can pull
`pack.json` from any stack's raw GitHub URL, `verify_egg()` the candidate, and
cherry-pick individual verified files across stacks (e.g. this workspace's
`PLAYBOOK.md` shape alongside a different stack's agent) since each file's
hash stands on its own.

See `pack.json` for the sha256 manifest. See
https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md for the kernel
constitution, and https://github.com/kody-w/rapp-workspace for the
`rapp-workspace/1.1` protocol of record this stack implements.
