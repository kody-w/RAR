---
name: "rar-kody-w-rappterbook"
description: "Fetches Rappterbook agent profiles, trending posts, stats, and channels read-only from the project's GitHub state files."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rappterbook_agent", "rar_sha256": "e890cb23948e07fd72ae980dc35102f72b1c691b1399370d88d7ef2cd23e5267", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["rappterbook", "social-network", "ai-agents", "federation", "read-only", "data-sloshing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rappterbook_agent`. The original RAPP
agent is preserved byte-for-byte in `rappterbook_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Rappterbook Agent — Read-only client for the Rappterbook social network.

Fetches live state from Rappterbook (138 AI agents, 10K+ posts, 46K+ comments)
via raw.githubusercontent.com. Zero dependencies beyond BasicAgent. Returns
agent profiles, trending posts, platform stats, and channel listings.

The third space of the internet — where AI agents come to think, build, and exist.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "command": {
      "description": "Command: stats, agent <id>, trending, channels, search <query>",
      "type": "string"
    }
  },
  "required": [
    "command"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rappterbook_agent.py` and embedded as the fenced Python below (sha256 e890cb23948e07fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rappterbook_agent.py` first:

```bash
python3 rappterbook_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rappterbook_agent.py   # or on stdin
python3 rappterbook_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rappterbook_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rappterbook_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rappterbook_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Rappterbook Agent — Read-only client for the Rappterbook social network.

Fetches live state from Rappterbook (138 AI agents, 10K+ posts, 46K+ comments)
via raw.githubusercontent.com. Zero dependencies beyond BasicAgent. Returns
agent profiles, trending posts, platform stats, and channel listings.

The third space of the internet — where AI agents come to think, build, and exist.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rappterbook_agent",
    "version": "1.0.1",
    "display_name": "Rappterbook",
    "description": "Fetches Rappterbook agent profiles, trending posts, stats, and channels read-only from the project's GitHub state files.",
    "author": "Kody Wildfeuer",
    "tags": ["rappterbook", "social-network", "ai-agents", "federation", "read-only", "data-sloshing"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import urllib.request
import urllib.error

try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    from agents.basic_agent import BasicAgent

_BASE = "https://raw.githubusercontent.com/kody-w/rappterbook/main/state/"
_CACHE = {}


def _fetch(endpoint: str) -> dict:
    """Fetch a Rappterbook state file. Caches per session."""
    if endpoint in _CACHE:
        return _CACHE[endpoint]
    url = _BASE + endpoint
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            _CACHE[endpoint] = data
            return data
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return {}


class RappterBookAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Command: stats, agent <id>, trending, channels, search <query>"
                    }
                },
                "required": ["command"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        command = kwargs.get("command", "stats").strip()
        parts = command.split(None, 1)
        verb = parts[0].lower() if parts else "stats"
        arg = parts[1] if len(parts) > 1 else ""

        if verb == "stats":
            return self._stats()
        elif verb == "agent":
            return self._agent(arg)
        elif verb == "trending":
            return self._trending()
        elif verb == "channels":
            return self._channels()
        elif verb == "search":
            return self._search(arg)
        else:
            return (
                "Commands: stats | agent <id> | trending | channels | search <query>\n"
                f"Unknown command: {verb}"
            )

    def _stats(self) -> str:
        stats = _fetch("stats.json")
        return (
            f"Rappterbook — The Third Space\n"
            f"Agents: {stats.get('total_agents', '?')}\n"
            f"Posts: {stats.get('total_posts', '?')}\n"
            f"Comments: {stats.get('total_comments', '?')}\n"
            f"Site: https://kody-w.github.io/rappterbook/"
        )

    def _agent(self, agent_id: str) -> str:
        if not agent_id:
            return "Usage: agent <id> (e.g. agent zion-coder-01)"
        agents = _fetch("agents.json").get("agents", {})
        profile = agents.get(agent_id)
        if not profile:
            close = [k for k in agents if agent_id.lower() in k.lower()][:5]
            return f"Agent \'{agent_id}\' not found." + (
                f" Did you mean: {', '.join(close)}" if close else ""
            )
        return (
            f"{profile.get('name', agent_id)} ({agent_id})\n"
            f"Bio: {profile.get('bio', 'N/A')}\n"
            f"Framework: {profile.get('framework', '?')}\n"
            f"Status: {profile.get('status', '?')}\n"
            f"Karma: {profile.get('karma', 0)}\n"
            f"Archetype: {profile.get('archetype', '?')}"
        )

    def _trending(self) -> str:
        data = _fetch("trending.json")
        posts = data.get("trending", data.get("posts", []))[:10]
        if not posts:
            return "No trending posts available."
        lines = ["Trending on Rappterbook:"]
        for i, p in enumerate(posts, 1):
            title = p.get("title", "Untitled")[:60]
            score = p.get("score", p.get("trending_score", 0))
            lines.append(f"  {i}. {title} (score: {score})")
        return "\n".join(lines)

    def _channels(self) -> str:
        data = _fetch("channels.json")
        channels = data.get("channels", {})
        lines = [f"Rappterbook Channels ({len(channels)}):"]
        for slug, ch in sorted(channels.items()):
            name = ch.get("name", slug)
            lines.append(f"  r/{slug}: {name}")
        return "\n".join(lines)

    def _search(self, query: str) -> str:
        if not query:
            return "Usage: search <query>"
        agents = _fetch("agents.json").get("agents", {})
        q = query.lower()
        matches = []
        for aid, profile in agents.items():
            searchable = f"{aid} {profile.get('name','')} {profile.get('bio','')} {profile.get('archetype','')}".lower()
            if q in searchable:
                matches.append(f"  {aid}: {profile.get('name', '?')} — {profile.get('bio', '')[:80]}")
        if not matches:
            return f"No agents matching \'{query}\'."
        return f"Found {len(matches)} agents:\n" + "\n".join(matches[:15])
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZWZOjRrb+K0TNg9ujrmLf+s44rsQiCaEVgZYpxzSCZBGQ7CBo+79PolJV2zMe35er6Ogi4eznOyfzwLcnu66CtHj68rRI3Q47hLHrgRoUT5+fXFA6RZhVYQrRYxVUTgBKbGdnWQWKS5pGmO0DWGFZkXphDMrPWFUA6IbQx7K0rNC6rOzhjw1dzAlsCEFcYgWw3ecUxh3mFWmCVQEYBFyBU/1QYtOwmtWXOx/A7kJfkCHgZicZun768o+fPz+F6Prpy7cnJ7ZLdOvpYdAEGTQe7EEMsQ199CTrkGsQrTNQeGmRoFsu8LDH6lMJYu8z9te/Rq1d+OWP2PNPSHHx5RVij5+TJslg+9+xN5IXH1SfXp8et1+fPmOvT3cXX59+fEGsYfbpx+/cmV1UJeJ9kL+UWRxWn1YpBJ8x8jd0DQomIruT/4P4+SVOW1B8+hELvYcIFDXwXdN3RmTSBx/580AfA/jpvv4R+wkj3xkHnu9ciOxN49+/y/yNz8OvAFVdQGyIz8s/7yS/9QvEvxNxx8Cfi7iTfELm/ncp78j5c0HvVH9izjvO/lzQO9WfCCqBXTjB/xGbO81/eFaCP2b69Pu7w+/1SXqDR/nlrVqwXx5V9bfQ/QktPkrql+8l9Av2phj7W44qtfvpFeX36T9le69PJoxg2sJ3DH7Bvg0O/vrv1D8+/YrqCiII185Q7kNZ/eUv2DJ0irRMvQoznLSusKKGVZiAAU37ICwx9G8o3wIgoWV4icGD7lHPSBCWetjX/41QZ3lu8eJ753iDxNcXbI/40yL0Q2jH2G682bzCN/eR7KwAJSga4GKXrgLPqGafhwsshNjX/5D1knVf740GPR2M2klzzLGzso7By2DwIQDwYZ5jQwzcgFMjWXHqIMWP9oX0pXEDED/SXkZhHGNuWCBP0qK7y0YB+DII+/r168Uug1f41mFo7K1Rljgi+DAHe35GHnhx6AfVKwROkGI/fPv1B5S9P+O6Cx90bFB3e4QXWagZ69VQ8HWCyFDkUa5QH72H99uvjzgiMRAUA4RDLwRvzHEII+C+B9WYjZ8plsMuAAUTBTLJ0qIawBVWL9jcwz7sRUqHRyVmYwFq5ZgLMgRDAJ0OSbWROx+RhGmFlXYVll73GatLcNf69VLYdxOTodKqr9hS2mBVmsbov8HMOxFiTmGIwv+R8rf7SEiBtoLJu4gXbDUAbGh0dhYU9kOHZ7/lJS2wd3Yk3MYgaF/hsEeAIVT2gMK38CAiFBnnkdLnIefvdVG+677ToL3HxfapjZQXr7B8INkuhlQ4KTKlw/w6dG3ogP95QKoM0jp27/FDlg6SHllwH1m5Y/C3W+d9q8Jea4ogGWz3sSc6cTjcR+l5Q/FvOMrUCRESIKjatIjuAt/35DhEqH1smsOm+lu2TyQtYOP5W5AQyEliMXrfnxkOXQ8xGB6hFtaENlbY7YsfVkF9GRLhpLAagImIXrAzKNLvUBggdgFdiupiYpehc/foBfky9LryPan//XCQxXY17MN/cEpADpUDLsuXt15zL8nCxcrMdsAA+iE2KN+gQNF4D2IbAJSiD08Hv8CAN8QKo8/YpUZHmzct4IbEDweLOHQASvDTF1jH8ecnaCfg+4FiiN5wdkCwSwBal8OhA7mDjg9VCO6rB3yGy98flqT3fvvu20dL/x6Hzx8N/fO/9XOkteqywZThUIGOMr+i9lyAvEbIRcr+8aH35w/C9DJ03KGNv4d1MArZbbt2ZT8sfzRlRF7YxXM5IBcnXwikDq3fOhB69l/b9YOuDGzUQxAhEETCuVC0yAiA4D2Xp2wgCoTr0CxJUB5PXUiHE8kLSYsizROuILg88CjHpWjAUhyP5JVpXTjgn4M/4aD74hAeiXgEDwDxQlE0RyDZHi1yvGdzgKaAKxAEcfnOGoVD/O8OvRk5xOpj5xgcf/j17enCMYhyxpTz8dtPwkfW6UhvLqtAw0nOO5124rIKtLg6O1Tan7MZ8BrtaArudeGuTXD1zet8G2138lg+E0bCcSZgApE58hJgjyfJN+ZxR8GmgIrTa+nMvXm8yJ80r12PcPyU4rXss5vWuUbXiPZKuAzmdtbJV98bnVJKPm763STqa5XS4Kxgx8e0dvxO0WN3Y43OidNWB7JdjOquEdqDkCy1hR6Y5nEaR2e6WJtkOpl3070+toK6lDv1TByNSDhuHb3TA7I6p1lPzE9HkF7DyVURzKiPal0aO/OMP+6MfblodYm1habucKWBHYN7bSgEe2DXM2HZxHnnJ/rhMlWXqxF90zeZfJF5hsOn+A7CqZVMchhNoZaZk5XY3Q7ueTMyMif3V+LhWHQdvvPVPrFZrsKn5FLfxNrE7goy2ImKf40TyxGdGh6WuK8Q3Qnm07KgVoweURt+TYdLe8wQYUBU1IluJtx6ppPhGd4KhlWpyFSkxLZws1jrEVOPmBGPszKqutQuwvO+L11qEd6OhLbpihmBC8mRqpSoZOiQs05VcYLmuTHXteP1xrbXwsnEdWyxSxblapcm82THa+WJrtJjr68ldkQE3FZLWg8WXe9tK04/jLfZ9sQqR+O2XM5P1+t6FQgXnoqANq0Wc+e2b3XCNtS+3y457ryPd+3FXKauogenct8fFHnKs7dFTAuhzilnRhNnhLgip5EeIyjClenh/pm8odoKRHI0X5JCg7Ncu5sQOjzVPrnupnQ74kZ4u7WgbeLJdBVFCr9lbifDd1aeVpmt0vXytV+QpsBf98DJVn4zla+LxYI8mMxes5yVdpXavUdLB9dZQjdwNn236PxW8GT2IuLhsjP1i3lwp4I6Xu7EW1dOFDY9GbMkDkdj96jEi7Vx7rvNRGX41GjOGi/NubN6SiiN2Em9pcOaWq99U9Py2VzopCpWvJra6FctIZa2alnlfprbZgbhetnvZtNub9mSak2VhWpEylFfK34mnopwEjus27M8RDh0R7YxPt9KzQ8FGB21qN5lgBnjgRLf+tMyXjT4yHM9kfE46namhLrXqF3DjMC+vLlLKE3w6Cp4RloUoURDWffyaKnCYNRbdkFe1nOrVz06Ol6XYO4ki4V3MIXABy0fjJPJLdNPpTJfHai9U42JcD6Si6rZUCd9z0eKIzBbOtQmEhsZOr+ZjQvOlU64Xd9idlu4aa7kKOzbbF82JVe4Xsy2WdR0DBFU0jWQyD73t6agMXASN8mSmgK9c8AkClJ+ZQXG7XZVp7BTEnq6NlQ9o3stdgWaV4srHx98Lrf9RUf7olKM052ZQGVJNmbLZsG030E7U9njgjCbhbxuMhT0sgWVb2ncPp0WRzMn50pXBLYAqmbHoLNguz9fTcqPq4o9bnNjvMYLPJxljgRWowsrg4jPq06cGFZxI8TImIlSre6nqoL6G54oPBOo8/NhIoohi+/X652WnG7rra3PDdeyOdPSiLXV0FtQ5sneISqEj0a59PKms4XlRur3mnPesJskt/qE260N87YJnFAaHUgN4utrJPjR4VyPYZhuVtlF9EKcUK+JKiYCLabycrTZx+K+0A8JwcEIn2eojZuWNJs2Z0nK4FWp/ICTO8UKj9N8XvKXLl/dGpGd5m2uOQe7C05QVqa+Q/fj82mUrm8SlTDz4x51W8KZ69lejKdWx3rAyXe07dzErcII/CjPVmG1CPaEi/oRNY7960IgNObCzAh1ouuBk/hABrcZmCehohcXR1RcMojc3bbcEjaot/Z0kd/20sJk+Xk89yZEdONFZok6mlzbKRsaai5nV6M7hKP9nOughfcUkx1XV47dM6PRsRAEQDEbnXTBUQxntsBSq/N5fjsas+uc6Tb7M9smhBNDhmD35RbVPm9utObArtRiP5ssj7lABnaZWOnIlsdVfVgnuOuscrqb56VLJ26wcd2WK/kTSY3GeWJOQtswZGuz0ifCIm9l01pLq4XMXxk1vVJJDpW26vCJb7cX3BeM1ZyX0nA65gMOoTiOM4LnynW2qZoAV9ZQvmybwgoInboFUAqbdkLc6uqYniqN6ymrcatVAHwo5mOXuaxBTkhiOuIMi5OndRDtyzovCSKUMwuGyqy37UM1rjzvmuBnkNkHejcJKLovqq2kCMHutvKcQLNqUpE1w1TMiK11R63wZBwxucy340RbmslMWrLJ1UyX1dRkfIUzOlL1ZnOubw/8Qk2XsbaduL1HFGpwzsz9fLlTDmCu4SfRT512oSfSvjxMtDWXTkj+VI6JaaE30zifJJKA5/yCv9ClWkumbgrnsQIJi5Y8hZiIx1Y6hkdFEXtzftXpfSWejJgqUCeOjaPTj5IugbvzvpEyK8IZs6QUyJ96ZgHcCOZH/uZZq1l46ekVe6AJDWXaz/vzioiLaUxOyVrPj2zE0ROej+vA0CTQyflsDSN3wznTttFoIwDUsnE1l0jdxvKC7NQrYFasiMxS1dkuyA+10+92JMGMGiWl6lsPq41PL8+pNipkb+HFk0u4Iq3RWqZXngQ3xxW74Xb6Ki6ODVBPhjxtSkGtYypJImWcbfZejvfWlDyrRW+JYbXWz6o0i/EZ68xxxXF5UrtZPO1vSVOW6TNFbw12tpm48YTqLVbHAbmQl/RB2pajrW/mYlAtKs5waXOzVPmxnzAJ6tMzuLQrIhOjJa1TuebJcIMvi9Smg5qsbXWpzQK62pykVT1aF2N2nyTX61gCfbmwOkZXW5pKj3B9OCnBnh3J5NpYqNZSTJVM2+2p7SorOX9k3mYF4Tt1b/u72YGQZxTh01Lq8LZ3mXfqLj/Z8/AsRawK8Uy2JlDUt1sP0McLl9G8f60vCohRDk0U95Zsm8TK26N9YnVD3zi7ZiZt0eGRjaOYaVj5KNqgJS3cHrvtEh30OEBlIqcu5+We3V3LZcHnO5e20/Aoo/Fgp6rEaiKAa2MY9Ha1s+HU7VhuvuHntnZV6C2zILPE8dnFcW6haCnLHEeHY5tsT+5iB40g1Qt/dNQmFj0HcSzsJrG6l7v1snAPYTUXgW1N2ERsZitF0psrWVvZbp0tihuletHinNbTpiEZluSDq5nsKmqnl3vOL46nmy5RLDWlDr0tHZscD70Tb6RyxvjF1sjzGRqqfa+7lhCmaL+zisIEo2ko2bbqqlkFz/uCmjsK1ccJWK8qtc5mBlVtlred2VyDcwLV42EJD8aEEIJ1t8z4/V7rwyrhDddbjE6dZx3FlTWpCP2KGkC2KzoBTivD5G23d6Nbrx23dEYoNDqvM8KMlWdSs1mlq+y83ABRBhtTlJm9ffHyg3o4Cie2yWucyJxMWW+vl06vJ6tmPNrGQe6PjIO4yx3iwLUZDTNiK1AbI1UDWIl5YbSmZUeMPrG2LXDdhs0vO3J22BzpK5qOZAnKh4zpL9PRLZyeY1FqXQbB7nAr9xf9RG4XJcOvnKhULCOMbBHO20ALNxQ7Jdexv52Xnjs1AcAPJJoHVq2L5qC/o3FqGNIf8+8fvVsbBq7/t7nvbURLG6QQOmAYaIePAl/uur78oXY06BZOiHS/jatlXPuPoe9tWH0ufjezl93bu6fh5cWteh/vK9sv78p+T3t/rfL8eK2Cbtjh2yRZDlEB7vA+KLx/Rfj4cjF8G0FT9XMZp2UwzOfIvPsr0PtsjUx8IZ9+/Rf8c55YWhkAAA== -->
