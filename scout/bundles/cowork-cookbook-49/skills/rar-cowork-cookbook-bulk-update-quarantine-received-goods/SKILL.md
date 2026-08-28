---
name: "rar-cowork-cookbook-bulk-update-quarantine-received-goods"
description: "Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_quarantine_received_goods", "rar_sha256": "51b3637ab8a34fc5029849b1647ee2f27e4865ad560044b212611550af395d34", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_quarantine_received_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_quarantine_received_goods_agent.py` and in the RCI capsule.

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

Quarantine received goods Bulk Field Update — Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 51b3637ab8a34fc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_quarantine_received_goods_agent.py` first:

```bash
python3 bulk_update_quarantine_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_quarantine_received_goods_agent.py   # or on stdin
python3 bulk_update_quarantine_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine received goods Bulk Field Update — Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_quarantine_received_goods',
    "version": '2.0.0',
    "display_name": 'Quarantine received goods Bulk Field Update',
    "description": 'Applies a bulk field update across quarantine received goods records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-quarantine-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c82986f13dd5fa2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/quarantine-received-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-quarantine-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateQuarantineReceivedGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQuarantineReceivedGoods'
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
    print(BulkUpdateQuarantineReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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bDwGI9iS2YO3PvqlbzH+jU1VpsSlCh18ghuO6X2C0y21waA2unQ2qZYbtSNuXeQc1XWzudOJfaT8sDshqwNC65fl9orum+LmLv1tJDKsHCLjyFVEH544gmMwdc0YDEXZSJ2Y66obQUe/I5d6iY3yubum1BAzW1wVlb6ILpubzIx2eL4FAoWdkB6VxPud8LdlHw67YvKlXsTNDby1b0vDuCndNEGeuZ1OR9wIDjdPOYOtQywdyok/tWhTFBi9jBCpX27xiUPlplsyELRvuLW8vHFQcszXkr1lT4eLFLGek3A3xrCOdlQol5tPjYdribKenHk9JElY3GkQt6u4JCkor7hl9y102wWnlXczj/clL51hZYWhgVUQ1oivVvad0jI4kg7KZcks08E7gMaQo1c5R2tFAt/XCc6HhXZtmgDuvanx9XDj+b3ep0vJFJYDLEx9SkzlVVWcIeLPyVIEXMk+ciKXRGhKxLSSXiGU7A+u4doovO/2ugPJ/F7dU+e10RW9ztfqao+062jvbuQDli3F65ZARuqGtipd0i463qjY7q5wGxQ5vmGW+uYwRUtUONxuyKFWZPnKOKhnsn61YrWu1xW8JCv9ak+SqcW3AEjnrMYVXyby6oId195IVIeQWu0MidQ7okwaqLowlXRaEisoabiV3928CitD0HdaawRbM1UEkZHvSiRT0heSJH/88eXDy3w8/Txk/ntvkucjv/+1k8fXQ8K3106PA+bICz8/eH3+m3L9/OGlCTIg1es5a5v3yfNA8j+dsn78l95YzCTG19e083uye/d2NN95yfyLo5esDPu2a8avbZX3j8PeD8CU7fzTh/br81D75aFeUXePsXd1XuYfIsxn0RVY3lVfnz/beDye3wBFYfY2qwMbP+9JPRyBx7Kg/Yri669RU88qP1+EzGe285uQl9/+H9AgUUPeJQAA -->
