# Fleet Management (RAR stack)

> Drop-in pack that turns one brainstem into a fleet controller for a
> network of Mac-mini brainstems.  Discover, authorize, deploy, chat any
> twin on any peer, fan out across the mesh — all from one chat.

## Two files

| File | Purpose |
|------|---------|
| `fleet_agent.py` | The SSH-driven fleet adapter.  All 23 actions below. |
| `twin_egg_hatcher_agent.py` | Scale-aware single-file hatcher (agent / twin / neighborhood / swarm / factory / industry / estate). |

## Install (one chat)

Drop both files into your brainstem's `agents/`.  `load_agents()` re-scans on the next `/chat`, no restart.

```bash
cp fleet_agent.py twin_egg_hatcher_agent.py ~/.brainstem/src/rapp_brainstem/agents/
```

The LLM now has `Fleet(...)` and `HatchTwinEgg(...)` as tools.

## What you can do

### Bring a new mini into the fleet

```
# Generate SSH key (if needed) + emit the paste command for the mini operator
Fleet(action="authorize", host="RappterOnes-Mac-mini.local")

# After the operator pastes the line on the mini terminal:
Fleet(action="provision_brainstem", host="RappterOnes-Mac-mini.local")
Fleet(action="install_agent", host="RappterOnes-Mac-mini.local",
      agent_filename="twin_egg_hatcher_agent.py",
      agent_url="https://raw.githubusercontent.com/kody-w/twin-egg-hatcher/main/twin_egg_hatcher_agent.py")
Fleet(action="hatch_egg", host="RappterOnes-Mac-mini.local",
      egg_url="http://your-source-host:8765/some-neighborhood.egg")
Fleet(action="boot_federation", host="RappterOnes-Mac-mini.local")
```

### General-purpose fleet ops

| Action | What it does |
|--------|--------------|
| `discover` | Scan the local /24 for brainstems on :7071 |
| `ping` | DNS + ICMP + SSH + brainstem-health all-in-one |
| `exec` | Run arbitrary shell on one host or many |
| `read` / `write` / `ls` / `tail` | File ops over SSH |
| `ports` / `ps` | Listening sockets / running processes |
| `chat` | POST `/chat` to any twin port on any host |
| `mesh_chat` | Same prompt to every twin on every peer |
| `mesh_exec` | Same shell on every peer in parallel |
| `brainstem_health` | `/health` on a host's :7071 |
| `status` | Federation snapshot (self + listed peers) |

### Brainstem-aware deployment

| Action | What it does |
|--------|--------------|
| `provision_brainstem` | Start the mini's brainstem if not running |
| `install_agent` | Drop any `_agent.py` into the mini's agents/ (curl url or inline content) |
| `hatch_egg` | Push an egg via HTTP, run the hatcher on the mini |
| `boot_federation` | Boot the 4 canonical twins on 7081-7084 |

### Self-extending — when the action list isn't enough

The LLM can synthesize new behavior on the fly using the fleet helpers (`ssh`, `http_chat`, `http_health`, `probe_tcp`, etc.):

| Action | What it does |
|--------|--------------|
| `custom` | Run a Python snippet (`def run(ctx, args)`) once.  Returns whatever the snippet returns. |
| `extend` | Save the snippet as a named capability under `agents/fleet_capabilities/<name>.py`. |
| `cap` | Invoke a previously-saved capability by name. |
| `list_caps` | Enumerate every persisted capability. |

Example — one-off probe:

```
Fleet(action="custom", code="""
def run(ctx, args):
    r = ctx['ssh']('rappterone', args['host'], 'sw_vers')
    return {'sw_vers': r['stdout']}
""", args={"host": "RappterOnes-Mac-mini.local"})
```

Example — persist it:

```
Fleet(action="extend", name="probe_sw_vers", python_source="""
def run(ctx, args):
    \"\"\"Return sw_vers output from any mini.\"\"\"
    r = ctx['ssh'](ctx['DEFAULT_SSH_USER'], args['host'], 'sw_vers')
    return {'host': args['host'], 'sw_vers': r['stdout']}
""")

# Later:
Fleet(action="cap", name="probe_sw_vers", args={"host": "RappterTwos-Mac-mini.local"})
```

## Pairs with

- [`organism-lifecycle`](../organism-lifecycle/) — the prereq peer-side stack (`Twin` + `EggHatcher`).  Install on every peer mini before they federate.
- [`@kody-w/twin_egg_hatcher`](../../agents/@kody-w/twin_egg_hatcher_agent.py) — the same hatcher, available as a standalone RAR agent.

## Trust model

`fleet_agent.py` includes `custom` / `extend` actions that execute arbitrary Python in the brainstem process.  Same trust boundary as every other agent in `~/.brainstem/.../agents/` — local, single-user.  Don't install this stack on a multi-tenant brainstem.

## Environment

```
EGG_SERVER_URL=http://192.168.86.30:8765   # where Fleet expects to find eggs to push to peers
FLEET_SSH_USER=rappterone                  # SSH username on the peer minis
```

## See also

- [The Federated Twin Egg Hatcher Pattern](https://github.com/kody-w/RAPP/blob/main/pages/vault/Architecture/The%20Federated%20Twin%20Egg%20Hatcher%20Pattern.md) — architecture context
- [`kody-w/twin-egg-hatcher`](https://github.com/kody-w/twin-egg-hatcher) — canonical public mirror of the hatcher
- [`kody-w/aibast-twin`](https://github.com/kody-w/aibast-twin) — canonical private home of the hatcher + AIBAST team twin
