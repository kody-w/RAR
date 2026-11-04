---
name: "rar-cat-agent-skills-copilot-agents-news-scout"
description: "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/copilot_agents_news_scout", "rar_sha256": "0121f58ca0194995eceb2c1c014371e45312be27668c438506c656cc63bd9d96", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Elliot Margot", "tags": ["news", "copilot", "agent", "digest", "automation", "weekly", "teams"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/copilot_agents_news_scout`. The original RAPP
agent is preserved byte-for-byte in `copilot_agents_news_scout_agent.py` and in the RCI capsule.

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

Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `copilot_agents_news_scout_agent.py` and embedded as the fenced Python below (sha256 0121f58ca0194995…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `copilot_agents_news_scout_agent.py` first:

```bash
python3 copilot_agents_news_scout_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 copilot_agents_news_scout_agent.py   # or on stdin
python3 copilot_agents_news_scout_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/copilot_agents_news_scout_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/copilot_agents_news_scout_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/copilot_agents_news_scout/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Copilot & Agents News Scout — A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout
  Upstream author: Elliot Margot
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/copilot_agents_news_scout',
    "version": '3.0.2',
    "display_name": 'Copilot & Agents News Scout',
    "description": "A Monday-morning Scout automation that scans authoritative Microsoft sources for the past week's Copilot, Copilot Studio, and agent news and posts a concise, linked digest to Teams.",
    "author": 'Elliot Margot',
    "tags": ['news', 'copilot', 'agent', 'digest', 'automation', 'weekly', 'teams'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'copilot-agents-news-scout',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#copilot-agents-news-scout',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fc3502443ed8b977',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class CopilotAgentsNewsScout(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CopilotAgentsNewsScout'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(CopilotAgentsNewsScout().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZOjxpruX9GtEzFuj6qLVUj0iRNxkQAJgRACBAL3iTb7IvZNgMf/fRJJVW2P7TMzEffLVXdEsWS++a7P86ZSv7xYbRPm1cuXFyZJoryZHawqyJuX1xfXq50qKpooz8BbanbIM9caPqd5lUVZMFOcvG1mYHaeWtOYWRNazax2rKyePWRGDXjRebND5FR5nfvgbd5WjlfP/LwCw71ZYdXN7OZ51x/q2SYvoiRvXt8vZkrTulH+OrMyd2YFXtbMMu9W32+LvG7A1czJMyeqvddZEmVXz525UeABiU0+Uz0rrd+AFV5vpUXi1S9ffvrn60sErl++/PLiJFYNHr0816Im8bUIxN+tAtMSKwvA+2IAhmTgvvAqoHQKHrmeP3vefaq9xH+d/fu/X2/AafWPX75ms+fn68v0T26zu51NDgwF+jlWYdlREjXD24xKbtZQzyqvaavJZbO6qYBf3x4zv0vKi9k/pnefHou8BV7z6etLDlS4u/3ry48z4M2vL1U7Xb9NUopPP74l+c2rPv34XU7d2rHnNJMwoPXbt+f9UywY+H1o5M++KRKzea5VeU5UeED4b+ybPg/Vn+KeLvn2GPwpL15nfy55sucfQN9HetlA7p+LBT4AM1/e4jzKPj3XqPLOy6zM8T79+FdindBzrklUN/8juT89BIee5QJvPV3y4+s9fP+czZ+2fcj862ULkDD/G0vA8PflPhz1V7Lvkf0vokHCgzp6j+WfivuzCfN/zH76S9v+1YTXmf/1hfYSUM+VZSfel9kv9xT56Qf3+8Mf/vkrEP3filHuKDBJ+JZaWeSDkv327acfHuDwwz9/+qEtQBaDAv7WVsmfyfwzv97X+Z0Hn6M+/X4uWP+cXbP8ls0+amj2S178n+rXt5lmJZH7/Xn9ZfbbSpw+89lkxPuiDxf8phproOtv/Pjjy68AczJgTevcXwP8+NvffgOIDxAFAW6i1JuUV8OonoH/E2pUHvBrHQHHPseB/J8iPGmc+7Of/69jNZ/vyPi5vkZJUkPOA86+3R/W3ya8/FZPU39+m6lAIsDkIMqsZCZTkvQ1e6AqWK2ovNqrOoBQ9tB4n0Ehf54uZlE2+/kvZT6evBXDz3dMjh5QJ2+4CebqNvHeJoP00Mue6gNqmHm957RAcpI7QA0/Asj8Cgyt8wQQRTMZfzcFIDkAkiavhrts4KAvk7Cff/7Zturwa/bAZWz2YKgaAgM+1Jl9/gzs8ZMoCJuvmeeE+eyHX379YfYfs3816y58WkMCzPB0P9BwrxzFGSinNp2sn02xBFhxd/8vvz69CsRkXjUDwYr8yHtMfhDSu4uVHfUZXRAz2wOuBW5Ni7xqJhKNmrcZ588+9AWLTq8mOggBx81cr/Ay18uc4U6vX7MPT2aAIWuQc7U/vM7a2ruv+rNdWXcVU1DXVvPz7LCRAPnkyUSJ1ZOMwOQ8i4D7PxLg8RwIqQAPr99FvM3EKQEBSVdWEVbWcw3fesQFkM77dCDcmsj5azbxqze56l4ND/eAQcAzzjOkn6eYA+JOQem79fva9zHWRJHqnSqrr1n9zHSrmkLhAOQHiwZt5E74//dnStVh3ibu3X/eo6V4RsF9RuWeg+8dxb/NHkQ/m5j+KeFri8IIPvv/sr2ZbKO2W5nZUipDzxhRlY2Hz8HMZhL5runw1AnU1/ce5B1n3uH2a5ZEIIGq4e+PkfdIPcc8IKytgBYyJd/lgzQBPp/k3rN4ysqqmvLf+pq94zowb3YHMeBAUPKTEUD79wVfHzbeNQ1BXU/33zn+HvXKnTwCMnVWtHYCssj3PNe2nCvQqpoq8Rk/kNLeVJW3MHLC31k1A9JB5gD5M6BEBBwLsP/uOjEHZoJQ+1Wefh8eTT0Z0MJtHaBt6FXe20yfYg8SqgYVDBqraQzwwg93UbPUAz4GKn54uA6t4qFMXl3fFbTec8n7bQSeL7+n/12XSX0g1XKtBvjyNuGw6/WPyH7o+YwVUDadCvY+6ffhfto6+y0B/f1rdtfxA/oBDiQTd//GOTNQf+kjE6fEqwEUpd5HUj+S/O3BtA8q/9Dly2xDqY8imyl3Spp9St/L486L599H5cssbJqi/gJBH8PegqgJW/styqE/8NvfnmT0eFp/nirm852Mfif74YYvs9/taH434pmTX2bIG/wGT6+EyPGmpHt+vsza7ANKPv3m+hmxe0Q89xUU7YSRIGOm9KxDz733ILL3PaTvGDJ5egAE+0E/70MABwWVF0yDnyw7sdgNEOddNnD61+wj7M+iAPCeBRN31vlvivXOwyCIjxh90AR4lTVgbXdq1AJv2hYlk7m19/Ila5Pk9SWzUu9fbYcmDgAZCbw27Z5AdYCGp4m8+91H8zPd/H7TeK8bUPBu/mUqn9fZ1Ki+zj56ztfZ+y7gvlXLWrDB+mnqd6clwVDw52Psx47U9l7ATq4Ziknjx6ZparOe7e8flZiqBmgMgLmedHkvw2nFPwgBF0HgVX8UcrxfWMkTC+rGmlg6+uCPGujpgp7ndQZiBrIfFAvAwBZM+OMyYJ3KK1tAh+5k7nf/fTcrf9jy690NzWPn+cvLOyY8Y/DsBcFwUHyPMoBAPoMFwf0jk8C7/0WX+JwJ8As0K2AqjKCIv1g5FoyQOEkuPMezUQdxgMHYEvHwBYagtocuCWLl4NhqARMOsSAch8Bsl3RJAsh7ZOK3ie+jSRvbgX2EIJEVwHHSRlGMgFce7GMksfQtwsNQz13BMGx/n3oFpfY08WHS5L+PhnVyxdPSX15sAgcjd3jNUY/PBppr1lJfxsP+Qo6El5unQ8Wb2yIr8Hpfdt6YE1mB+sptdzPcyKND5ZDvbe7qnAc521SKVe96LpjL+9WgLsTe7s+k3FT1jlL33A2NBVPUGx3yY2x3rEhmXEE6CfXGHJeEOc4wZwcro8hL5NoYJN2xOMa/1stTujjrdc8mUdljqIm7/kJP9zWunBVn1RyF03InngtcPzJbCcpiqRdb5LhVErbKlHVzTFqNkSWZZffF/iBHXFtc+XSNFF3GXuJ9xJ8JU9GFyrR4neETs170O1iJNnM4Zg8rlMv6bTtPmbXEm5sCPXTj3OpMMdvb3QXPfTxWeTI1Wr+KCTPkT2zTRsPRG7cnyDNLy/Ahe1XDZKoPumpEbaSuU9kMzvDh0iaWcpmzC4NgdLdyoLM4js7J2YtsuBTJmksF277yeDqkpkn417MxKKbitef5GjVKKNqfYX0VEowR++bqbC4vHm8asr7lxdCOxE5za5e3esVm9bFfbPus3lICd52fBUlYrVozU7GltFfZ7WU1N4i5pZtx4picpoxNkFolqZv5jSdRlaPnXA2DOA29odnVIaYWi2bVpVdZglp6U5FjVwvapdv0bGsqLDqE0WqPzAU4pZeysQ6zmx3R0G2Xx+yFsOm4CPje6XYkota9gbCYFKi5aY6p6e2kUF4xwQWCrilaaCbu8CInqypeZ6hXnFWiIdkyzWEhP4QaIMFuL9L7SDhoAAx6YoGuMmho53G7Dd1Aposds94agVDSIL8oxje62mx2RWR3yBLKovkSa7vKzxgfL8a07/ybQUdRcMuhbnnp8GRc6agud/tbUzfwtnRsEi512bZU2emP4W4l4iAtYRRN8RvX4cekw5F1tk+6WLjcPL7Ol6O+PSvIIRCbk3huuOLAw/OIb6P4yB+CzTDMlYoroD6LCypJKHQUuZt403SHCczt6mTkJ5rG1Tp1N+rYQce2E0hy5fvLdjT9aLz4ndCtOnynrjuOY7Qs9zLG4AiWTp3wnJFUD13NfWIHuehouMIBBMH184VAr9y6kMOzXuaBtL6uzmFaaNf6kGxW8sXkK12qL5eKA5grSjaDOEbNcMdDyKBXGhZ6y04rrMeKlrpksEsQo7648CJ/OtD0wb2q55W0IS+KPPCNJshKbmC0ROXUXMGSY3ForsY6qsXGHFeba6evTf6gn87dCi2dG3pxTDJwdhWmo9bNjAs4JLKzlmxoFFNKMYLOlCcTuV1r+31TOj0qEdz6tOUMsePKG1I1MY+lqUqEia5qvpI3zaWgwXZc3C92WpAp23Z/3VNdsTxlCgddPK8S9HG87pQW52SgHbJE2hDfn5LmxtaL9rJrm/SGt2Q2yMPacVA23LJwXNtuKCdyOoyZlccoY8DVxmbYy7xmzVRA5n5n0/yex4384C60VKXXc5qEIXdNXWK0DC/FzpH8A24ipFXjubjCjSVZRtXpkuJXVOmZqLCJi2fu4bXQLVOO2knB3MUBtjt8nnckumqHUI7x7Hww8d7OVom4pFx2ofnh0TnvemtnlmkceaZXrnSeZVLVC5DApdYHYkx2cRmx1NJA9G1f1dS+LxcXoqq2soGWNblUOH+hyGxzhcIgMTfXouMc1+g0St8HcrRSgrrenbYSSdkADOIxqeuSNV1hdQZ0Y8sxhst2v6Y0aWuE1QE/LLptRmZw6d6KTu7JU3A127I6oKOPn8lsIUsGGV0Hf6j5npFu9JaU5cTWY3Zuk5zH47XV6WF88aNGLEpOdbYCQe6awzrnr/Zx7BRZIwxJiw2o7NyDv9gRg8HMWVtNreOWuWVJeZ1f6epU8iVtWcUiLGGT5JXLBha2ezbtrlRenKAWci1IU7cGvRASlwBtW2cJ8/WF0ThOZyAJclZFlBpBdWFzaiVip8V8H/XVkYLYLIQ0oV0wELe4yVhcXQ5+CgVkjVLaYvAi2shsyjU3jH2stL04phzrLI+MmIX0WRWOAjNoqO6A3RDKuJylikxKcc46EZy9oSFnIMHryGOSxna3lMIEsMsWsk7G7jQHqDLs4ptIn5ywWFBOaCDNwbSPCVBeLDEAlyc3851xGMdFHcnG9UAp2HrQmd4wG0Shuxu3TsgTHncLfm+pbbZFjKsVIvN5AkkXaEzFxbwkBK+CoGV9GPxblxc8XzZUfuPymhbpmGIbBNRx7miXWgXMYoacAUnzAhEKaqFJVh2VLTtoaZuz20C/rW9iOvZbPhvh9bncO+7mSBhXSbFtJ/d3C/Hi9PbVCQbado+7zh0vMqUcxj7Q4+3YHl1p55I9dOhRjAw2zQrQNqJiJoX4+pDtB0FX9CrRMY8wuf3WsVd4CS82uHNslKIyLvjixFqlugAdzyKlsex07pPLjq1uxpZzAVpsIIaVvD28EtXl+ahRJ3PTyNz26Ju6Zvny1kLkIUlPDXYdDGROHBE2r2F7x5bbMM4XHCJxbJ2SNmy5/KG4rOA9T8n8DoIJKExEmaGtoEo91eQBp7BUtWhQsYVlFzkt4jmGue1BsFP4ttSqC8nKrbQROYow2Pzg6al40YRU8uLTJrfxzbmFGI9bOazA5a5wKzd2nm0ohNOThdvtEnLpdiHUcknHXgu/sBKcol3RLxlEPkNloTH6Znc6uyZ12SRJqcRL+SybG1E3eF3ke2u1aIKj1Cjr48HkrJKtHSfWLWSp7R35HB9oI94UAYaK+nqOQG2pHNmrQImbii9Zh87LPNkPS42PjlddbGqA64Z2WMPiZrPHeZSMiRLumXZL1RyRj7pdNEnZLTWaOTpGpstpH+zEEt1JV27BsCZzOq8GH5FaM1KrGw/tQ1jLjI3sbCyGoY0m3+yueLG07HCbn4xUlnDUF9ahqrgqwuoWtV+EVHviTheeiMskuuY6FWjqQTvvmVg1d1pcZ7WSjavQCmuf6MhbeLFZ6lYsVfMwWgk6+PmGEprTrr6gTp77TquoQr8njEiYn9vGRvtEIk4jeWgGzWVYJ5zDOeFQgS2jwi66LZTLAUYsvlkUgirfmOSiXYdGl/ioz73bgGtx0edDsfU2Osb3FSqZBzK1o3kEz5fMZkAlxVeUhFmwCn3YrHumEM/LrYjQoGPe6iV+3DNJzK0PhXU7Ljf2pvZMsGkwaL/pIZnuokNYuz5AviQ6L8a2H6NDKaGBNRDrlX4VGbYt1YoiTtQAGjprWLdW3Nnn21YzxzBj1egSRV0uh31My1kkEJs4Ig0mO3LduVSZc3PaXMhNeIbL4ciqG3iRRcq8qvHQ2WYmczPDVm/X+1tFzItucUKCzTnu4Eo6qjq+Kg7Yho8a93DYibIxnHDtcJNFlLfyVeEigWnYUhIGloQZaaIQTkdpkVzmR3TwDqXnuWilZFphjhJRGQNlgA3VRVRV7JSoS3hHjxdmCdg5na9lcR9sqtCV6gDrXeaS0VOWblCxoKH9Vgeli/ZCHNvW/Fxk4lA2J+7qhgGi08mtWGUbxTyrK8rc1FR9PqBqvIdzNMTkZcZClchdl/naiqmwnoNtAb9A6S53U29TMGLKHXQeeGSod3TEpO1eSvCEPcJ0edaJ84YNHT71zvYWTVy935DN8ux17PqCOSzbX2SXZbRKbAwT0vcuo3s3XoliH9NZldp5YTDqS43YmeQuQCvR3x8Rr12qsd7NG9NaCOqybTy6ybqYmC8F+UKmRX9pVH0giRUZi6zMSaRUiF6FabRSkE5l5P4S9ijZiea33OYbBFlRA4f2leVzYzCYEXeoUlYQVbyK8e5mV6UVBelV1Arv0t5WG7LstjpL07UYraHiQND5blWX1pWWF9y8ifCDsDtBxla6EIztjKIBdpHtKPrH+cYJlNvKU/O15IqdRdzUqt9tNCxBEztxafG2gQpUILRhtaziDPKXItOmmnlkkHZF2WXI9dXSjm4W20Ae2IuA7kQieIhgYgoid6kHJedk71GbLLawG3WQdgx9DUmomu83a2jRinsTKVdNLGXygG+bvUE0+pzE6sNR2aJafFyf2mGeeed6ISe9Mgp4aLr2HCLoGkuSI5ZLaa/CrLIngiM0uBhCYkvNU7e8cwEYssoy29fyyEYhJxMM5LJNRjixQ49mM989lXoipYLnko54HDUe2S0JMRyaHeEkbekT/XwZn+nUFTg4TM9B1I7r2xwiFZdE3WwUVE52L9ZK3HJNKZEtf1hKaONLA95EuZuMCRX5koViO+DmtieWgzWM8RnfQE0lZdBVWOnJ0PnKrq03IsqE2HjsGWG5UuHNTTht+NsOgNe2FkZcCtdYv587QFKZrocrNT+aR7x3eXqzXNvKXkVyu78ucVpMLLyR0Thnx3y7aaBTF7Hw8lyOc21czCFvzTCBj1CuTmkHAmZzp6y6C7tgJII67I/0AeeN7Dzcct6n83BVVrvVMreqEokcsC8bEL9fKuhJ9k/uddu0+tJaMieX2I4OGfIHtVMuw2idtKvvh4S8C+GoE/LVrUD2Qr6kEa+zFjw+2uQpFfITjpOdR+38eZh5albtCDq7EbWXiBep7dJ53UiJbiD9olIDL8jEuS2mCwvHik2JdG3ZDEYRpysCKWUDNEjaQbu5IrwnpSo57cMLdZR9OId9TL4iR9hgzjS+lVCzP5YEgEfb4/BksPkSI6/EfmPLLn5a9oG4bsec6FeWWGBOC3sqCKWpLnFhLIvrCOP1YS4tlhZCDlmEkEtOt452ISxITrWQNeYvGopNVARsR+cpIVUutEiw9Mr6WOfD8WluKaRzO5XEoK+Ms0wdPfNqIAkxtmJ2uJU5LueEWVXOYXmWdgtYyNyGJnAObOV1dEnRAg1Abj4cxnk6sM6h2BQKqxxsnuVBsRNdK56D9f5CIjxBqOj5DGHl6ra+GooAcpQsLgxewCOiSCct9OeIwRv+bV8063GxWkU0rY0FK6ZScIkEvNIaL64ZedHn3W3Bau1uCEkt7fEBvRA2rsN00pRRfcWqbSEtNMzRXDghGs6dU/Z4ZT0/up733KiwtXtzSZhdHQ2v7482H2P8lUxMiPK9JISi2HKjEoKTk5cJmottL4v1yvLCKMaQojplGaPckrzCGhQzhk5InXbJH7GtLl4qaJMgantlKqaWin5kkxUZImF2potsb27D0NmtIV5QzALB5ZUn33xHbnSlaklJz/lqd94KWu0Uwrypwi6B4pIhZAze9Efy4Jg5b+kFMQY+sQ04bNXDa7xkM6TUNRbft6vD0SikPdyDRl7c7ipvGAaY2ARYkQ4a6Eo3gqSmWzhc8v42heqyU44+USa473oEl/fd3BTL7pjAhDFSRcV4aTzkW6cGneioDILNXi3Sj0Ebh0vuUeYvsBVvyHqpCFevUU6OvWzJZJd3kZfXg6rBC38MnLSDMPGG87m0EyFtkJSrJKyS3X5u7OMMsSMacYlrDtqq7TbUmnVY5vIFJ52yxhYxZJooIfBcgEM8mzbeKAxaqYekgyoKJKj0bhUo89tpm4aHRdjDFyWRYjsNPWZvZY4V7PvTQambeL0R6HnpHk6ijw/L0ICzi3C7mdQpA/tCfMk2rZQGKWvGx0RQ2oWNxSi5z46VrkLNOtiR7DHJd+PubPYnf12WUiXR47Etd6EFkcKirRDermxx3kktDwXlJtE5e9DqZOdAqYTYDs0P+4BaBrGBxevrMl6woMG9rnwSiwhSsa6LMpg3PdjQQbi3XUJ4fh3DMoskqU2GDHNgIhg9Gjrro9NBAZoRGHfwVqeuj+jy5u4wkVmyHnQs92HXkpdmie0u0JXrd+mQ3Py429L4vNi0DBRty36/pkS189kS29gGzWVRmRJUMPgm7EH0tSgJ0e0RazjI/eEaLy7UpWEaTmd93bsUsnQ9hKgr42cXzy8752pLRdxwST/6sbdCKUqQrDOW9Rmm5vXONPGWD0ju2GQx7QENifAK6jdkA5Iv961hBzq8dME2EGzZJB6bQ2kXXGG/uLG607Wng08yKY4pC5dZxvYiOqoAaFWc43fbalGhgwXoH6K4MyyJp6N4o6iX15fpMOZ5pPLf/3xi+qr7/9k37o8vx9+PUO+nKZ7lfrmv9eV/oMs/X18qJwKaPA4S6qQNnl++/9djhM9/eRY3zRseP0KYDnf75v2UqbGC6Xd4L9PQ6WjnIQBcPb7Bf315HHBPDz7O3cHNdIKeTG5qplPvScXn8R3QDHuD39CXX/8TRsUEBMcoAAA= -->
