# Private RAR Template

Your own gated RAR — agents you can install from any machine you own,
without making the source public.

This template is a **public repo by design**, but you clone it into a
**private repo of your own**. Public RAR ([CommunityRAPP/RAR][rar])
hosts the *listing* (a stub manifest); your private repo hosts the
*bytes* (the actual `agent.py`). The brainstem stitches them together
using your own GitHub credentials at install time — you can `rar install
@yourname/whatever` from any box where you're logged into the `gh` CLI,
and bytes resolve through whatever access your account already has.

If you should not have access, the install returns a clean "Locked"
message. Same UX as an app store listing for an app you haven't bought
yet: see everything, install only what you're entitled to.

## What's in here

```
private-rar-template/
├── README.md                       # this file
├── rar.config.json                 # instance config (role: "private")
├── build_local_registry.py         # scan your agents, build private-registry.json
├── submit_to_public_rar.md         # how to publish stubs to public RAR
├── agents/
│   └── @yourname/
│       ├── .gitkeep
│       └── sample_private_agent.py # example
└── .github/workflows/
    └── build-private-registry.yml  # auto-rebuild on push
```

## Quickstart

1. **Click "Use this template"** on GitHub → create a new **private** repo
   in your account (or your org). Name it something memorable like
   `<yourhandle>-private-rar`. **Important: choose Private, not Public.**
2. **Rename the namespace.** Move `agents/@yourname/` to
   `agents/@<your-github-handle>/`. This is the publisher namespace your
   stubs in public RAR will reference.
3. **Drop agents in.** Single-file `BasicAgent` subclasses, same
   convention as public RAR. Name them `<slug>_agent.py`.
4. **Optional: rebuild the local registry.** Run
   `python build_local_registry.py` to refresh `private-registry.json`
   so you can see what you've got.
5. **Publish a stub to public RAR.** Use `@kody/publish_private_agent`
   from your brainstem to generate the matching `.py.stub` file for
   public RAR — see [submit_to_public_rar.md](./submit_to_public_rar.md).

## Why a separate repo and not just a folder in public RAR?

Because GitHub's permission model is per-repo, not per-folder. Making
the bytes private means the repo itself must be private — there's no
way to mark a single file as "logged-in users only" inside a public
repo. The two-repo split (public stub, private bytes) is the cleanest
way to use GitHub's existing access control without inventing a new
auth layer.

## Federation

`rar.config.json` here sets `role: "private"` and points `upstream` at
the public CommunityRAPP RAR. This is metadata only — there's no
auto-sync. Stubs in public RAR carry the pointer back to your repo via
their `__source__` field. The two registries stay independent.

## When you'd want this

- You write personal agents that depend on private API keys, internal
  endpoints, or proprietary logic and don't want the source public.
- You jump between machines often and want your agents available
  anywhere you're signed in, without sneakernet.
- Your team has shared agents that should be installable by team members
  but not the world.

## When you wouldn't

- The agent is genuinely public-good — submit it to public RAR
  ([CommunityRAPP/RAR][rar]) directly. It'll go further there.

[rar]: https://github.com/CommunityRAPP/RAR
