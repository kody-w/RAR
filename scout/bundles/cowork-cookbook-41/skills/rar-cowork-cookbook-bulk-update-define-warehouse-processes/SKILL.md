---
name: "rar-cowork-cookbook-bulk-update-define-warehouse-processes"
description: "Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_warehouse_processes", "rar_sha256": "313a3e051a63339cc233cbaea75352e90ce90a126e848f191daeaac571780ae5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_warehouse_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-warehouse-processes:e953a147d30ed5b3e83792b32cdcb24e12cf3ae872c8ecf81624152d16fcbd59", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_warehouse_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_warehouse_processes_agent.py` is
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

Define warehouse processes Bulk Field Update — Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 313a3e051a63339c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_warehouse_processes_agent.py` first:

```bash
python3 bulk_update_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_warehouse_processes_agent.py   # or on stdin
python3 bulk_update_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Bulk Field Update — Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_warehouse_processes',
    "version": '2.0.0',
    "display_name": 'Define warehouse processes Bulk Field Update',
    "description": 'Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a8eb01f1128b3147',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineWarehouseProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineWarehouseProcesses'
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
    print(BulkUpdateDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZPiVnf+K0rnw9ihp7VL0G+5KohVuxBCgDyuHi1XC1rRinD833MFdM84tpPXqVSFqe4BdO/Zz/OcK/WvT3ZTh3n59Pq0BXaGrOwkiUJQInbmIbO8y8sY/pfHDvxB3Dyry8hp6rysnp6fPFC5ZVTUUZ7B7dOiSCJQITbiNEmM+BFIPKQpPLsGiO2WeVUhHvCjDCCdXYIwbyqAFGXugqqCu0rg5qVXIX6Zp1A3EmVFUyNJVNXPSBfVIeKV/eeyyeAW0EagQxzg5yWAJqVpVL9Aa8DFTosEVE+vP//y/BTB90+vvz65iV3Br544aNPuZsz8ZsT+3Qbt3QQoIrGzAK4tehiRDH4uQAmVpPAraDny+PRDBRL/Gfm3f4uhH0H14+uXDHm8vjwN/3RoZR0CpM7tqgYe4tqF7URJVPcvyDTp7H7wtm7KbIhVBQOaBS/3nd8k5QXy03Dth7uSlwDUP3x5yqEJ9hDuL08/InkJ9cGIwPcvg5Tihx9fkrwD5Q8/fpNTNc4JuPUgDFr98vb4/BALF35bGvk3rT9BqffEOuDL03fODa+73YOfcOfTyymPsh/ugmEmW5DZmQt++PGvxLohcOMhpf+U3J/vgkNge9Cnh+E/Pt+C/Asyejj0IfOv1RYwrX/HE7j8Xd0z8gjUX8m+xf+/iE5geVUfEf9TcX+2YfQT8vNf+vbfbXhG/C9Pc5BELawOJwGvyK9vW20x+/mT9+3LT7/8BkX/j2K2eVO6NwlvqZ1FPqjqt7efP1W3rz/98vOnpoC1Buz0rSmTP5P5Z3G96fldBB+rfvj9Xqh/l8VZ3mXIR6Ujv+bFv5S/vSCmnUTet++rV+T7fhleI2Rw4l3pPQTf9UwFbf0ujj8+/QZRIoPeNO7tMuzyf/1XRI4GqMr9Gtm6OUQgmOA6SsFgvBFGFWI8mvrrVuQl6SX1viLw26HdIUTYTVIjq9KOkgHZhowPHuQ+8vXf3RuUfnYfUIoOGPl2R8e3Oyy+fcDi2wcsfn1BjBAqz8soiDI7QfSppiF2ALJ6UHsrkKpJP7eDZmhVdEcefcYPqFM1CfgH8vWfU/V2k/pS9INDXzKYIRuu9JAapEVe2mWU9Ih9Q/e+Bp8h2EJUKfMkcWw3RoZfTfEyRGkfguwROxfiOLgAt4EMkOQuNN+PIEA/w/RXedJChBwiWsVRkiBeBBkA8kp/Ix4Y9ddB2NevXx27Cr9kd0gmkTvhVChc8GEw8vkzJAU/iYKw/pIBN8yRT7/+9gn5D+S/23UTPujQIEHcogbLOkGEraogsEebFC6rkKFAIADdcvjrb/d0DNZlkCFhZ0X+wHj1kKLvCmLw4J6j9wRBnwcTQfnQ9Pu4IV0I44JENYwW7Pbq+Us2iMjh0rKLIE0+gnjffA/9e8bveoacVI8YwjzdSHRYe6vFIZkDub4gvI98RAq6C/NaDxkN86qG5VuAzAOZ28Oddv0thVleIxXsoMrvnxFYMl+yQfJXB4oegpNCmLLrr4g80yDj5Qn8NQToph7uzrNoSPyjZO9fQyHlJ1hj3LuIF0QBMJpIYZd2EZZ2BW7rfPteEZDp3vdD4TaSQfof+B0MObr19q3y5n89XQzsjyxvE8l9CEC+NASGU8j/69AyGD1drfTFamos5shCMfTjvcKGQWtw+D6bwckBgfvu7fJtmngHnndI/pIlEcxK2f/jvtK/FdV9zR3mmhJWjD7Vb/KH9i5vcqEpCD/kuixvsfiSvWP/MwwMTEw1wBjs4HjAg/xD4XD13dIQtunw+dsc8IjO0A2wnpGicZLIRXwAvFvp12E5NNYjD7BOwNBksBPc8HdeIVA6rAEoH4FGRLBgIT/cQqfABoGz0z36H8ujIS3QCq9xobWwg8ALsh8KGuahggmAI9KwBkbh000UkgIYY2jiR4Sr0C7uxgzD78NAe8hFng518V0GHhdhcQ4kA/V9dB6UasMqgrHsYBJgY13umf2w85EraGw6dMFt0+/T/fAV+Z6k/jF0H7TxGwXAeX3g9++CAyG7TKsbCkHmjSvY3yl4FBCshBuVv9zZ+E73H7a8/mHi/+HvHQpu/Lr7feZekbCui+oVRe8c+E6BL7ALUFgjUQGqGx1+vvfd53vDff5ouM8fDfc76fdgvSJ/z8LfiXiU9iuCv2Av2HBJilww1O7jBQMy+8wdP1PD1S+ZDr5l+lEOA7pBxHX6D5J5XwKZJihBMCy+k041cFUH6fGGdTfS+KiGR69AKM2CgSGr/LseHnwacntP3Qcmw0vZgPbeMOMFYDgDJYP5FXh6zZokeX7K7BT8s2efAXth0cKIDMcmGHI4N9URuH36mKGGD78/9d1aC2KCl78OHQZ5Ds67z8jH6PqMvB8mbme0rIGnqZ+HsXlQCZfC/z7WfhwpHfAEj3B1XwzW309Iw7T2mKL/aMTQWI8iGWx579RB4x+EwDdBAMo/ClFvb+zkARdVbQ/sCEn50eQVtNODE9UzAvMHmw/2E4TJBm74oxqopwTnBvKxN7j7LX7f3Mrvvvx2C0N9P2b++vQOG8P7+3Bwrx244W+OcUNg3+n3bRBvD0Juw9Ytzrdh9Q36GA00+92lYJgZ3u4F+fQKkQc8Pw3RLCM4gV9v5+unu03QmW9jLpQAMeRzNYwNKOwnKAmSeTE4EkP8+07B8HXk3dYPb17/dDb+n8HgFUxo0sYp1iMx4NEOCcYkOyEcknA91yEogBOuT9pgzBLuGLj+GGcICqcJD2d81/HoCTRlyGlqP0xB8SEb0ImPkP8vp/anuxTIIwTNQDEkTtokwGjcZkiSnLguQZKuYwObpUmaABPMhT82TjBgTI19fIJ78Jrt0izOjjEb0IO8x8R4N+3tfTp/z88dGd7ucwXUSMDtY5fFKW/C2owLSMwhXRgQ3GMHQyakPx4DCu7/2PrI0ZDCu/dDDcOxBY5q7aDn10fOh7pkKLhyTVX89P6aoRPTZgjW0UNnVDLgaB1Q3slMAcssR1Tr5dr1BS49bbtFSorLnlN7fY3Vm1042m/McrsKDHqRsZxW1WNaZns+Log4Gu+jwGylTIiv1phN1MnYEoNo1pkqjgnxdoWneWKn1SJLwmO6r6tGEBKTESz8nER+MDKIbXFRRygaWer4ejVXwi7K28XyhHvNQbaXlXmMvXFVmatevPDF8uhZMysWMmDuRVOpe2FuMwc+jQmekcRK3no2aeqxfj5u8uRYKoAh+X4ldCOfpC9oe8VYPzFcnz2z7l5boEtCdxXr7AjbXizcdCce9tTSzJNLIRKi1WNRNple0MQKXdo5Vsmy03YhZlZ1MPJC+aAmB3y56HOq5M/mjG+MaHJs5a0+C4+S5m6lRS5KQYBd9nItS5eNtzkWpWmGtVys7NH0XG4nSqUzKp5FdWGiG3K+VuG1bNkn1UqJ4xVY0svzkV1uznEctwvT48VFqBL+yjrtJVlPC6CZ1yxeCJznxBERBDP2YtMaZ4lj+Vq4deYSTm+d3cAnDDG3gYjv88gPQ2FXcQzeHDVj56S5dprj6WY/a49KGGNhuStTo1aM9Xp5jtO+xRNDWG8rI1IkDmghAOKOF7HQiIScXk3nZwIIoHHHBDhl2UZO8Ots4o6bBqCYUHlnekbY5KkDVYr328TLWHubn1TJxqNZaFaOFduwyA5mepHTNqG6PVDwnS7ioRLN/XFlLmOhouQ1epBTseJRKj0pXR6i3MWxlUgTfDuLZVlau4sqNIjVVYUdY+yMMyvJ7L5jTockZBVPWagTQ+cNNbHwbZbjXgh/7JxwcC4nz97OZJsOW1xG2QEHs/lItcA8pOV1Oo33E7ychTJqjI8UcYVF71+Wl8A9iKd9e6VmCpeMREasq/UqHE8ElenT8DCjpNo2BN5pBaPl6zzM5oSgj+VVGHWqt2gFydrVsZ4pimAaudp4Oj0XWFVOZDFiVtVFsYWwDBKNi6f0xgr3M69Y8bnhGmqw6TbEIVoxQRHzsyLLjriVRaG85q8A9M5hxmhTh6bxC6vTxBaE7uJ0PoQ8LnXVMdn06GpFy7G2Fa54NTYcX9k5lcKkFMpRsb1yA4cYt6OWWV5LWhY1XEupqXg9JKRQVH7Rz5Z9vpiWDiacsTySVZ3gj6buMHu8dVKLDalr3pL702nlF4Y15g69wqyK4yrbBbk4oS+bzWzPpCY4C65ksPSyonTZI9D5tSUp6xzx/rXEzzI4tvyRUnE8M84aLQmbDOsSvlQCziqqsisEenNejs+HbeCcm96+nsIWFYIyX033HdlimhatNhlvb+36lPSAy9CzMBTU6ZhRST8ujrao880epdZSvC0WB2wFgX6dtVpjuZuRRR33Lb9JyzqRZ5GxP1UyR50MwJeRcGQ8QzxtI7UJxETIdTfve8ZRuVXYylWz7AqlajSaYIRtTjrydTPBqaDHY2I9Rw8JnrSbiJHn8jkOC+pEbogE3xE9wGxnH3v6aFV33rJdo9mp0/CArjFK1UMOo6ldnHeORcBanY7kBdUr8jwMlu4WX+2p1OuocuXO98puw0PcGR2dJb+U1Gu1NdbdDvLqVjVc6TJGpSXRxUbBFpRLLfy0v3rXkKPzpTedb6rzjul1qZ2sCPtkTflGL47yYi3ws8VkaYeMUkcZ7CwOq8+HeDlaVKconEtTaRLFxEhArydjRrlmvOSDkyTH5sGaiebIX24p10t6KhSm52PtWYGSbY+TDHNkgGN9gGOWoaotSVy8jD5f/UzgpHGfnBRGU9eFIMq7krqmZtZujWCzz4zcNnB0XMrLRMGJtVRJS24TjtPK1A4RBbRTh3m+TncjdCTn6ygZ7xT1JImTkbnmpKnoRfoiLG1NUAtzsz2Acr1xrd2MTh2WEArIIRhDLYRc0dV2s+Iv1ZkW3bTg02AyEabQqSOwrdOu06ZH+dSlq7WnG06+Xcr2zoODI2QB2k2zlTL2NdUU88wbMwv8KgV277OGSI3PMdr2bkerdBCJ517qsulB4536tBYdtxMhEJUCnfR7kQD4lC0m4qKYrjNmPYnPmaiTuBWe5t7+OKGn+SksOfPCHSn/AkqcS7O6lZKrOe3hSUHqLnI4iRPYMXljiQaN7hh6fYwnC4tyKn1eK9JF68KuDyN6cTxZE5tbWAk4WKHZ77ytjnYxNtsvZQEWFRGiZ3+XS0Rg7mdSuCfWsstrY5/wmWRXbQ/yarqkmZY/mPtTtJltBewSldaZ2sCinO8F/nzAdP0yN5JpYFhzO5Q7WQsyVVxuV3vzsq3a+XjZ7oS6z46i3EZpqXPVpTQzzZR6IdiduH7ttW3duuXiIu6xKJbmTheXp3xx9ZpmPOF7S6TXe2FaSdoktRP2eDiSZYzPqUY0y3GvtNCr1ttg+PYiTv2KbE65GYGTOw+O85lAXvaxu1zv0DaG/YuzcbFtV4t1QW5jajmz1X0C+BTi8SFXrbGVqzW9s6f6cZepC0DM9htFiVadHoY5Jm56rVzkB5ebiagdceNGIaSWOIm6ak+3ltaix3V6KTqsta2AWkhZzU9Po3lfxwfYFaxaSE5vCvl4IkOKqVHG7iS1OUOIkzcew08mPJUFhJpqOo3tVaWIGMM7CHWqKrhGHJsQE8tLPSGLONApS97w/eR8nhiX2aI3p1yXnRVN8l0zirMAxcJFqJxWbhlY3GwEDvhIj8nNjrMC77QjcAdj6W1uaDmwaCyU9qKyU3X8IHRn1SPdeivCsU7ky3xRcY05LRRAJNvrDg6kk6m4mnYhvHpI604RyoKadfp02ey1VORmV9fcHFn6bMfbZcaJ652tWuLWWdr6PG9TA+TA9aREKQ22KJVuNm7ADEvGVIdy2C5bnA6WO88KfFuzeQwSntmMY5mWyCaMjnJcRBQmG2K/4zUhmaAj3TTVzle9ed8TfSxci0jCZaxVYE62hp2FagoTujupDXM8gUQTM35Ol6sE6ypjb5pu1W/LhE7kbIfHObskqgY10mo2OptotVmdMmrppad9UxRAHoVsu95KqchPG9qrD3OzXmtixBaA70njVHpWberdqaV3kxXGssESzr+oPhXGy35/UXQgEcI2cmeb3dJIo0PMtjN9py0XMbELwwu3xbp406wqasFyi5IqpX3DY460tydljoGdw7c7RwsX1ioi0UAcSdcqc73qtAsglBQzU6F2jbgjNr2dCyN93WkLiqPOM63meozbRIEhUxZucHLCyd6OYPRlNN6es7MkbdFumZ63tDl1jbFe1KHLpPsk4kgsVFJ1dNCkJHHZIIC4YY6tS23TWz5ZjSdYTRebDddi6FFIWpqNt0wrXq/41D2QS/occrOEu8AuXpz1cjeH23uWOlWWJh+v43OiVaIfKGDORCwpl7VC0+3R3lnpbAXWl2R3laLDaT65asomGXO4UWPtxbJ03YLT+TjmcG12uG5TK05Jj8qbnY6blGqbaKRn+NyY6frI02alnLjFOV2Ja+o4w6e9slzHLFdwsBbEeirvZMKICaJeGzZ66Iyl2XtYMDtOjcKj/crMOFxBK2q29dxswzP8GZsx3mZ+WvT4QmKU7fUyZ8+GhZGzMKrE1N9Za2Kp71zMw4TGb05r4jwbSWUaYl6N+XtTmUazfcGX7FlNJcUiNYLMyHMjL1h6o+IRqZJ7Zs+oaxb3LqoUlX6NQqLzme2Z0rVJ7rEJAc+16ETK3DWNEqZ68Yr2uPcqn2L0mFjW0oZVLqiiCuahSRcYq4ZBPR/PpdjfJyob0Yy9ZJl1WdPnuvfHcplHykXu8iT2FqG/RrlaX+e5hc3TlWmCRhM7Hl+RXByAFS1tLJapL85aOya1b0bGhPdLfbxWynxyXCkoazkdbhYnyqGual+3BDWrZI3MgcQbzJYlvFzDgTqzRiN43jvm/k5a7ESGRMcYesHGScmSB+3CoBsvomuBHUFepLiJN6XWG3MktWcblrvMHJWyQwNDzTuKWa8pm0724RTviGJhaNUa46lgLLTuqvNXC1SI/TUYV1jXkG7pZMcYwtdebzyFY5upcoTgYajK1uuJFuyOjJ5y+pVnDJlvA6dvF8p45Ejr1NCcUa3yfsJiyoRceFtpJaFZ3YXjQ+Y4phv65eSS2JvOPIpYxqgbbe9Namo157kWJhjvMBboC2XO2vXlWpesIqJ7dEJR1CU2Ms+9oJwccstJMy/q8fJCklbjV54cLgn2cKoDSeUXzqxVr7JzIKv26tsqA5yd1EoXjr6GDd3QNDlj/KPVTKftVS4taumiKwsOpYtNfQ10tYtB6Re62629/oIeDmC3WHPBvGqN+qJcNuxV7Ce70xWdBmv9pGWqxIcdHPzjmQOUgIaFOSvHwBUAxVxPdLeOwmM0muLjDdUyzTZjqtVcp8ZpTGXsZr0LsPhCNhOsTzpXX3Nc6pKcsJCO7IK4bjFiDeaXw76l6413OJTxhUfRK0+dQNoE9YhtcJuk2BoebV2ycrwruYgvylU9XtmagydZkdgqkIivHQE7HQ1IwZ9PXI6tiMZLLGXUbZeY6OajFnDaRJyutLW21/C1fwovok263Mqt4aF0tKdP8MBdtTswdeNlS5hrR5+7kpqReFmda9vL2TbBSjm44E65OZ4impyWmKVx81TZTJdLdINzZDkn4XFhsZvTqpZZjArPRgdhrK1DLW96hwn2ExblYqLBu4AMp7YE2iqbd+1+z5IdrGC3YVjabw4mQEccmIzWc21C+4SyQfNiQ6ClupLKCdHCnExm7L612Vyh5+6FrdhSNlymISkNrarWja/MuGTmBBnUsLvn/TSkdTqa2TJnHHGTtUc22mWL7twe9ZxZlmydt+FoIo1tENrb2XEpbkdSxjKMSXO6pOxJEnObNhgbhtfbLG5Jc9/wFwmvmVTdNQarifN5rmP+htf0XS4I9slZpEblEsWqaGp2T0tiAweSqgC4ymRUtTuRM4iyTHYV/QKjAw5O63OqKO1KYmkOT+f5dFmGMyCdNku65VJ9uRvtVuNUMTDGxafpyg83hE0rIJlvM/uaUMusoYxIolYJy0zimY+656U67Vt4bh9dWbPkJ4qUEOsxSRzTyaTdWI5fWXvfVTbry6g786Re8InjplrXcpuTqRF7OJ7bdObvugKvVG3q5ULnX/GE3hzP80LKt9PMgXavUZ0/7PYhpDqU38t5N6LO1xTg88xj14eoampqzKEzrqjMahtPp9Offnp6fro97X16xTGGJZ+fhkcEjxv9f/8WcXCNireHPJIlmeen/7u7lvc7iO+PA2+3/YHtvd60v/5dU395firdCJp1v7VcJU3wuF35X+7Rfv7n7h4PMvr74+vhCealfn9mUtvB7RZ3lHlNVZf9W5Unze0GNwx8Uw1/ylK9G/h0czAt6tu1D4eehj8sGZ4R5HB7nb89/gzn9vXwbA540fuqGgSPJwPPT14P0xi51RvJ0G+gLAafH0+ohlu6wyOqp9/+E+p5NOSwJwAA -->
