---
name: "rar-cowork-cookbook-adaptive-card-manage-work-assignments"
description: "Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_work_assignments", "rar_sha256": "7751c10f3b04cd2c8d8510b1d5d6bc3e6a6da53910da527a567128228b1caf5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 7751c10f3b04cd2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_work_assignments_agent.py` first:

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
    "version": '2.0.0',
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
