---
name: "rar-cowork-cookbook-adaptive-card-adjust-inventory-levels"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_inventory_levels", "rar_sha256": "2add617758d006a0c9ab61306e0cfd6791a3269b7a2eb9b29aa979aecd214b75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_adjust_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-adjust-inventory-levels:d05fde5e1f13e3973d88a1a39b5c48444768bd5f18ec265f5b82652410e60ac8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_adjust_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_adjust_inventory_levels_agent.py` is
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

Adjust inventory levels Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 2add617758d006a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_inventory_levels_agent.py` first:

```bash
python3 adaptive_card_adjust_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_inventory_levels_agent.py   # or on stdin
python3 adaptive_card_adjust_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust inventory levels Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Adjust inventory levels Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of adjust inventory levels status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-adjust-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2437b95c31d7167d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/adjust-inventory-levels'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-adjust-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardAdjustInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustInventoryLevels'
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
    print(AdaptiveCardAdjustInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
