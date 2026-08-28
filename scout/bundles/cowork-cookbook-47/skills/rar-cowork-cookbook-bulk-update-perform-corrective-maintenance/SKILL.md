---
name: "rar-cowork-cookbook-bulk-update-perform-corrective-maintenance"
description: "Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_corrective_maintenance", "rar_sha256": "323b0e3cbac651f70cc62648c5a330a5909bc6df52892e922a665e7872497087", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_perform_corrective_maintenance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_perform_corrective_maintenance_agent.py` and in the RCI capsule.

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

Perform corrective maintenance Bulk Field Update — Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 323b0e3cbac651f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_corrective_maintenance_agent.py` first:

```bash
python3 bulk_update_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_perform_corrective_maintenance_agent.py   # or on stdin
python3 bulk_update_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Bulk Field Update — Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_perform_corrective_maintenance',
    "version": '2.0.1',
    "display_name": 'Perform corrective maintenance Bulk Field Update',
    "description": 'Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7bae3d7026cc0a1c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePerformCorrectiveMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePerformCorrectiveMaintenance'
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
    print(BulkUpdatePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOjVpbvV2Fy/rA9ZKUQq6iOjniAJIQ2JEAIcDnK7PsidvDzd38XSZlVHnf3dM9MxFMtKeDes5/fOeeSv72YTR3k5cvnF9k1M4g3kyQM3BIyMwfi8i4vY/Ajjy3wD7LzrC5Dq6nzsnp5fXHcyi7Dog7zDGxniiIJ3QoyIatJYsgL3cSBmsIxaxcy7TKvKqhwSy8vU0CnLF27DlsXSs0wq93MzGwXAvfy0qkgr8xTwB8Ks6KpoSSs6leoC+sAcsrhU9lkUFG6beh2kOUCci4gl6Zh/QYkcnszLRK3evn88y+vLyH4/vL5txc7MStw64UFcl3uAp0egnAfchy+iQHIJGbmg/XFACyTgeun3OCW43rvWvxYuYn3Cv3Hf8SdWfrVT5+/ZNDz8+Vl+iMBSevAhercrGrXgWyzMK0wCevhDWKSzhwqoHHdlNlkswoYNvPfHju/UcoL6K/Tsx8fTN58t/7xy0sORDAns395+QnKS8APWAV8f5uoFD/+9JbknVv++NM3OlVjRUDTiRiQ+u3r8/pJFiz8tjT07lz/Cqg+HGy5X16+U276POSe9AQ7X96iPMx+fBAuyrx92PHHn/4eWTtw7Xhy6z9F9+cH4cA1HaDTU/CfXu9G/gWCnwp90Pz7bAvg1n9FE7D8nd0r9DTU36N9t/9/Ip2EGUiHd4v/TXJ/awP8V+jnv6vbP9rwCnlfXpZuAsK5NK3E/Qz99lU+rbiff3C+3fzhl98B6f+SjJw3pX2n8DU1s9Bzq/rr159/qO63f/jl5x+aAsSaa6ZfmzL5WzT/ll3vfP5gweeqH/+4F/C/ZHGWdxn0EenQb3nxb+Xvb5BqJqHz7X71Gfo+X6YPDE1KvDN9mOC7nKmArN/Z8aeX3wFSZECbxr4/Bln+7/8OHcIJsnKvhmQ7BygEHFyHqTsJrwRhBYG/U24DIHLLKgSGfa4D8T95eJI496Bf/499h9BP9hNCZxM2fn2g4tcnkHz9Bodfv4PDX98gBXDIy9APMzOBJOZ0+pKZvpvVE3eAgZVbtgBXrKF2PwFCn6YvADShX/95Jl/v9N6K4dc74IcPxJI4YUKrqknct0nja+BmT/1sgMtu79oNYJXkNpDLCwHgvgJLVHkCAL2erFPFYZJATjhxzMvhThtY8PNE7Ndff7XMKviSPeAVgx5FpJqBBR/iQJ8+AQW9JPSD+kvm2kEO/fDb7z9A/xf6R7vuxCceJwD4T/8ACbeyeIRAvjUpWAZcB5wNwOTun99+f5oZkMlA1QPeDL2pik2bQbzGrvNuc3nDfEIJ8r3ogOKSlzXAbAiUHkjwoA95AdPp0YTqQV7VkOMWbua4mT0AqiZQ58OSWV5DFQjKyhteoaZy71x/tUrzLiLwGVj+K3TgTqCG5An4bxLzvghszrMQmP8jIh73AZHyhwpi30m8QccpQqHCLM0iKM0nD898+AXUjvftgLgJZW73JZvKpjuZ6p4uD/OARcAy9tOlnyaf38sucGz1zvu+xpwqnXKveOWXrHqmglk+qjsQZYD8JnSm2PvLM6SqIG9AqzDZD0g6UXp6wXl65R6Dp3/cO0y1HVrfe45HiYe+NCgyx6H/723JJDzD89KKZ5TVElodFUl/GHVqpybjPzow0BdAYN8jgb71Cu9I8w64X7IkBBFSDn95rLy74rnmAWJNCSwnMdKdPtADGHWiew/TKezK8m6PL9k7sr8C49xhDHgK5DSI+SnU3hlOT98lDUDiTtffqvzTOlOGg1CEisZKQJh4rutYph0Dqcop1Z6+ADHrTmnXBaEd/EErCFAHoQHoQ0CIECQPQP+76Y45UBNk2d36H8vDqXcCUjiNDaQF/ar7Bl1BtkwRUwEHgAZoWgOs8MOdFJS6wMZAxA8LV4FZPISZWtyngObkizydYuM7DzwffovvuyyT+ICqCSIJ2LKbkNdx+4dnP+R8+goIO0XUw0t/dPdTV+j7EvSXL9ldxg+wB4meTNX7O+NAIMHS6o6sE05VAGtS9xlAIBLuhfrtUWsfxfxDls9/6ut//Nda/3v1vPzRc5+hoK6L6vNs9qh47wXvDWTBDMRIWLjVvfh9euTep2fSffqWdJ++S7o/cHgY7DP0r0n5BxLP8P4Mzd+QN2R6tA9td4rf5wcYhfvE6p/w6emXTHK/efsZEhPaJgOoth+l530JqD9+6frT4kcpqqYK1oGiecde4I8v2UdEPPMFQHvmT3Wzyr/L43sNBv59uO+jRIBHWQ14O1MX57vTpJNM4lfuy+esSZLXl8xM3X9lwpnqAQheYJVpQAKJBNxRh+796qNTmi7+OOPdUwxgg5N/njLtFZq62lfoo0F9hd5Hhvs0ljVgZvp5ao4nlmAp+PGx9mOAtNwXMKzVQzFp8JiDpp7s2Sv/WYgpwYDEtjvV+PwjYyeOfyICvvi+W/6ZiHj/YiZP2Khqc6rYYf2e7BWQ0wH9zysEfAiSEOQVgMsGbPgzG8CndG8NKI3OpO43+31TK3/o8vvdDPVjmPzt5R0+nj54No5gOcjTT9VUHGcgXgFDcP2ILPDsf9BSPikB6AONDCCFoZiFuJgNoJok5h6F2DaJkvjCJkwMQ0yCRmjLJh2PQBc06tIoapIk4VILCsVpCllQgN4jUr8+ah0g6SKei9Fz1HYwEiUInJ5TqEk7Jk6ZpoMsFhRCeQ6oDt+2xgA3nyo/VJzs+dHdTqZ5av7bi0XiYOUGrwTm8eFmtGpa15klBXu4TOC+x8gz5uaJ7NLmeRl7ZBmI+5hT2JggJXe1o7ZbW1ZrZbuv92i9Mtg2j2C/pWSYNFD3Wq45r8A1NseP+uBgBuokpMfLueDXq9JQTQLVwSPEWhcWcdXDeq7eioNRrmSFLBE5GtVdjK0c5BLKgwrPZhfMVvPLTTWuMruR4LzUdpTd6MTR2uElBbtbwwqEUg0tjyvibSap6k7d1gOe4oir8ltex47qJeVuYlNbuRSfBYrVLKuUiSynN0WF2hqxoEWM6Gd7m/DaMsN12XItPjSUMFyXh+JoZTKxov1kyFFUKMx1tJF244zVOHd3q3aqZEf1zrnKMarM0YBrnFuRr9i1aquxnuDNHvHrLFpVeXdd+EFWOL7FdKVOyWqq4kWTC5f5otCzqx2O7qGkOGokogD0epot75ug7RpFm9kIQyCxMA5tnigb/aZeVlWGc9GOPS8EdDhtD6HWJVakk1irNMJiaVBCiPkMR/Y72FpyBZW6Rxh1yqLlNryiYxx8idXzgjwe0jxt65lwiZfUOi1Oi74JO0/bjKugWmuyFbHlGs2RKuNkornupa0YzzBCwJy9JO7Qak24awLPz/7NXotdtolJxjDHfj+fJ+kQ2wuLRXbybAxH+oCVFh45Y9KfGwxZ6HUWp6VymMe0wtt8V16M1c0er/Ft20uZkfSy5e2aRVttejdVA9ZEdgsih48CU/dJe1TH2X6xq7YzvAnnvl/Nun5lwqkonnthaI4rac7vq4MWwHPKU8/puKtKbg8rYxpZG++Ii7MRXklNwqJKuUIddYXS7mpu2ccS9dOW8tei2rW9rWxRUQs0LQ83VeeO7DwipMrdaUdt5iN7sYhpOD3hakge9nOn1F18lRIuvarZA3os85yyupRzVdJyZDNcHdDEQFQR85EkW+XodXOBBf4EvBRV1HVY9WG+Iglko+zKqr9V2VUldvJwrYLtZktzp6stmoyyd3fMWJ6Z+dKWt42EydvuoFvuOuxWAi9JyjqxXRO3FbYnicze3QaxxYRrWuupXoqrMRyCI9LqaahVKa9VVy1dr0pncxGzJZyloWVsdprqe7TFE43LR9luT/PeDLPW2J5QB0k65bhBjliCbevKq4do2UudPEdzG1PCGw4SKujVdRobab3c7g96C8fGKSX3yA1B1ZswM7x+X+jIbhi7uHTda0bvjqOqJ2hykjC0wm/RIkDt1SCWVkDMZ4u9Kqc8B9P6cpPPqcxAnAvp9iXrkXFc2Fw3F26tggHwiIaC0/vQvg55lTYkbu16Y8efV9RBp2+nrFO9ODsdhWuAUiETL0jZC1X1uDQaIdNQthPP0h6WxEN08/tAXyMzd59ZXqPnHd4T26TuzjU7Dxuh8Od1tuQcIV2GO4q7itllkSPlsiLYYEUetd1RaMrIjwVr2B9gW1CcKIKlWrldUopogmWmBGv6uq3bFa31i5LxOuKshnrSZZVsaY5SGrNzUV9NOpvjdIQJRItmHjaYJyw4b6mkaxtcLgwZL52jllnCqWQPp0iR+m6Zb2+RdlBc3Z7TklBf80MSOAv/bFkdfxLHSlY23VnEJe60wBWaPGjjcRT5C6ZuCUqYjdYRqXFmw2TnwJn7zGZ/XKOnzgpMhecOPZ+EeI9v93F+WppoOK8v9M2ymxkj5wjq87mpFjJmp3IvcjQaCDcbzrU9L7IhfiCMOMypnOZaqsvHKKpTTThu19aG2K/3Jpq6CKxmp/Z0yEfzQGCaBo+eOC4Itx3xOLmsnebokiSMHu3wYhcYbBhtjUX2gaPJ435MMwqtEHXXwJVeF4tuWIlwtFPI0ykbOvPQ4m3IemxASTPe8kN9s1iQ2NaqVotAQ2RhdTQNajfnil2K3eZIxqtCjdR0dqx2Cb8BWbQXHJVrGRnp7Ru6q1KA1DFMF6SQCAQ+XylqIR4KpOUvSLnew1uFOhOnrJDmSulxhpeUKTKWyn5sVur65J4Vt80R2rwtigY/YN6KcPbHcEZc5qEWZKtZoPdWmG01+xQitXnbEpfdlZ/npHBsNwaTdPWRi1pnW8iFS29su9Ms3LHJi6TD/k0HWdPic5WsJcWcZcP65oyMLB+7XgjkOOXERB3O8smgRm+HXZSq8tg8NFK/KoGXe2HRV8RaD8kq19VM3ZpFpA5qLTuz7oYsD2tpC5fcprltZcb3OaMTcF6tRZ0KPbJbwzdDMS42qQun08VQuBtyzNlrsBt8R9fKcBkSuDHIZrE4XC490p/3Oi+1DO9zmq/v1ja9BhW0wrIAPqxuIp9o+fq0RBw1TsTAG/m2PfRupfNyqsNbSqRJBkvHIREGiVv7Dq4k44KTUex0BZhziHOl25KVtaFBH5/pRoeVqrqkxN2xpLljGwRW67Cr9EbvGA/BqiiXOG9pRxc9OqyxTvNtYaPtW5/dBTWiNnLLrzYFJscEz5n9NXGFFXyYa7m0naXDjsr6GzPXL5S4ElFeMkRzVV5k3fTZZLHvhl2BsGcxIFewqW4oG6mFmVDEEmsx9MwpPIsvGdmp6Si2RDDI2PDZT62+1c7K7Kbyebkky+25ns0WM/m46YnuGse3fLFszkevQpEKl0i6zLKziaPhplRph7CTxo2O2Q43xG1znDe0TXCYIi5YnqkKr05W67OS64K+NHKKiqUayYlN2p1i99zXt9VhjK2AnHuZQZ+vkXlhu1szXmhMupDdsNgcjUXfB9wVvdxuy5KMFXbB45xPLG8uSEOmz9Vhq+5uxqXVzKA3NWR3Zvh1pyHYIsmXt36VRAzpKQBbQYFUjDIYig07IDuHSBRueYHzkfPPoOurzss8SxU4r/V6vz76CCPzVnIsGFrtFbgLU364ZCsejY1ld2wLWp6VfuomK0I6+KKwpohqXAZbP+MSzkCVwOfQ29Eskk1xbIK+oAxFN/J+Raa6LmGb/XZbUed2Xfqnw1bTrN1USdari4jt+ajBq0VVFfZhcMs5kRyyixELJI22Iqyk6pbO3dINDt2GVEEwqkl05cuyARG2j/YDoQpmo13n3dySRtIfnCUm1jlOKVZw28C8MtuhArWuG+mq3VgQGNhNj0tRX6x0V14i+MrNcHzp71eDgkZIvgqHS74TSNJnc8neF52IceoZDMW1EyDVNVzwrVTRecJahRcfMdy/UJ7hdadtQgxW456CQimR1vQyntzuOHbDV3zuesK23exUAe+4Y82iYSBFeStucdMTkjBPxd1+uw/dizC3KC1aqsRSMX170ewM8YChGufteZpmHTxa8hyqnY5LmT93neBqO3FHouolP4cVDQsmfMn3SttR161qkInMuqpjSCSB7w25Q7S84Xw7MCTBElR82zBmZC/yxTo6caIFt0uSL31e3sDzNe3MD9zMvkqH2yVhov2elEwlVkoscRF0ROgLTEtnujLlM7u0GkYhdkvB5TcRmsJFnrp5xd9Au2139c4zhM6UllGbE/VmW9Ly1UBjlOdwnccYecuvLzCb915qSTLnCRKauZaJOseWdtmDqmwxmckYFk6wpOk1e6OGTY1sZI65GgLQNhYJ2215dn3bKRcz2YSH45kf63i94YebQUuhZ83XXCSNurXYi2nl6357zSV8vjUcDWmWwi4kGk+AzXMRnc7HmzsLWMsY+1ic+4RLXMiUVDcZrKfiSWrIErfMGT8nRZLIg62HxZ3RNCIzzKhw0QZjTfiWxfXVaNk9nSiC0tdWR8nlWpQKO4lGXz9t2+pyWKJhgQHvHys00oGh6YutaBQjg6oSN+f9oom3zHW/aJGsWc35zAF9eaJqVjRU/FE2uljYKM66utCVTNRIVNloWfYBmZ3mxWYZ9IiDLDeeH2qLHVcj3vKcblHHIedLNWRmYkHN2yNGaDVtRAgw3WwGo+QMZ2R2Xzkn8jRbXE4EptOJhd1O440tUZWyz7jvIKWxhBEFcdkCUbHVbImnSxI38m4GkFTwO15uCaOQvJiVonoYeds/dfu9Pm7bFTuehi21RrR1m85Bh6xX9Go4zdXQGG/kie3mlIyGodHtlo2WUEOUcXZ8ibsa2XOlsJvlw+gdshu82SkNoYIRaFBmnGBlZb4FUO/1hITYGZjMnbM2nAkDM6Viz9bRnD1hC8FFKWbemVW1Hg7qWYsN1A4PBg8ToOvF1OvNg2vP6eZGufNvni0dmeO1YBYpmP/EgCpGmkXmF5e6XWGUqXzfqnY4fghqyx2qlia0G8nnirshozG72Ia3gKlCOdmrnllmVOqEMFd4wUHb4ZxwJXph1OXW85D91owctJ+pnqvqG44J2qxoiBTfamMCu7ethJV+FIwnVNwLTbeLNPKMgolu1J1hpREVoVhjKbbNdoEs2at/BaMlDYYhe6b6C/e0yZF0gdksmS/jq6WjMGo0yiDgDDNeO1ZhypA+LNiU6dPree4EsFWxqupigrLs6a3HmpdO4TBqRkilGzVI06t7u0+oky17qw1/7bSN6VRZ3IO5jFOYESObgzCjiLhx4SanCNHKWqpPMP8cZBm5KRh8vTjo4hzPd0PAKAsbZTq0zHcjnSEzZfSvka2Z5nm34jrLiuri2tTZmTQpSijdmyk7tCfPB74pD7XiO5qn260aL3DRmDN+3pBcdaZFk2qV1cIXtz2diU1FivzgbXpyibLVDb4RM+XadcebsxDqGcM3mEXpXaVhdXudiRab15nmHY8oVc4IzmcjPMAauMUuuXvhWqsN1aUOz+AErvFrvK+ttZX62QD3PgZr5WF5mXlUtZ7B8vWEGkuvHhmLIi+tw/iG4OJ5sWCsxVIGkxLqwCaNbU7ybaaPUre8YDOu9uH5fmFeOdMbMZ+Ed1kG46q0BIXlPMbIKRqPe1QS4VbVy7QgklVAa/E8pEa971bOUsQ6hr0d1sH+gLQDf9gcNuex6lQHtDnJeKUt3Wo1xZYd9CRdc+bKFysaPaU4fe4pUQlw/FSlRdmdgJfi80lmEltY9q7JZCf8IAi3zeBjPpGz2TIT4l5a3PhR24HZiDTQnHBZh6pW+A1elk5bGtuWamRW2Rpa3LIzx7ktLt0RzE0beYYh9Dh4PjLMcLI5HTbSYZmkap8kycKI+uvcnR0uzOU03xdRUWR0uxZEBxnwzYbh5n3Fj3NWXvNpowfJMSpCxO3UReQt/WJpjQrsVpbELogqSp25tvSyzPIFsadoFnf25epkgIaIeXl9mQ6nn0fM/413y9NZ3//akePjdPD99dP9eNk1nc93Xp//O8L98vpS2iEQ7XHUWiWN/zyO/E8HrZ/++dcXE53h8Qp3enPW1+/n9LXpT7+c9BJmTlPV5fC1ypPmfuj7CixbTb8gUX19Hm6/3BVNi/r+7EMxcGXa99Pmr3X+1QmrIq+mmxPzMnWd8LFmuvSf59CvL84A3Bfa1VeMJL66ZTFp/XwnApRF35C3+cvv/w8+W5UwDCYAAA== -->
