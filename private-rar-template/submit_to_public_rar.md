# Submitting a Stub to Public RAR

Your private repo hosts the bytes. Public RAR hosts a tiny **stub** —
just enough metadata to make the agent discoverable, plus a pointer
back to this repo. Anyone can see the stub in public RAR; only people
with read access to your private repo can install the agent.

## The shape of a stub

A `.py.stub` file is pure metadata — no class, no imports, no
executable code. Public RAR's `build_registry.py` enforces this. The
two required dicts:

```python
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@yourname/your_slug",
    "version": "1.0.0",
    "display_name": "YourAgent",
    "description": "One sentence.",
    "author": "Your Name",
    "tags": ["..."],
    "category": "productivity",   # or any standard category
    "quality_tier": "private",    # always "private" for stubs
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

__source__ = {
    "schema": "rapp-source/1.0",
    "type": "github_private",
    "repo": "yourname/yourname-private-rar",
    "ref": "main",
    "path": "agents/@yourname/your_slug_agent.py",
}
```

## Two ways to generate one

### 1. Easiest: `action='publish_private'` on `@kody/rar_remote_agent`

If you have the brainstem set up, point the remote agent at the GitHub
URL of your private agent.py. It fetches the agent (using your own
GitHub token, which proves you can read it), extracts the manifest,
generates the matching `.py.stub`, and opens a submission issue on
public RAR — all in one call.

```bash
rapp run @kody/rar_remote_agent \
    --action publish_private \
    --agent_url https://github.com/yourname/yourname-private-rar/blob/main/agents/@yourname/your_slug_agent.py
```

Add `--dry_run true` to preview the generated stub without submitting.

### 2. By hand

Copy the template above, fill in your fields, save it as
`agents/@yourname/your_slug_agent.py.stub`, and open a PR against
[CommunityRAPP/RAR][rar].

## Skip public RAR entirely

If you don't care about discoverability and just want your agents
installable on machines you own, you can skip the stub flow. Use
`@kody/rar_remote_agent` configured against your private repo as the
registry source instead of public RAR (see `rar.config.json`).

## What submitting a stub gets you

- The agent shows up in public RAR's store, browseable to everyone.
- A "Locked" badge tells viewers they need access to install.
- Anyone authorized to read your private repo can `rar install
  @yourname/your_slug` from anywhere with the brainstem auth flow.
- Unauthorized viewers see the stub but get a clean access-denied
  message on install — no source leaks.

## What it doesn't get you

- **Metadata privacy.** Name, description, tags, and your repo URL are
  all readable by anyone browsing public RAR. The *bytes* are gated;
  the *listing* is not.
- **Server-side enforcement.** Public RAR has no way to verify your
  stub points where it claims. Anyone can publish a stub with bogus
  pointers; the brainstem will just 404 at install time.

[rar]: https://github.com/CommunityRAPP/RAR
