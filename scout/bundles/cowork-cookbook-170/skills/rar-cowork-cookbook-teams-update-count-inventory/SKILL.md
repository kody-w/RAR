---
name: "rar-cowork-cookbook-teams-update-count-inventory"
description: "Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_count_inventory", "rar_sha256": "c82441143eb98bc576890881e1441700504992b693f4b3b264583fa7ffdb5e36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `teams_update_count_inventory_agent.py` and in the RCI capsule.

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

Count inventory Teams Channel Update — Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_count_inventory_agent.py` and embedded as the fenced Python below (sha256 c82441143eb98bc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_count_inventory_agent.py` first:

```bash
python3 teams_update_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_count_inventory_agent.py   # or on stdin
python3 teams_update_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Teams Channel Update — Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_count_inventory',
    "version": '2.0.0',
    "display_name": 'Count inventory Teams Channel Update',
    "description": 'Drafts a Teams channel post on count inventory status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a19d51ba4e8ef04e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/teams-update-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateCountInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCountInventory'
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
    print(TeamsUpdateCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjSLLtX+Hl/VDVo6pkE4tqbMweAkmAkJDEIkRXWzWr2HfE0rf/+w0kZVb19MzcGbNnT7WkgAh3j+Puxz2C/O3Fapsgr16+vCielUEbK0nCwKsgK3MhNu/yKgY/8tgG/yAnz5oqtNsmr+qXTy+uVztVWDRhnoHpXGX5TQ1ZkOpZaQ05gZVlXgIVed1AeQbmtlkDhdnNy8D0Aaobq2lrqAubAOgCDxqvspwmvHkQ41rF/QtrVS7k5xVUtqETQ0C3dfVegWavt9Ii8eqXLz//8uklBN9fvvz24iRWDW693A3QCtdqPHbSKrwpBTMTK7uCIcUAFp2B68KrgIIU3HI9H3pefay9xP8E/eUvcWdV1/qnL18z6Pn5+jL9ObUZ1AQe1ORW3Xgu5FiFZYdJ2AyvEJN01lBDlde0VTbhUQO7s+vrY+Z3SXkB/W169vGh5PXqNR+/vuTABGtC9OvLTxBY+deXqp2+v05Sio8/vSZ551Uff/oup27tyHOaSRiw+vXb8/opFgz8PjT071r/BqQ+fGd7X19+WNz0edg9rRPMfHmN8jD7+BBcVDnA0coc7+NP/0ysE3hOnIR182/J/fkhOPAsF6zpafhPn+4g/wLNngt6l/nP1RbArf/JSsDwN3WfoCdQ/0z2Hf+/E52EmVe/I/4Pxf2jCbO/QT//07X9qwmfIP/rC+clICkqy068L9Bv35TDiv35g/v95odffgei/1cxSt5Wzl3Ct9TKQt+rm2/ffv5Q329/+OXnD20BYg2k0Le2Sv6RzH+E613PHxB8jvr4x7lAv5bFWd5l0HukQ7/lxf+pfn+FdCsJ3e/36y/Qj/kyfWbQtIg3pQ8IfsiZGtj6A44/vfwOyCEDq2md+2OQ5f/1X9AudKq8zv0GUgApNRBwcBOm3mS8GoQ1BP5OuV15ANc6BMA+x4H4nzw8WZz70K//17mz42fnyY5wM9HOt/bOO9/udPftne5+fYVUIDOvwmuYWQl0Yg6Hrxlgs4kTayDaq73qBpjEHhrvM+Cgz9MXwIrQr/9K7Le7hNdi+PXO1+GDlU6sMDFS3Sbe67Sqc+BlzzU4gGq93nNaIDzJHWCJHwIe/QRWW+cJoNxmQqCOwySB3LACy524epINUPoyCfv1119tqw6+Zg8KxaFHDahhMODdHOjzZ7AkPwmvQfM185wghz789vsH6L+hfzXrLnzScQA8/vQBsFBU5D0EcqpNwTDgHuBQQBh3H/z2+xNYICYDRQt4LPRD7zEZxGTsuW8oKzzzGSNIyPYAugDZtMirBvAyFDavkOBD7/YCpdOjibmDqXa5XuFlrpc5A5BqgeW8I5nlDVSDwKv94RPU1t5d6692Zd1NTEFyW82v0I49gDqRJ+C/ycz7IDA5z0IA/3sMPO4DIdWHGlq+iXiF9lMUQoVVWUVQWU8dvvXwC6gPb9OBcAvKvO5rNlVDb4LqnhIPeMAggIzzdOnnyeegIKcg/936Tfd9jDVVM/Ve1aqvWf0Md6uaXOEA+gdKr23oTkXgr8+QqoO8Tdw7fsDSSdLTC+7TK/cYZP+u/D+aBPbZJDyKNfS1xRB0Dv1/6yQmw5jN5rTaMOqKg1Z79XR5ADZ1OhOwj+YI1PX75HtyfK/1b0zxRphfsyQE3q+Gvz5G3mF+jnmQUFsBVE7M6S4f+BgANsm9h+AUUlU1Ba/1NXtj5k8AhTsNgXWDfAXxPIXRm8Lp6ZulAUjK6fp7lb67DCwbOBmEGVS0dgJCwPc817YmDIJqSqMn5iAevSmluiB0gj+sCgLSAcpA/gR+CBwD2PsO3T4HywQZ5Fd5+n14OPU+wAq3dYC1oJX0XqEzyIQpGmqQfqCBmcYAFD7cRUGpBzAGJr4jXAdW8TBm6j6fBlqTL/J0CpMfPPB8+D1277ZM5gOpFggqgGU38ajr9Q/Pvtv59BUwNp2y7T7pj+5+rhX6sYT89Wt2t/GdukESJ1P1/QEcCAQgiNuJNScOqgGPpN4zgEAk3Avt66NWPorxuy1f/tRyf/zPuvJ79dP+6LkvUNA0Rf0Fhh8V661gvQIGgEGMhIVXP4rX50eV+XzPsM/vGfYHmQ+IvkD/mV1/EPEM6C8Q+oq8ItMjKXS8KWKfHwAD+3l5+Tyfnn7NTt53/z6DYOLOZADV8r2QvA0B1eRaeddp8KOw1FM96kAJvDMp8MDX7D0GnhkyMcx1qoJ1/kPm3isq8OjDYe+EDx5lDdDtTn3XYzuSTObX3suXrE2STy+ZlXr/yzZkInQQoQCIaeMCsgW0ME3o3a/e25np4o97rHseAQJw8y9TOn2CptbzE/TeRX6C3vr6+y4pa8HG5uepg51UgqHgx/vY9w2c7b2ATVQzFJPRj83K1Dg9G9o/GzFlEbDY8aYinb+n5aTxT0LAl+vVq/4sRL5/sZInNwAOn0pu2LxldA3sdEED8wnyJtSmUgc4sQUT/qwG6Kk8QOyAXKflfsfv+7Lyx1p+v8PQPHZ8v728ccTTB8/uDgwHyfi5nqobDEIUKATXj2ACz/6jvu85FzAa6D3AZIfG5nMUneOevaBth6BIeoHQNOqh4DaFIAQyXywwm1zg/tzGbYycEzTuW5Tvuzbh4SSQ9wjHb1P5Did7MMtyaIdC5+6CskjHwxEbdzwUQ10K9xACSKJpbw6geZ8aAzp8LvKxqAnB9xZ0AuO51t9ebHIORvLzWmAeHxZe6JZ9hu1TIM2qZNb3OHnEtUJD0vrg0hWh7d3euW6sPc8p264wLqIfK01pzSPRQXJK3u0ZH9Hhi4FLh5El/NMuabF65yLssrF5EXMz08uyJC0URjilXjqGbUBjra6TthNW7tYuu/mZrmmdyOZFHCSFc7wdYKTOCnM463Fw09RQPBbRFlsP8XFEsFVxbk4a3ia5lHr7daGVpn4orNDda+vbyKVKr9aqknhrvyJWhVaYl2p9ITYFPfMNooMPOErBieLc8IKidSTHy7nu5oxMsTxIYXRrnFHCso3zbnU575qLeXD2t/VFrbrkknBLNJFDImkNPFyKDqnNEWEpl3EZt3qY31QWvdxci9jqZVtp0pDn0rVunG1x6luTJM8Dejx67dpKUDUYzUKoqi2xa3tsYXu9o1Btis9vSsfGg0occ/0sdqaYZsI43OZIl13KRNvENQkHuaXdTNTOhGRcS07Fnwc8Sg/XjTlfU5VInvLlTnUI42Bv5/xIKGEv1bN05biicvFniJpy2RmAtt7PWlMxtnLlhHqREsIpdnx62PYre9nM0ty1enegRfNS59U+xhSYxjZ1KWWuUY5axnhZ6cusJFhkeFQUgWjnB43WvYUrrm+Uzy+vBGO1LsabnEXDgm5Rzo5vFnUq2JrcajvztJD2u/4a1ES/WdorWeka/iJQs+GSItjQOpKQwuWuXK9WM2EPL67WLnCzIF+QZt3r0QFeIad2veAxWVJVuu9LXgjUTqvdTsHSQ+7LNq5H+94uSzZq/fEkeukhQC9nAdthykoqFFfXTxpCVJLtlOh+g1alBSve2Wn9otH9IzLzPD90/GvuC0fcmCUrzZDIA84tMV+VKNLy556RHzP9tDB4g5DJJlzzoWKl0lDPrVgLW73UrdjgVp29DmpNk+ejhonO7IDVEaWEjHZWYuqoBeRSq/hcY0mZ3cy887y8+KuyopYo23Y5q1zZ+d7Jw6JSIlbshZTgXSFixPQW6xxjHJVUutRVOvJceJElj8C3Ec3bdHC5iQ2TbllEjZlg3QtbAVttZBiT2iOaLbZqOnjFIj+nbr+JfOHQuSZWGVK74CvYxiKbkmklpOyZbWV6tYXjIZVQ4hSgRngQMDq0qq0dRawb8nvnjGyKZskttzRLL7r5zM7LrT+LyAxfNOPJPItaoZ9ue3Tcpq1OJlarhU2cNXSMO1IvV/wpg+HBs9TtpRq7JjwfDWTlZhaJF5WxMBRE7C1xu4UvDJvtVQKPFFY8bg8A3kg/zdSL6zSrVbXeMI26YCKSz7rl2bAlESgm5ysmhMnYiNwmXx9heUmdxFNp8jDKLATP1JmzaI02pc9mmkh0G2uV3yRh727XpZsVFuZqpVsEsnbkxbV+kjI1dR0LGxNJyCT/PLAZFjgCvvTWzlwKfEuu7bHBzo3YIJTYwwXKJWWBR5sZLrpbb4gRhhfbuhdoZlNT7KKElwezWlOnNneYhcyxxgK+HSmOyOXcO0RjOz/uJPOiYOgtjTs35igk5Y224FZadNKXa4Vt0nl8vMzKaK0ZFSdKR32pF4MbKjN4tQhX2zHut56/HXr3dsQuCxVsh6moQz3bcgW6ZcTOLriAUOyEseDOJvck5qBOtEVVWla0VBg3vTJSF7eVQVAlO6RguDhH9bWz0cua7VVbSGlZcKRlNx61UEzo8aTuS3Wwa3LbCSh11ZulckLHjh2O1uy8tHALWy2WZiYmc1AHXN83Quow6im+V1hDjKuNFc901NrYY+wRsj2a5IbpknVAzFG63RzW1RJFu1sthcExqCPeR2rY70dpXJx81JdOJoKNtNCy67QgCL/dat32suQWCu1sLXPcjmG5PEmEQ5bqnsGyzj+Nskg0cWwwSkW0gr5hI8+Wy+01KE+EiqLLSyHHaCi1+v5KFccO7VbUxei1TXIwa68Wb8mQJmaMXSUqD3UJb9ee0iG2c2Nbyjqa2xgUvnqZG/xa3ebldQn7K4bfWa4iaU27KUm1Uc4Ou6ka46AzRu0tr6e8Nljz5ormKfdIXvGEuEl3rbERdnan0Gh2MMRGTNNL3EftAovyw94iZ7clKhEVXLv1MTo2ewExV6WdoEgiOJEzOieOjI7mYUtRexeRtsuEWktr7IQQZM0r/Tq1ogMppCqVa4yxre0NHxTB9lqfl6JQZG2l6vvVCsR2BXoDO0mqZcRcT+U5IZxLL3AS3Yk8OVjtzOJvo7famtkQneS9gu73R3GzYAxanHFaXvDXYJdk2eBW1RHJzcV2z5oz9myTOYlq9m5T5uMKo4/oUF5mS34XzTvcIg6ndbBNwg6jxZRCTvyZWqniOW4SW1q1uw1xFOF6XN166WKT3t5CAre+2W570AyNTI00Vvd1IHU+1lY7ghdGF833gqTI1iLxD2ekRVwm2M+1ohxXCazmiUju0EOzWpv6PLRXndZfnWzYcAgsD/16XKZJd22vxrguRaU5HU8zidmgIzlskzo8bqIu7m0lGhtzFu9CQUuZdL+DZwNsGxmncJc2irXWG66ssTqI7RgMu4gmkyYkt5FgImHD4vDYL0jMXfTFRaNHXONPwQCroLLur6YTegtZtb1LGxv6YLtqukj5nSFg+onEZ/N9e91yUiaslnKvu0N8ZcUmYIrjvsg2Xkqiinr1+SN5TDt1i3Q4o92MZOHHl3HUw/OF3+0NTuPkvVbGY8dnYAulEPlKX/E8aiWg/mBrVivLhEJRtZ01xrbciS28TU4ljm2c6zpjLkjmNNWozzdaHJK7qNCXqmAthNnlokviPI8DvE/J4qhnW2Gzv563mi8f49KzfFS6aabcNmniiUSrnxGuN9YSwc6cyzp0VJs8JdS1aTOX71pla2lRwg+nYWX4kQdiYXfM2CK8pGqAsGQpO0SztbnYdWXljMvRVjFNaaOnRGTtaKnf9lzPnlBsKCmEoNV46ZN9Ye+kFdroRrVLS9QjRrHnzU17c6vcr4uMPG43lnxR2eWsdma7kubO3aaB13FH74Nq3fMxa1jc6JzPtAOXpRLOR96SWxQRXCNmZThWET00YHm1Vfcw16mdFN5Cm52rtZIl89UxJ1Nz1YmjK6jawV2hmBacRnVAgmGFSzOHcZkMpfEsMxDroN+4WYYcM6HWqBlTbFqvsCjKZI0AlIFhW+OFRebbNYuXMd6xLkMNR84UBAzhN8f1wiJ2nW+odJwjHIEeRXMVSKhUOnTdSDDjgYYy0vbWZh6pvkIYTiOlgLVn9k5r25lEiATOzQOxK2JS9dBlchIXFFXYvXJNOS/BXDvFx17QEX2fGEXcJUEVnZQgL5dY4u4ixz/nG4StknEMjrk377M1Ivqq1jP27jAmRoDgvdqArQ2Wb53NPjwsLTPRcvzGJUp1Oy7GG8rf5EbUBJajalYFxVL0uNsyksf8WuMn3/PgmGT75EAmF+kUM5ZhG+rQcidjmy6Y8ChvmPGyjJb6Wmb2sJ6Phs1ICXeI5zs42yJphpNIy8RtujNyhr+Ipu7H1RJT+Q01DMy2A15xhkuGIW52iNgw4pblrlf7zbqITogaBomTpr4WJzhMCLXt0j63QJjbJjfnKK+f8YHkhM1Va5n5zDJan5yVK9FBhUMagL54xvLnUb6dbcem1cgbEDuaUdVoO1Rmt8Th3KJqZvrcjFrOIhdJqPq2pmVdptzrdX5euPQejYR4ezoHuB1J1mJxJElVOjrrkBts0P/knVW6gL1ShB/THa5Ruq1RR1MuVmJpJioRk6Bzl2DpfDqcmMMlk5iyGj2Y87Y2yHWBEfa3JaxTRNQJsN9abUp2xSzD3dzhNgvEpaUNfIpvRFmOKM2xl5up44YmnVccTXKZo+Cy4dmV4EVjV8EzI8tgxtizN04BG3FYO9CUeR4jqsqwxMFTMagrchC7ZL6cj4zGH3VvHe2l/CCzAeEzkR7RK9LixWXUgf2jCfZSIrsvT1pPsDBzLaMhpY8G42jRIOUz2TWNqtBrCj9eB6Zybs7thOz5lrqi60pcM2uUgLfnxbyPcNbg8GU9mEFG8w6OJ1HWE0f2usb9/VrkZgIotm03WKfLeA7HOj6EM4rsb3GFci3oebzkzMZiHwUcnvk2qOIDY0kzd+mKvDkITX6hjFZeNC5R+SROGzzPbvTlYmHyNNNrsbq4wOx8zt8qefB957QP0Q2lcWMobDqJCoe0jyhLpjHeK2OsYeeH896r3T6ubpljN/Q1RVjlxowNnnsSYMN5Jpgsv5FW+OZI7vZ8hQl9m/oEiZlWIAjcruwP+NwIkyTUULLOsnqxlEfW2zjKSe2MtBUYjLYD/CIOqwOdDFkV3eTDDRDEMpAuB6PntnRZHG4k4h0ONwThVgecgc/LMycTlAaz+JJYOSvWlBzGOTpwK9nL7rLbhylb1D41u6btHCNY0YMjYa56V+8a0RcX29cSbhmXcN2uZnBWrN1QjcSLdChEzCCRunap4aoWjVNHMOt4IYwivIeTBG9muB0cDCboo3LOMzfK4mczeUnPreWN40IHvc5VYU6OBELgreSd2p7K50x/PXOm5rvXfdeSO3zXDiZetVlL4dZi4DitJdFQlipH8VWMuKwQu2PydsvdBJflERcT4+Nai2abw6l1+cqUovlic1vvylmJgsTqS+9I1a5drA6KjLf5APbUG9ikah+ncdOECTlaLhywBdtIR4OcE3AjBcSFX+xWOx8oT9CSwjE4kPujpYN8R2jPbyqQIaxDo+24OfjX2w2LT9xNX0Q2159vxTkwmZ7M593STZmCtkoqtnc+7YeXtd2AZlBCF4Nu5PxFnwmH42LP7NhE9HWYnsnyIsivZmVnhcwrhWdW7rDFUbta0fJttxYEFIuOhUodZIbPXcxnGO4UO2JXj85q47fOOeCLophhBCcVDYyVhIfJWJbW+nXPrm4cKVEH30TIQEWcQ0TmVYuIN9K+7fgdI/EsT/NKYKssvx/kks7X2I6MTURMObnOlsGiwOaLLZe2RCId/QN95fgz6GLb8bbnbhG1JhAmoc/cpumMrDU5m5cSGZBjtxjDyxF0XQV5u+2402o5jiUxHgsHvTjndnsgtKt+mCmpRlIEfpl1Yj+TYcbJlzt5XWDwZXcSkF4TGLVZrLuoz+NDeRAKGjlcpXXs4zjdOQGCFA3aOu1WIPkbwjeeVvgK2B4xzN9ePr1MJ83P8+J/60XvdIr3/+ww8XHu9/a+6H5U7Fnul7uuL/+eOb98eqmcEBjzOCitk/b6PFr8u2PSz//qDcM0c3i8M51eZ/XN21F6Y12nX/J5CTO3rRuguM6T9n5I++nFbuvptw7qb8/D6Jf7YtJiOtn+0fiX6ZcA3gxv8m/PX5m4357e1Hhu+Daq8a7Po+NPL+4A/BI69TfAHd+8qpiW+nxzMZ26Tq8uXn7/HwMoG1k/JQAA -->
