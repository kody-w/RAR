---
name: "rar-cowork-cookbook-configure-manage-loyalty-programs"
description: "Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_loyalty_programs", "rar_sha256": "9e5b93881d1d3e221de69d53c78f7c006cb1cf6df909f2bde460289d4a8ceff5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 9e5b93881d1d3e22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_loyalty_programs_agent.py` first:

```bash
python3 configure_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_loyalty_programs_agent.py   # or on stdin
python3 configure_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Configuration Bulk Setup — Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_loyalty_programs',
    "version": '2.0.0',
    "display_name": 'Manage loyalty programs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to manage loyalty programs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b20f4a724994b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureManageLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageLoyaltyPrograms'
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
    print(ConfigureManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaeZOjRpb/KmztH20v3SVxiKMnJmLRBRISQiBxuR1tjuS+Lwl5/d03kVTV7vV4ZxyxEavuihLw8t3v914m9euL3bVhUb98flGBnSO8naZRCGrEzj1kUVyKOoG/isSBP4hb5G0dOV1b1M3LxxcPNG4dlW1U5HA5V5ZpBBrERpwuvdP6UdDV9vgYcUM7DwDSFkhm5zb8lhaDnbYDUtZFUNtZg/h1kUGhSJSXXYusri5IET9KwUfkErUh0ttp5D14jZrVRZo6tpsgTVeWRd2+QnXA1c7KFDQvn3/6+eNLBL+/fP71xU3tBt56WTz1Afu7AruHfPkpHi5PoYaQrhygO3J4XYLaL+oM3vKAjzyvfmhA6n9E/uM/kotdB82Pn7/kyPPz5WX8p3Q50oajpXbTAg9x7dJ2ojRqh1eESy/20CA1aLs6Hx3VQG/mwetj5TdORYn8fXz2w0PIawDaH768FFCFuwO+vPyIFDWUV3fj99eRS/nDj69pcQH1Dz9+49N0TgzcdmQGtX79+rx+soWE30gj/y7175DrI6oO+PLyO+PGz0Pv0U648uU1LqL8hwdjGMQe5Hbugh9+/DO2bgjcJI2a9l/i+9ODcQhsD9r0VPzHj3cn/4ygT4Peef652BKG9a9YAsnfxH1Eno76M953//8P1mmUwxp48/g/ZPePFqB/R376U9v+twUfEf/LyxKkUQ+zw0nBZ+TXr6q8Wvz0wft288PPv0HW/5SNWnS1e+fwFVZp5IOm/fr1pw/N/faHn3/60JUw14Cdfe3q9B/x/Ed+vcv5zoNPqh++Xwvln/MkLy458p7pyK9F+W/1b6+INlb/t/vNZ+T39TJ+UGQ04k3owwW/q5kG6vo7P/748htEiBxa07n3x7DK//3fkX3k1kVT+C2iugVEIRjgNsrAqPwpjBoE/h9ruwbQr00EHfukg/k/RnjUuPCRX/7TvePmJ/eJm5M3LARfH+j39Yl+X9/Q75dX5AQZF3UURLmdIgony19GyrwdhZY1aEDdQzhxhhZ8gkD0afwCsRL55Z/y/npn81oOv9yRM3rgk7LYjNjUdCl4He3TQ5A/rXEhCoMrcLt2hGnXfuBw8xHa3RRpD7Ft9EWTRGmKeFENDS/q4YHKXf55ZPbLL784dhN+yR9gSiCPPtFMIMG7OsinT9AuP42CsP2SAzcskA+//vYB+S/kf1t1Zz7KkCGsP6MBNdyqBwmB1dVlkAwGCoYWQsc9Gr/+9vQuZJPDxgZjF/ljoxoXw+xMgPfmalXgPuEzCnEAdDF0bza2FojQSNS+IhsfedcXCh0fjRgeFk2LeKAEuQdyd4BcbWjOuyfzokUamIKNP3xEugbcpf7i1PZdxQyWud3+guwXMuwYRTo2yPrZQeDiIo+g+98T4XEfMqk/NMj8jcUrIo35iJR2bZdhbT9l+PYjLrBTvC2HzG0kB5cv+dgcweiqe3E83AOJoGfcZ0g/jTGHTTyDWeU1b7LvNPbY1073/lZ/yZtn4tv1GAoXNgIoNOhgs4bt4G/PlGrCoku9u/+gpiOnZxS8Z1TuObj/k9Fg8d0oMR+nCxViSIl86fApRiL/v5PHqDnH88qK506rJbKSTor58Og4Lo2ef0xYcARAYFo9qufbWPAGKm/Y+iVPI5ge9fC3B+U9Dk+aB17BWvcgQih3/jAJoEdHvvccHXOuru/O+JK/gfhH6Jk7YkETYEHDhB/d8SZwfPqmaQirdrz+1tDvMa290XSYh0jZOSnMER8A7+6ENqzHOnsGAiYsGGvuEkZu+J1VCOQO8wLyR6ASEawcCPR310kFNBOW2D0K7+TROCZBLbzOhdrCeRS8IjoslTFdGlifcNYZaaAXPtxZIRmAPoYqvnu4Ce3yocw4wj4VtMdYFBnM4N9H4PnwW3LfdRnVh1xtGHvoy8uIth64PiL7ruczVlDZbCzH+6Lvw/20Ffl9t/nbl/yu4zvAwypPx0b9O+cgsLpgco4pN4JUA4EmA88Egplw78mvj7b66Nvvunz+w9z+w18b7e+N8vx95D4jYduWzefJ5NHc3nrbK4SICcyRqATNtz736VFrn5619umt1r5j/PDTZ+SvKfcdi2dWf0aw1+nrdHy0i1wwpu3zA32x+DQ3P5Hj0y+5Ar4F+ZkJI8KmA2ys7+3mjQT2nKAGwUj8aD/N2LUusFHe8RaG4Uv+ngjPMnmgDeyVTfG78r33XRjWR9Te2wJ8lLdQtjfOaQEY9zDpqH4DXj7nXZp+fMntDPwre5cR+2GuQm+MWx7obTj3tBG4X73PQOPF91u2e0VBKPCKz2NhfUTGefUj8j56fkTeNgP3/VXewd3QT+PYO4qEpPDXO+37ftABL3D71Q7lqPljhzNOW88p+I9KjPUENXbB2M+L9wIdJf6BCfwSBKD+I5PD/YudPlGiae2xO0ftW203UE+vGzEdxg7WHCwjmKIdXPBHMVBODaoOtkFvNPeb/76ZVTxs+e3uhvaxTfz15Q0tnjF4joSQHJblp2ZshBOYp1AgvH5kFHz214fFJwMIcHBWgRxYMHNYgmEwD/MIgOOYByjWmxEuzfi0O51SroO5PuX57JT1cccDJDXFGdYjbcYFvj+D/B6J+XVs99GoFG7bLuPSGOmxtE25gJg6hAswyJomwHTGEj7DABL6531pAtHxaenDstGN73Pr6JGnwb++OBQJKQWy2XCPz2LCarajTxwl3KF1il6vBHUkQJHegN5VQjHDBMMzCi5bWjt3bZ7rZtUOWx2TXC3p7LOX84dIphaTZkenuZV72ygV3XLjLwtz7QzszcONzLdIWyyyeKrNraE+K50Xi71Hic1tV6n60B9OjqBSlK22J3uNirttzSg77QRS9IAbBqNZOrBsXV2vj0FfEu1surm0x3pDmH0h4FW8dTbHLoxosby6Rq0dtKg09tjqBCiiCOsM9PuptV1vo+o0I9N9TSrt0G7PrH6ZHvqeouAiY4ayXR+qxvJKs2BHZ0aEnV2Fr83SHkQHZKs6vpZ6qewIRavUId3kB0rJ0armZ6KOeaKTeLNTVVo7g77x00RqNrrDx2pXpedtSrm9vhzOIajMWqTyIsmlY2is9Taa8wKmtinFVZhbMYWK0um2Jji7CmJjqteBO8ht2FO8Uc20jdmeo3OVlk25oec8kKZZd6bXqpjJM+oyLSx+4C6hImZbncRBOG0GIHMHrVLo45qXOMxvp+ezlNy4SSa2nsR210zVgpqwplNRjkF1juUrcXb0IitE8Spq2bW3uYkgnFZhszZUJ9bqNV5MG0EFWZft9O0h9x1eb9G0ylNHXzA9x7jTyxEbuNzUi1lXCHo0HVivtBrUl3nOkpxKoizLQxkjEV2vsxd4h+Ub1JT6wIXYb9yMhXlxRFc5242YJzGagj4aikrC1brf0QvGtsvzUW8X/UGVd+p+N+fsHcjovWbuJtd9uptrPsqnXkFtmHJZg+NF7bzjAtfkoyH5KO3Y0Qr3NMK+GgNgGuGcz7rUijtBQUMV5ulmf9Kw88mAP2fp7Ok5hanT1WEi6CW6YNHFGhVi3JRNTmQnhbblBTSfHC+TfBqhaB7THAmqFTUl6thmd7NTdKRNTxJTWvfCAb8aIlO3tiPttX5zawpPmOe7bns6y3gt0Yw8t5QjHWgYdT7XUbLUvUZfJkW8wJp1UNnp4NnW3LmQgdK0lyJOJOZar8kdPxO2KyWZXqauiFWbartND7qGz0qOzOoYO2akpjXAPzDSPsDPlM2cDnzNE0o4NHvfPPdzajusZNUSImBrfQaBWuBZklg63jSVYHWg8iSbBcszQ7PRdkK4zPzSl1YdsQfDpNTVvKIuEUVsebok5LkQlzsBlqat1qnMlJlPdgusRlvFvsYoXp7ruls61xuJl6i96kTZ0srMIFi2KiOZ3nv1YnvKCGZGT9CtZsEynlF1umuMWVspxA671Yo7Ya8bNdeutWLs4i72pEAHIYdraJ0rqQOztppte16rL9gmZK/ncrfy5YKZbHkUbNtliW2U3axW0M0Mx9tsk/i+ym/3JFFUArqq9KVfVTeOMCiFIYUpb7pW0JgnnNzAmqh6Zq15u8OBp5SjkqTUvJXUWTFLpoeGKRLc1oxqZXbTZQR3IrddvXDXtHKNO9BXiSV1sU7IrG2dWQW4m6nMkueCP8VyYmFS6sk8uG6rCbY8nvDbzeowE5w7XTZqirYA6l7NiVqjhrKku60igHQtgTYh6Y2693XVtUGly7i6XS5N6zoYcdzsukDnhO2auRIRFgcC6udk0fdzlQ7t1Uy6pvSN3Wc1bx6SsxjNshUrJYDRmaXHiUdZmOND2QaR6lPSIdzXssWfWjdYrLYCWMUXM295Yu4UHRkM3Px4WdSteCxUJUnqVj0fmA116vrF9ugdK7BgFMusD5TELendAnQHwHpmMI2URjL7pvWdrU1QqMVqs6Rsk1O9O/REOvi90MyOujLfmoOWyDoB0FiNlQr1irOVtxxphkbiLW+NMMGT6XnRoY3lxQybbDwmia+wrItEJnKSkiRZGM6+ijLFJF2ey7RBUafM0ukcD0KyjPeCpN1EIirFxKiwKd7Mb1eyX8bbcpdKeeAueVIvwpwTryZ+MjH+dM5ujQ9WMz5bGbjt1cbWI+vkQBkJNduQpZ+R+8rGzaHYbWxMtm8SZhuEhU99jZxEeHdEqfV6s6BT46R25y7E2akNvH7RJKk+s1zxSGLm7mJq82pidKwYl10n1Nrc2JcUOXN5Y4ctzwHnLWjDEmdEvpVuLb5PLrN4E13TuXSJt7eb4VSLVcX2c2x3bfTGXASoUhKb80ap6tRZMf4U77bdhrtupUzhdXPYFDrKCtxpTvPX5twbUR1Fjt56NboMYJcHQwFDf01W+a2jowuT1mv2kLbWzCVlw0RzZydf53ZHrGNguKkmnHc9h84C7jCrNlknSzrA5ktuTYeaT7m1Pr2ermRaKfm11Wg13p4srjrOtAOfq2awK9bbk1ivqxkgUcAnKdr5IibU3vncL+aJc1ngm5TkxdCSlQXlbFqMBEWoB9etTYXXC6obniVVG+DOU3eyGpRjJW1rCmNF4nJzYYPe6NNYnjJb18xCiaKxOFSazCFFtZuegdoZmVXV2u7iUN5cOh87wgi4Kah2rseeTlovVaFz9JmuNmfCBZewQuJ2ytxi4RcNW8XEfiur+lHMySCkvKl1UI754twakejFnmFvosk+CoQ1pq+1IikPZ2k6v1rtriHOaqNe52W1I6+HmgnP+/nqMth6L9sOMCYtr/MA4+opP1mGvlP0OmmTW2GDukx7Xi1CN6MneX5cx522gg29XTE62pG+RU2YJexmpmkxXL4VshyOmu5mxpY1odrM5ESYJNpn2mA4p+yWOnvDZDSNIuYXnDlye1m4rDNfMqXD5aitHI4zi33JMcyyXouHedsurYWz3nunFldDFPVvUS5V08a+cMeVpC/N/fraZysVw0E/nZvHsMPEJHVzNTGJAF+s1huWxqeiXntDaYi2KB07bB7sfO68mm+MuX/yBz2QxGlCmsKJ8iJli568Y34Slmnb7LYiWgVZcdnmixXfRvoigR3xjKu2TOVGtEoM/KYKmy2lHaZL3FgL5IJyTSIhGyKJd+6caI8rmmW39QUSnLfHfsrvN0YXZjlQSYAth2NYcIfqFNW5UPqrgpp6iZUsSOtQnHJB827HQbN4UaAkIlsvLsnMSrXZ4awUXKkQ211yjTTDkFLxCta3LcGXq7ZnCyKc+JfTXq80cY1t+sP8MPMYy1vZUuHb3TyP2di5zrXZsLdPlTXrky2rHFcFeqtt6VDrxGXl0Ft1ajh9dwZwFkb7wkgM77zaldOcTHfDxUyPGHokF/OlwJKDOC8KWhzSQ3eYGfg+Sq9dzi2OwrFRgmnSqxsu68b5LsvZUwVLncvhVoFAyQGIerg69iUrWgvtrGw2fKlRLHmaHcipwmz4tjLiy1rdeJkG8YnUJ9V2Sm1PUbQLySTlJaMjyEDyBP4aC75gZreiWCpDuqeGtNCMlRVMMrvEIwrWel6uKqtscHw45iHjYfLMOqvpQWHdna0M1t6l9M3lKkKnKtEMyzkIZefKCDJN8BrOOFaF1+xPm/jG72kxWFJmHzj0MRIvhyKOVnSz8ySbV+dLY9GHTVBvU3LwDhFbLXqvK7Bmk66XW543jDDHvRXHzGWZEK9lLIZF1rVBoKCOurT4gLsdsGk8lMutUQVBGR2nPGfCEp2e9Vsg3Na6V1vFmglz1c3wbat69ZKab6TTljhxKcdl2STNhnxTVz3LYYu0WA6Ku3dkb6AsdLcQp3oE0VnWTH0hCceZeNjpKwtTj4Z/3nNDn27T2j8sYppYyFZCUSRaFJai8QFZ1GS5wCamUmtLZcOvjSVf0HjMOqkRTzoMCJcJQGUlw+sprZHrJSnP015JfCK5EKCBfXFCrGf+MiH6W78XYFXUF+Hg8aGxmILpwfRKTBT309lSacgsvHWBmCg7R3eOHoarRt1kzRK36w1dYktS4U19tt+fgron/VkHB8pN4uSWF8i3FqUM6iyvvM2BSwjRYDjC6XZHXkh3VeWuliWL2dvN1fcEj7/ml3kmH7RaOl2mVjdJDACOS8f28z2N99JtRtTULS9I5tBPWgybXDg60kjqhPkTMvTz4krbRLf3fW15KnKcbFsYdGMQLDgrk1F/BazKQHZyHegRgYYLMoqPJpn7LR8uwd7rxM2NXrLzhSIPzlXxlkUMZmZeEr3A7ivPmA8mL2Z4dayIQ1gwxKrV+eF842GkZ6e837uulc3Dm8ic9mJfOEPPtSYq7452CYhC6zZyS0u7K7E2tWW+A4ZHzBk5dwyLiWVfohJbvWpH0ZavwBgy2fHmKinhejTjxWrXxhi6WxeOoFcHuvXWxYQi2Hwd3Xhlu5m4J5uzE3WOMhOVpARQH2iAlpGxM/pWP4ib7sIdoHH0AWsdf2DSRemkzCWwXYIq8tjr6B2J07OF5K1mh2VO98dILyr5ejhXq26jr2peoQ56taVXbg8EkoFZHDTQSeerTEAv7MCqPGGeLO82Sw8o5DXc5ER4NmlVxCKTpblkr/pJnkvyKnOPEEdm/KI1K7Bi6Us5pyfT5ZVk5GXoLK2bQAWH7bYMnZqJZ/0mKCJ5ZS8s4XjAJe5kOsyOc7ugvhEXtDhLOB/sT31P3g7nshSYTTvBGBp3BLdMuw3OGuUBDELmJc7O8pgSp73FHF3karcG6C1e9NTVEuq6ttdM3hJ9fs2J4Bjm+UyoLhcHzS9SXR7X6ZKjSbqZJ66xMnICjmhAoK72gtBvx5ozlkfSazfY0OFzo0OZGyHmWUYdWopdn5IDWyl6XjANq+CMEdPhTF0tlcWkAnMHy+lB5ecYx9xycujisIysAcQtqYobUIFk05un4ejFvnsJJwHeYo50DFGXv02oS7Zj03jie4CdMTtjyZw4mb3dLpS0vEUwkRilT4SIbP0JK1hUepY6qjQTv7/OBpci5G4vWNDeqUFQJ2tpJ+xA7K+ZX+qDtNgWAT1EsArjC6bl+mnvM15SScCzgqtex5mSN6mzRnfy5brnGC7ZTjSMcffy8lJEfH2+MLcAJ5a3nYOeDqDWTKfazlarmDXUeTgke3e6l4/LAA0uIAgu6oWQSNUC19gO7PToXA7kUtZxgcamBJCP8aBV3DpYFH0XMoJQLWRnYA6p4maYBOYdSzLB3DZXdbhxd465mvlhOk8NP8mmgsTtSbc8J6Kc2ngwreRzXsR2nFTDbQp3SBqLu3AGZk6+QARRp976EizQ6e5sziLTqDs5Na3SISp2XraTU+qxl30yHK6aNsdtA9OFdT3ErMatT5Mim2jeftKa5fyGdgZnkvPOpU8Ny50zpayzzfZkUnp7aObutjIbkk2cmCZtF+5PefdW7BjvBhg2XGNdXsgo0bDp6iYGHPfy8WU8t36ePv/rb5jH48D/s1PJxwHi23uo+8EzsL3Pd1mf/4JOP398qd0IavQ4e23SLngeVP6Pk9dP//T1xbh8eLy2HV+YXdu3c/rWDsY/O3qJcq9r2nr42hRpdz/8/fjidM34JxDN1+ch98vdrKwcT8zfJT5uNiVw269t8bXqina8F+XjWyDgRfb7ZfA8jP744g0wQJHbfCWo2VdQl6Olzxci4xHu+Ebk5bf/BuAWW4PgJQAA -->
