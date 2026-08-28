---
name: "rar-cowork-cookbook-win-loss-theme-analysis"
description: "Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/win_loss_theme_analysis", "rar_sha256": "3c07691b700b5f096ed77c40f7b9b4fe17b139cf9ef6cb54f2c4282259605d50", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/win_loss_theme_analysis`. The original RAPP
agent is preserved byte-for-byte in `win_loss_theme_analysis_agent.py` and in the RCI capsule.

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

Win/Loss Theme Analysis — Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_loss_theme_analysis_agent.py` and embedded as the fenced Python below (sha256 3c07691b700b5f09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_loss_theme_analysis_agent.py` first:

```bash
python3 win_loss_theme_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 win_loss_theme_analysis_agent.py   # or on stdin
python3 win_loss_theme_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Win/Loss Theme Analysis — Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/win_loss_theme_analysis',
    "version": '2.0.0',
    "display_name": 'Win/Loss Theme Analysis',
    "description": 'Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'win-loss-theme-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/win-loss-theme-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47370683e39bcaa4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/win-loss-theme-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PowerPoint'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class WinLossThemeAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WinLossThemeAnalysis'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(WinLossThemeAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abPbRpblX+G8/mC7IQkLsaqiIgYEF5AECRILQcKqkLEk9n0hFo//+yRIPslul7u6IubDUHrxCCDz5l3PuZl4v75ZbRPk1dvnNxVY2WxjJUkYgGpmZe5MyLu8iuGvPLbhz8zJs6YK7bbJq/rtw5sLaqcKiybMMzidz6xkGEE9c5K8Bu4sL4q8atosbEJ4s8lndVt5lgNmFXDaqgozf9YEIIXPwmzWBcPMBVZSz6wKzLo8e6wPBTUfZn6VtwUUaA9wqlXn2QeoSFqAJoR6fJjdraQFMxuO//CYVDeWDz5B9UBvpUUC6rfPP//jw1sIv799/vXNSawa3nozwkzK61qbVHioXoeTTYmV+fBpMUCnZPC6AJWXVym85QJv9rr6sQaJ92H2n/8Zd1bl1z99/pLNXp8vb9M/pc0m46DVVt1A1R2rsOwwCZvh04xPOmuooSlNW2XQXqjw5IxPz5nfJeXF7O/Tsx+fi3zyQfPjl7ccqmBNHv/y9tMsr+B6VTt9/zRJKX786VOSd6D68afvcurWjoDTTMKg1p++vq5fYuHA70ND77Hq36HUZ2xt8OXtd8ZNn6fek51w5tunKA+zH5+Ciyq/g8zKHPDjT38l1gmAEydh3fyP5P78FBwAy4U2vRT/6cPDyf+YIS+Dvsn862ULGNZ/xxI4/H25D7OXo/5K9sP//0V0EmYwr989/k/F/bMJyN9nP/+lbf/dhA8z78vbEiThHWaHnYDPs1+/qqeV8PMP7vebP/zjNyj6X4pR87ZyHhK+plYWeqBuvn79+Yf6cfuHf/z8Q1vAXANW+rWtkn8m85/59bHOHzz4GvXjH+fC9fUszvIum33L9NmvefG/qt8+zS5WErrf79efZ7+vl+mDzCYj3hd9uuB3NVNDXX/nx5/efoO4kEFrWufxGFb5f/zH7BA6VV7nXjNTnbxtZjDATZiCSXktCCFc1Y/argD0ax1Cx77GwfyfIjxpnHuzX/6380DPj84LPdEuzL5CRKu/PmDvq/UCnV8+zSAIwVoO/RDemin86fQlgxiWNdNSRQVqUN0f+NeAjxB+Pk5fJtD85S8kfn1M/lQMvzwAMXxikSJsJxyq2wR8mmwxApC9NHcg8IMewjKUm+QOVMILIXB+gDbWeXKHODbZXcdhkszcEOI3BN7hIRv65vMk7JdffrGtOviSPYFzPnsyQ43CAd/UmX38CK3xktAPmi8ZcIJ89sOvv/0w+z+z/27WQ/i0xgkC98vzUMOdKh8hWfhtCodNHAKB1nIfnv/1t5dPoZgMUhmMU+g9SAjeg5kYA/fdwarIfyQoemYD6Fjo1HTirImawubTbOvNvukLF50eTXgdQFaCZFWAzAWZM0CpFjTnmyezvJnVMN1qb/gwa2vwWPUXu7IeKqawpK3ml9lBOEF2yJOJGKsXW8DJeRZC938L//M+FFL9UM8W7yI+zY5T7s0Kq7KKoLJea0ByfcQFssL7dCjcmmWg+5JN9AcmVz0K4ekeOAh6xnmF9OMU84lZYdW79fvajzHWxGHag8uqL1n9SvKJqeFECPpwUb8N3Qn6//ZKqTrI28R9+A9qOkl6RcF9ReWZg2GGTiw8e9Dw7J2HZ19aAsPJ2f9fLcWkML/ZKKsNr62Ws9VRU25PR0590eTwZysFWX4Gs+lZNN+Z/x033uHzS5aEMCuq4W/PkQ/3v8Y8IamtoIoKrzzkw9hDR05yH6k5pRq0GJpqfcnecRpqO3uAEjQW1jHM88lJ7wtOT981DWCxTtffOfsRysqd7IXpNytaO4Gp4QHg2pYTQ62qqbxegYF5CqZS64LQCf5g1QxKh+kA5c+gEiEsGIjlD9cdc2gmjJBX5en34eHUCUEt3NaB2sLGE3yaGbBCpiypYVnCdmYaA73ww0PULAXQx1DFbx6uA6t4KjP1qi8FrSkWeQoT9/cReD38ntMPXSb1oVTLtRroy26CVhf0z8h+0/MVK6hsOlXhY9Ifw/2ydfZ7Qvnbl+yh4zc0h8WdTFz8O+fMYFGl9TM5ITbVEF9gKTzNg5nwoN1PT+Z8UvM3XT7/qUH/8d/r4R9cqP8xcp9nQdMU9WcUffLXO319ggWCwhwJC1BPVPZxIp6Pj3L7+E48fxD39M7n2b+n0h9EvHL58wz/hH3CpkdS6IApWV8f6AHh4+L2kZyefskU8D20r/hPcJoMU6G/c8v7EEgwfgX8afCTa+qJojrIig9whZZ9yb6F/1UcELszfyLGOv9d0T5IFgbzGatvHAAfZQ1c250asOeWJJnUr8Hb56xNkg9vmZWCv96KTPAO8xL6YNq3wBqBbcwEfNPVt5ZmuvjjPuxRPbDs3fzzVEQfZlP7CfHtvZP8MHvv7R+bpKyFm5ufpy52WhIOhb++jf22ybPBG9xDNUMx6fvcsEzN06up/bMSU+1AjR1QP3D6vRinFf8kBH7xfVD9WYj8+GIlL0SAKDwRcNi813EN9XRhO/NhBiMG6wuWDETCFk748zJwnQqULWQ6dzL3u/++m5U/bfnt4Ybmuev79e0dGV4xeHV4cDgswY/1xHUozE64ILx+5hF89j/t/V7TIITBJgTOmzsYQ3O4zWCYTXkYRwOXYRwS8xibs0kP4IyNzznH44BHOzZFeoRDEixBUByNUS41qfFMwq8Tj4eTKoRlOazD4KTLMRbtgDlmzx2AE7jLzAFGcXOPZQEJvfJtagzx72Xf057Jed/a0MkPLzN/fbNpEo4UyXrLPz8Cyl0s20BtJZCQKkH6fk6f53qhE3dNlZELW8o13Z4Xx00UUkJXXElhvkvsM94bBqWObXmzeDSvkO6OqIBQAEQ8NabBhreQJX/I3MxNaC+9xGVYSsoGz+R7srZqzq1qRawbWVtf4vvRu8+pNeqJGrYfq/XColb9JbGKo47lEevysIto6EE7LaxihbvqXFprp5WiHc26uONJawhrquqNircv2g5Q/nAYtypsmy76bRe0Z6fE96FT61Sz32wS/WSI1/vGX6nMGr3lKUaqtRJhVqZRHMiWLOdd58hRa1DWq8KWCleL9FIom/hms72Fu7uauEiXFa/sTWkMS3XMNx4t2PuhaA4bJcVXAUZVV4J1WxLfGtt0XAThbdTOc0qKybsk1q2Kr+2mkVbMLl7caF86eZAxsZZa78+6yYEQD/b7dVgyfKQf1ls6wtVllrY1jl7mFzop9buoEfr8Irc5091XsZTam2QlZvt6uG8XPE25eliotaivKutCXAtR7GyZM03y0Pn+8sq4yXJpCt2VI3duUmm2a6aBJVCDd+yz+LptrF4ej2nQGEf6kpZqpC8BsUDSkxRusJW9a09GfSqPFuLs9iVSl7u+rlDLEU70pQSX5Lbs2WU/PxdL/XZwR/se5YvkdndQ0QD2/jKOtXhOKR+0wLh6Lr3UxWbOGyPNOtG+b8LFxSLmIbvP6n2f6cZt5V02LRbqlHlJLdLwXaJasHRZHLoc6xPGjGjMd+ZWWu2LTE2IBDkg8tWHG6HSIc/1DknaYyeMKQtp+qC3TcSexqwqUegy/FAAMBrGbXfA2Ou2v6QhH5iCRjAx0HXZkrNjtUnnezfLqHocdz2XrhbcMqJaChk1ZCWyvHD3hlV/vp4KFDtRNdJc5hiL9LKUnzNd5obhYoL4blbS0brE9qkrrFWFW7hxFNP+VKx7TjfIW5OIq2IjMheZw9JzdU2pVZYLNqoMMXcOxDG/dvYlKc+jZgj5MarJhFisN8pWwHRzv6pWnerWu1ahlVWxlG/xyh3XjcGWpWlkixiLQrO9g7Ptu9c+YUkXQ/gTG6+FUxzWS0ryfWaTsdwtwmp067VrSsouF3aDqciRXjYyTpC3MTM8HL0Z7BmrdWvw3ABT7LzThyWS7Q/VBvU5gggv7uY8tofdhgbHRbMUsK2QLiW02GhUu49lz9+oIZdz2E7ba5vdlSUEP6IF8VR1yd5B85q3z1Ww47KUQAO+yApK3kSnAVhrbH9a4zRY7jaUfjeMo1wojSchhLgU6rOyafBqqQf3odPMujwYp8ga1lqsUNotb4yUM/h6YZh33jjdEKTYC3ZxGaVxcxEoyUX6NU0E6iJFUfOyreMkrpfshtuc7L1fydDTl0jwJJJrjuFqfpIORwBRxi0La27ptVYEcnyOzPUlGA0tBJYqS9mGHyrkqvZLyrP3xQLsHHS8c43cniiayZWYYI6MzsWMP+AxdorQKxZIZzNwiEWm9wBjFTwnVGfPxQmGWcOWCcjtSY9GtDwBnu3E1rudyeYAzk1wXOibxi1u263Y+Nk12hZaH3P9uF5vyVgh50um2A982N0rSWlocn2Tl010nc9FZxsdCX1MjvEenOa1SxBkdln3dmKBUpLMsV+Y57MgbrErqm8GbaWRwkk/bJsNQTlF3Agr7NRv+J3cUMa8cqw26aIjvyvlBMJFvyqXTFxcjG6LmcQ93fILx/KVMlWP6A2rqlxo2GPLUDavp5pRcMVtrew7TqmZg3tlGfVc6iOWXYnRlke2B/cxj5M03CfCGczvJFux2pKt1Opi5ujSv/hhYbiBh3bLWgxYfH6qpUCZCgbpncNdjEZ6gLqye67o71l2SnhWd1WhLC+sRfRbfpv4ClaY6umwOuqr8+5QJXpqHnlVsBlil3WXFX5m+CTeRPK1XFb9oUwPQDsHe62trfJsFnui0Xxm4VCy6JB0I9xqjSiTaEFqnO+xWZDjrhdytExEq2xNEuTApG1AjnSAJlV62yZjYqUYdkqF7GreBSHXan7NxRDQGkUiYmxrqFzYXY1Vwnv9HqlUiDpGV6XY2kWNTGvBLmVMZ8M3pCSUS+OwI5A4viyIhpAP82BvOxZhygvMvOwr7pTZ2kLFUNqgIZ5KC5Nw3Nv+IhGoOJcsZsevhdphDBJ1KdJgBCRRWwyL1gEH+Xq7F/aE0HH4tj0vG+JmamZclH6sCcfm3lT36BxgETJkGmvt9APAcrDZ1CeFKNejueLiysGwMxnS64bZnwt/4LX9mi98Ij30A51L2xMhtWq4Rmw/qIRWlPaH8lasu8W2w6Wa9duc5uIRjxbpuLPBnNQvViAn6nh2JHLQVPKSwv8mawJTF2pL3omHiBPmZX/ZXnsmOB/YHX4nSg9tlLrQnUO0xAwk0JiTQl6NNFbVam+qgnUL3OZu4a1tXG3LAipXlkluQyolaoglpQuoTd5vbmNINP1l7oWoZ63U2xzfCLDeI2WvYabgKKHpBmO0TdedsKQUGMwRqa2OtBNqMSorp7fpQ7WOQ2On7GV9t3Kt9aomBfmCYLHEOTa4os3GSEXLN2jXQ8imibSoCGpPGSB86Q5ft9Jgy50XQZwv7LIs6wM24g3DkqiKZyjWsLJ641ix7Y7LqsAOq55lzjKSHRsQG8WaA+W1Y+5mYkqDCdv0ynZTtDOVgF2px7zHKSzp1MNhUYf+MfHlyh2bhS2w9hK5Sdn+vL0NmxuiXgb0NBLReaMcnJBfuDdVyGxJbzL2dHHoc1Jt1isF5LBk16RLboRELtY2flLb1pR0V8hv66EkXIlZ8Ji43Nrd1TtWoUof3VoqQjl1eKNr3NFBpSOkSTLWyzpufPzAOANv0na+os2FhGApq+g0Pd/bVGacjShfsq0Fg8CSnRu1O3CQceamKZbiYLFF554myrrUrxCWYm+3uIlSKdKTnacFJr1acjTHXy5nXDyjq6iMXVwOr+sCUHpHytvOimkIS2spFel1n/UCHdPNwSbSai3lmmTFpws08G7g1O1sBUbl24edHVrXCFXpotQKfVt3CbVabKlOuCU0Xgl9JI+wJSKIuUIur14r7qMUPYuJUKgjsm9IjBrNra8CSrqGlclZmKtc76G9dRZz2wpth9lsz0O833X9eFptxT2Q4ghma77e3baDUUgWjpN4vTA7OVscKvYOWTq2+1ipXJp3ECsrBlkGuzNm6yvCE9Ikt1RejEsiFwC/J0Y+WDZFKtZKu7icE524chWyqi+CWZyp3fE8KltZGWgsYU/lvLzyuZrKByZrF7qVE7C85qS2tCHlMPNBgT5zhaI9mng6WH6T5wA1Ry/Ub51dnPrxdmUAJrp4fK0bQVwWfbnj9yu/QPcXvVwrkWNnfK9VLdEIARNtrtmhYNGrtanOtIrO2egW09zgHq1VuFiehIxoQLoLuTpyasna3G1k2xSw+cuEldSSmsyShwWDsBuBMUJhdBccRbcre7nce/hu9IOjn9cNFg0Nbuo53wVmgIkLOEWPt47EHUWBrA4X39hv7PWQO+VlR6B4ffNx5+ryAh2RqQE22RqE8vZKi/zejAO+LXovCGlkuSwgUKj6Tb/7jrNrpJur0UVgSl20KruScu/mKp2fTzd1f+wW4vWyxtfeZr/NhUq9GzFjH9rzTs4X65TVN0mIYAlxWMHcbxnUzJlTqOlAVLyFzbilgwZk2SfyMXHFZlhyKppJmXNdY6d9prY9b6zvth5kjs76nKfJjG4wmm+ojL+5uMYNI1x20QzbMZJatgUYD+QuLe9mzsKiVlAfbj/kPd7FeD1Xi3W6oDp/m8OMuZj2iTos/BPnDhfQtZ1ojvfQO8rgiGa4ICJi6XlGt5JFUZl3Bxuhw2GOE3IT3DyZWYvAPYvm7XRXHLvTiIEh3PyEA1lhGJxDESVGrf1tr28qlOrRsKC83bxtkZyh6e4yxKBPjhHILzFPRCMuxhyxHUJDMQlllTi5rKO3s7m91ZurHTJIRARrYiFGWXpgdNcH+thGlhSlp96Eqt3jAywHary3StgRjZoYPXYUW4rHF6W2U8aSO+1VjlRHa9UKraKrZpBxS/U6xzMLSbrj7doMa1j5KBjPrNvH621+V8KxXt1Dg6G7eyzhy7YeVcO6q+6uj8ASzzwRLHx1BSTEXTiNPI8DSUeIynEyFZWUe39HwUkPxWTtchex5vtbrM1rrrpDlvWZhuGyXb1vrxbrHhb2xTPqKqXSpmKI6xqSieu1gjAOqK6zbjM/XsW5t4fJnuY+jzqcNlqHFXIzPSmU1ra1UV1lzzqn231NL5ghIVbpYntYgqFDgQL3SUjpntYQQC+Y0/KnyHa5jlqdFm5l8ce7WWjEOr8lXCjrd6dgScRZkLlxuOc7Tzey5rrjWGK5oDhuXYMewRb4dmcQBZifWubG1rLPH5jKyEu7nvuqtBi3dVCuQwqw2WUftN1orxgGOWiRTNu2cO84oiPuJ3d3aTuChd0iaJP0WJuSYnP5pvcKZMBPorFhj1WzRXsbdvJIu6UI+7pnzqPXHgd6Ja+8q9/NESzgqr47RktlThJ9a/NgNchtAxr3bofXrKoBmfKH3Zpn9pHt961wLWGnw2wzI6UNpnD3eH6jG3wH9wD0nM8w977mU97hw5DJic7DxKrSNos1jygRmm8UCl9uqVNAcztcJDTPOMzTCO4wUtfZNuR5E8wrWvaRBWMy8Z0BcMPjEVdMq6oOFOSRrA/cfHBcNWAUq88YuTbBFeBIyV5BchS2bSkyp1Pb9i5unWx7Oe4ZL0fRAemvfXxE5s6uTQrAqYcdGTJdoK14nCwrLWeqOXscallpdORWaU1atWSJ+EZ2wgMi0tC6Fq/9jUXnYbvdHFABdaygZO8amZv3RgNS48vjHVhRqdKdfrwgIres8guG+vwmsros9BMy59blElsNaxC01oAv7giXSD1FrIDaXXzyBgFL85KROonOASwD1jOPnhGcvF6GacYvzDrwls05afxlwG0qp7gnx5o43o4EFS5Oh7sQ1AF+AMVSu1/m0vkyBxg41DmNMABmF3Jqr+lZuPZaDTejLDXevBt1hJ3hMRRbx2AkI6I4Au6JYCJ09obd+4lL5EHS0BWtk8SGThA2FrP59cCK6fFwXzCkSC9NMWQpsNpsY9qzlj7svxe+gsbmftAW0v14apOwlJfcKIqOE4XJvd0NtBdhV5Znx+ve0m4Fz/N/f/vwNp1Hv06V/9XL4enA7//ZuePziPD9XdLjQBlY7ufHWp//pSb/+PBWOSHU43mSWiet/zqA/C/nqB//4sXDNGl4vl2dXnD1zfsJe2P509//vIWZ29ZNNXyt86R9HOB+eLPbevqrhPrr66D67WFCWkyn3jmUXz1v1AVwmq9N/rVs8wbAe5Z7n4ycTkxDuJj/Okj+8OYO0PWhU3+d09TX2pr+9Aha9nqJMR3FTm8x3n77v7UR+rdzJQAA -->
