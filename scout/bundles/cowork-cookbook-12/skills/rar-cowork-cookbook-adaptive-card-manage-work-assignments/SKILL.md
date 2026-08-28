---
name: "rar-cowork-cookbook-adaptive-card-manage-work-assignments"
description: "Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_work_assignments", "rar_sha256": "8075af455d9b53b0a7b9e5fe4a976de41e89bdc3d1a5e3ce448c40bf7041d8b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_work_assignments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_work_assignments_agent.py` and in the RCI capsule.

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

Manage work assignments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 8075af455d9b53b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_work_assignments_agent.py` first:

```bash
python3 adaptive_card_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_work_assignments_agent.py   # or on stdin
python3 adaptive_card_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_work_assignments',
    "version": '2.0.1',
    "display_name": 'Manage work assignments Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f7de86f4189a95e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageWorkAssignments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageWorkAssignments'
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
    print(AdaptiveCardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
