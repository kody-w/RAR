---
name: "rar-cowork-cookbook-scheduled-brief-perform-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions", "rar_sha256": "9b56a91589535a69492388e28d3b366e4168e90e7a3f512e93cfa61529151143", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_perform_corrective_and_preventative_actions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-perform-corrective-and-preventative-actions:234111455dbc646c550dd2b91fe87c809d0dedd0d568f526da996fa0c78ca577", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Perform corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 9b56a91589535a69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions',
    "version": '2.0.0',
    "display_name": 'Perform corrective and preventative actions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4386c40b04d7c5e9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPerformCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformCorrectiveAndPreventativeActions'
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
    print(ScheduledBriefPerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZPiVrbnv6LJ98H2o6rQjpQdHTEghBYEEmhB4OpIa7la0L4C8vP/PldAZpWfu9+Mo/1hqKhMJN179vM75+jmry9O10ZF/fL6ogMnRwQnTeMI1IiT+whXXIo6gb+KxIX/Ea/I2zp2u7aom5dPLz5ovDou27jIx+1eBPwuddwUIFlR53EefnbrGAQIyJw4RZouy5w6HuB9pAR1UNQZJFjXwGvjHtz5lTXoQd46jxveSLhB4EKkjQBSg6aE1/FIv7jkoP4bAgWIwxz4SFsgdZcjPuRzQ+D6CwBJevsCZQRXJytT0Ly8/vyPTy8x/P7y+uuLlzpN801m4C9GQbWHVNyHUPPc174Taf6QCFJNnTyE28sbNF0Or5/6wFs+1Pd59WMD0uAT8p//mVycOmx+ev2aI8/P15fx3x6KPGrWFk7TQi08p3TcOI3b2xdknl6cWwOVbrsaGsFBGmj5PPzy2PmNUlEifx+f/fhg8iUE7Y9fXwoogjMK+/Xlp9EeX1+geeD3LyOV8sefvqTFBdQ//vSNTtO5Z6j0SAxK/eXtef0kCxd+WxoHd65/h1QfEeCCry/fKTd+HnKPesKdL1/ORZz/+CBc1gU0qJN74Mef/hVZ6BUvSeOm/X+i+/ODcAQcH+r0FPynT3cj/wOZPBX6oPmv2ZbQrX9GE7j8nd0n5Gmof0X7bv//RjqNc9B8WPyfkvtnGyZ/R37+l7r9Txs+IcHXlyVIYSjXY5q+Ir++6RrP/fyD/+3mD//4DZL+v5LRi6727hTeMiePA9C0b28//9Dcb//wj59/6EoYa8DJ3ro6/Wc0/5ld73x+Z8Hnqh9/vxfyN/MkhyiAfEQ68mtR/q/6ty+I5aSx/+1+84p8ny/jZ4KMSrwzfZjgu5xpoKzf2fGnl98gcORQm+6Z/68v//EfyCb26qIpghbRvaJrR/xp4wyMwhtR3CDGM6l/0deSonzJ/F8QeHdMdwgRTpe2iFCPsAjzYfT4qEERIL/8b++OuZ+9J+ZOm3eIeruD6dsTXN6+QecbhM6376Hz7Qmdv3xBjAhKVNRxGOdOiuznmoY4IVw3ynKPGojKn/tRHChq/ICjPSeNUNRApn9Dfvk3+L/dWX0pb6PqX3PoSye+ozXIyqKGtQCCtTNim3trwWeI1BB/6iJNXcdLkPFHV34Z7XmIQP60sgdLFLgCr2sBkhYe1CmIIbp/GqtDkcKq0Y62b5I4TRE/HgUs6tu9tkD/vI7EfvnlF9dpoq/5A7wJ5FHDmilc8CEw8vkzVChI4zBqv+bAiwrkh19/+wH5L+R/2nUnPvLQYHV51iwooayrWwRmc5fBZQ0yhhKEqru3f/3t4aNROljREJiDcRCD+2ZI7VvojBo8HPfuNajzKCKon5x+bzfkEkG7IHELrQVxofn0NR9JFHBpfYkb8G7Ex+aH6d/D4MFn9EnztCH0U1AX2X3tPWpHZ8IA8L8gUoB8WAqqC/3ajh6NiqaFgV6C3Ae5d4M7nfabC/OiRRoYKk1w+4R0DVR1pPyLC0mPxoHBBZf/gmw4DdbGIn0v7+MiuLvI49Hxzzh+3IZE6h9gjC3eSXxBtjAga6R0aqeMaqcB93WB84gIWBPf90PiDpKDCzI2ByB7BHGR3yNP+xN9ykcvgfD3fufeUiBfOxzFSOT/w+Zo1G8uCHtemBv8EuG3xv74CMaxzRtt8+gMYTvyZDNixkeL8o5m7zj/NU9j6MD69rfHyuAef481D+zsaijMfr6/0x+RoL7TjVsYRWNY1PUY+c7X/L2gfIKOgT5sRmyEyZ48dHlnOD59lzSCGT1ef2sukEeAjpaDoY+UnZvGHhIA4N+zpI3qMQef3oEhBcZ8hEnjRb/TCoHUYbhA+ggUIoaxDa17N90W5tLorXtifCyPx5YNSuF3HpQWJhv4ghzG2IceaBAXwL5rXAOt8MOdFJIBaGMo4oeFm8gpH8KMrfdTQGf0RZE5LfjeA8+HMI7HygX5fSQppOr4TgtteYFOgDl4fXj2Q86nr6Cw2Zgw902/d/dTV+T7yve3MVGhjN9KCJwW7jH9zTgQ3eusuUcsLOdJA6EgAx9x+ugPvjxK/KOH+JDl9Q/zxo9/biS5F23z9557RaK2LZvX6fRRWN/r6hevyKYwRuISNN9q7CMnPz8z8PO3DPwMeX/+PgM/PzPwdywfFnxF/pzYvyPxjPdXBPuCfkHHR0rsgTGgnx9oJe7z4viZHJ9+zffgm/ufMTKiI8x09/ZRpN6XwEoV1iAcFz+KVjPWugssr3esvBedjxB5JhCE4jwcK2xTfJfYo06jwx/+/MB0+Cgfq4U/dpMhGAewdBS/AS+veZemn15yJwP/xuA1wjkMbmikcYyDiQZd1cbgfvXRwI0Xv59N7ykIscMvXsdMhKUTNtufkI+++RPyPsncZ8a8g6Pcz2PPPrKES+Gvj7Ufg68LXuBI2d7KUaHHeDa2is8W/o9CjAkIJfbA2BwUHxk9cvwDEfglDEH9RyLq/YuTPmGlaZ2x4MI6/wSD91D+hNzNN+I9hNMObvgjG8inBlUHS7w/qvvNft/UKh66/HY3Q/uYcX99eYeX8fuj33iE00j7L2gXR2u/l/m3cbdzpzw2dXfj39vnN6h4PJbz7x6FY2/y9gjcl1cIW+DTy2jiOoYzwXB/CfDyEBRq+K3xhhQgAH1uxvZkCvMOUoJNQzlql0Dw/I7BeDv27+vHL6//ulv/80jyihMkhmEkRfmuR5O0R1Go7+MuiwWAmXkMyvqoD3z4g6KZgMJp32FZOnBQb8Z4DjWbQflG9pnzlG+KjX6Dmn04568cLl4epGG5wika0mZdinZYjGJYiqAcmiVZnGAYgDM+4RI0DUiMZgCLgplDBBSGA5bwAofGKBzugVoTI71nD/uQ9+19Xnj35ANroGxZFo/a4I7jMd4MI3125tAeIFCX8ACGY/6MACjFEgHkT8L9H1uf3hyd/TDJmAJQOdg89iOfX5/RMYY1TcKVItlI88eHm7KW4x6n7jUSJ3U6uZ6MWaGUfCETom5VtJJzbI6hy0YQALGz53ucO1DJ+SR6h6QDhyD1+MVkL1JRkGRBZuGTWFa0xt9wZyDyfO7jfn4C+TWpOEnZc5jZGW6yj/VUSS2D1sPsVNJSgZ3s9XqSAFLJ5dqOT/XKck63wjpdu3IzFQpMKMqgJ6gUP62uZaILmJapKbs9YpRlCHk9mM5hEnvMirFm+TziTAe31rLZMivUCAjVr6brhS7bVnW93SzeMX2d0nNlYxUKe6DPihtV2v522uQU7mtGSvuBTqh5zdDTgTRrZl5t7GzlkXpTzczSd20swsOaT3PpIATocjstCKW6WE6enEqj7GQjZQv+bAu1RJrp3OR8yzbXOkNth1PMYLKg411Yr9BLtdFv5yV3zp3b6tKnDprtiqK2rNozs13W2QbhSPQZM121dff1JKXNRV/tgak4oUrpaFtIw6QhUTI9rktb2NQZb6jcrkmtW4JufZ0QWKxJaWoguXzTtMz+uNutwKGdV5ZmAFLEb6iywTOJOW110h7QoVrkQmtV6YJpqaNF+/j6INhZlkWXqcEPfNSsCMc5W/UKV3ZNHutJfzD28uTsuQcnm2BZmpbOnNH4ic9zOwzfpKaVy+jSIfLKrs/KNl9TJLqUwKrpDE2p85xduqKbHTuPZgTpdNrU6Fl2NWKjEkLKW+vaO4iuZqgAOm7Y7mtLdUzMl8PS4SdSGuCXVXZsjQvmsVtwvF3zaUyvD3pnx5w0GOj1ehNlwbiYjb/T8Uy7BGrQzRwnJixrZR8n2e3AbAJxdmn2zamfS7YezhoU57sudiewd/NrHr/6ohFU123gDJhBGOuM7Al+VkNaPW6LF4cI+/4ITDfXzzc7YEThXPlaX05ANFEKQrMEH59F+ql2+QOzMo6lb4mngwnd7h8qi2vicxvh2/iGeyLfkNj8NqwjbLlgiptVZ2vczJtV2AddQp8EP9+X4XRA0VSR3RuXgBzlcSrMk+Vpk+5Xy8NeQO24cMMTqpuc2fvCIt/sU0UqynhQl0tPlTOSTa/dCgtW9pAZxjVz/FyHXCZGuxItPI4XAFN8g1JRlK1vbFTk7Ik2zlSeVe5JlF1f96ZuYwSb9qhaGrmbMppJkOfK3garfs2KyvlkM5l1BbSyOcnbpRU4+/aUbI8JkRfR1V71iY+3kXjSQpuohDPVxUXCLG+sdM79Tbv0I1NOSmtfzNI83dKmkwnKEAQWsbgGKE1HuxQ7VprWTy+xmZlXOz9f+ZbrLxLZ4dveiPsJnZb7bYHCHAol/bp2VcbZReutXR8SdZp4VU/LtII169Uur7c8u6tARDH7A8nGtG3Fxw67yNuJvKJRSg/N6dTB1kmBXaqB3k4khbGOB9kxYE+/mUgRe+k5hdaUzRZwPOPjZY3r5ipfcv6umsqydV5SBZXbatOUB91P8/IUGWSsnsKol9oddaHaS7McLPzQyi3uFCSL0pGO8bR9Dtwiq+Yn4EvcTTlv4p7b5uzgYZMibayKLYgJK1HzgOrTzpuikqza0U1BWRZvWsOQ93vTXagFilKqslA1ba+LMzngsnAe3bjl+dpWpchji6Yd+pRXSnVhlHQQo4HHRcS80vlhnfduQzvdrrG6pXiNzgaPAxcEF1OfMyE+X2RxQXDrW5CI0LobuTmpps5xlKyEt6kbDXZ7juPr/qgKhr1bRFx1sg9tY0nLNVXG+pAbuKmSgyCVN8bC8sxdR+XOy+qeq7sx0f0Q5mtjkL3ZTtcnl3Do44Q95XJK7mHJDAINZdWBug3bmDtGea0eGdZcebHppQQFgUg7kqI2J7peb4odO235iG4HYjmrjiZTLmf5dJreJsakD85gGhjabR9UNUvtp2snHPwDw6DESimEzeKM6TSvOtdhPcTRGpYkCjMzX4o1jVXkq4xpZ4HUZWm7D7TQUa9NldSbrOSTPjiudtHJOOzba0nGR5Qpj7N+vePNeF3g5WwbWiuLUcvycNp2Vojqasr024Nehu3+VgE/ayaENwUyNrddgb0167iUO42tl1pXrcv2YojWyi3wy7w91Sc0XqLnWTeT5GUt7toZYR7Mo9Ptk3yjiKezkmaxsTKFWo2FNbqbOkntH/OmbjOHmsjZbBkP1WG55ASz2u/wplud9QWY4FSH8cRmxSW03jdEcD1ISwVXMjsZ1rdOPLWZW5k3upLDYkJeL3AzGkVsupxZSTK31EXAWLHdlkXmrQi7Vm6d5WZpsNwusKxau6thOS84RgWmWU2cjlCVfgsOkaGl+tlal+vjbH5bkcvt/MAsRVhkinIDg+TG9pedOj9azXZ+OmqaUiU0xrsbwWbwuXwSt2GR9lqOD4GC4sIejXhAkhdxGzs8X/RZB6uDGZ2v+lXZropkp5HqdcMYHDfNDaeSbFfG22BqpZMNQVGldLYVPVlOa+eq7iXZaGltz/FD3sv+0HRMAcqFSPNYdEsKpki8nBX0hIj1qtrshh1Fb9M+u+4Ox8ka7VBjM8iCo0BJp8YhLEmRN50jd1ufq2Gdnuc7aXNIlJ0mijrBSqf1br1dDOhyOotxggXbGLs56t6jZmtJDhbUChe1Q+zlZtna+93prAfSrp2y5ES3ckK+aEldm4Xoh4ELJMIkryg10yYpBgvy4TCb0Fs1xcEZO6/RExy2lBo2RasFtRcTCl0wZ6K/xgLHnFN+rmgLUZLyRXosr6TWStbaOC7atbOM13ZNkipt4S40pbyWYHwdzguytKLS7IgTGSlrYatHFmqf0ErY0ts4WugaYFcUyg9LNzUFD/XWkV/Z8jGQLuziaC+D1h30nSTznLOt6bTaTajzLFoknahnnqjpp8raZp4kHfHFTtpHxUbaX/XhNDUFRk9iHHcsebm5ZWgIbmQ5lSxjKatGvA30TVsIWQUEoyIlPN2rpiGLw56bEIXuyYlAYpLB6uZm7qS73N7R+Y0SD0YRtUMcw8ooX1cb/nAV0mF/iyYLEE4Lr1UPJ3uSV9Llwl3drm4ujWWnK1uNo4TKjFi9pZY3I/JANtRsavJEvps4S5+bUbf6grlzB/P06ao/dI3NH3alfyNBptQTHpiSW4AT1ot5UCvXJCBlkamlvjsIOHea7JJjkvsn3qOGHA61hLm/qLq2o7qdWtlxmNZrHRZ5xd2lHGyf1cWE1CuNGIy6Uc2KyKYevXMTbu0HRt6IhpWwF3+Podel1UoVC1I4kRe8Aio/mMtNDnTpYC6drQyRfuC7QVpd0Ymyt2CN49f7vSQxhpOriguYy6FLlkdsaUfdOiEGzbIVYxKWtLEfhJtSx/qpVwtIc21tMt3Fyw0pu4F2HICT8KWdBHmGNUxyFbs4aopWmvHM1XPccLPYqVZNRTl3PoR5Ma+w4VJfsg0jXXva0wrHm/v+xZb6c9mHudsNcqqbBX86Ag6H7dOuB4eZ6fYGZtTYYo9jZT/nt91loaHkJiLXIM6sfF+txP116y3mOC3RenMqLvx2aHtYsVelktpA5kxc4GZHYbk4nFR+k63aa58d9zfBl65ULlvUqeuubFAUDgSoYr5MlkQtXvNw1tde7i0tLilMRvcYPFlfrrNqHrccRm9uS9iTFoaF69w5o7YSU1BKQ2fe7KxKZbpgz7nrkIy+1+zpfkeSyfJs+j4WHNLtPOaiOqtnpYordbU2iCwT9vONnmlSM5ssI7e1K61dgf66MAtWdOm+3A6N1V+Too191S89sZlNJ6gmxz7BXwklGYhF28zW6JYl+M7aRaAbtoPjg5LaygymzGcLecty51A4Vu1NooGrVJlmB9ODmGDgEie2WOqOaudMpM6v03aSwf4ETj3orGvqegg6KwqP8NFyobtNzdt9TKySG3tOMeugQ1/4h3S3EYn9bNfsp2RpwAluMJmtcOopnIBdrS2dydlSBD7R10Fdb7zzeXKaToGVT+cmc5stjUnFTmNlwpqaf2CvZ5aJKj/t8JXGi4E+2Qvb1VYMHX9VX7WiV7lMJrhWsFkOo3h+jl2nsqs6aHjY+J1+jG7z6bxpz5uM2YmSnwywfQcCcO268pkBNaRBtE+AOuxJVVSHtKkPu3U4K2fAS2eXXJjIjehxYTYsNVoocmJ50Mo42YZ2ixJEopGsINOzpVxuc9W0W2LBELnrrphYc1g6c/SbtVMkDQ34AK3J2WVtRsJtyHYw0XFPFYva3vedWwQyYdM5W4sE2JqLI3o0Jtyp4dbsRkxaRryaIlD7ystuKT6zzl2o8JJac506bN0D0VRK4Jh01xz5vJ0U/hUTO7sJfKbIVe4YLgYW6ybBYpdfYqV0FvwSkPy+k+3Wp1dFvz/MnKmjlJvNMppf4BTi6lHHiRjV53Xs6RwpMd7AnM+3ulkehXW6DbbVbCPMOGUKPLml8DwgeOAsQuW4sSOeZCrSm2Ja0AXB6SRIbjdnD4vDclPM8mBnLyjek7iTcpyTc9ADIVtGO8ldoSvrOM2p+da32ni1YaamdUnaJRPm7Jrc1kHeod2VVzx5NdN0fcqLwuFy0HS/yVG5lYB8C42uPTbnqdKdri49O+cnzKvVwWUvolLur+eKFBYaac1ZR4UjmCP0HDGn+sU1sy54j21C4PkMe4qJw2VxCQ9LF+bmEZqN1mynu8lE1eVZULcOtTTMjJCval0fvWCPM0fO3V6SQoUI7LbL2QTMBGbOra/ThVhM1XPa5FcGhH7orvuqCtBpY5wdIuCWwWVRtzi732grdua2024REdms7hmd9rDp0FzMKzOfEoE4rU1tPbdD5XqDlKKOmEhFlCuskbhZxN0EFicWQzN3/WVHHKHV/d5kpKjH2WjbUkqPbvabxPVMk15sJ1zZOJVbamlQ7ge06vEN6knY9lI0R61dT4VVmOUTl1T7+Hqd9ivTQF0G56nt/MJy+ixN+xo7rCkKuAvJtdjlrjVmqjoXixMO5vPtPvTkS3P1eNztjodQLMuSxsmlUrYzvKCACtgzepzxzlw+CmiA7yYDnIfFlppoYdjNjlkvwQYb6PN2M7cujbpqmzksCbfwlk3MDBW38w3pUXyyhu0kLlAmoLT9AROVi5L7YS7YF9/wlNlengYot6aUNZmQ2iz2IyaTW6+TSHuCw6HK9YTMZjWLmoWOHHoM03lN0tcNUISVyFRz5zyBBd73m2kbyIth0tnzI8mp6ipCJ4W0k1DizJt1w2qbApeargo2BZO455yUvMCPeGqIGljR2GnFK52q7YPL0tk0YHWJi/l8/ve/v3x6uZ9Rv7xiKEvSn17Gg4nn8cJf9BY6HOLy7cmEmNHEp5e/7nXn49Xj+3Hl/bgBOP7rnfvrXyL/Pz691F4MZX280m7SLny+/Pxvr4E//xtvrUfCt8eZ/XgWe23fD3paJ7y/b49zv2va+vbWFGl3f9sO/dY141/6NG/P45CXuymysn2+wv5O9Zfxb29GrgUk0RZvz79Uut8eTxqBHzsteF6Gz/OLTy/+DUZC7DVvBE29gbocjfE8WhvfHI9nay+//R/GHSaA/CgAAA== -->
