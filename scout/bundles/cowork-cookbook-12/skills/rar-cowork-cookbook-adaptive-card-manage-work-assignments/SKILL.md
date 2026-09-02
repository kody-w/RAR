---
name: "rar-cowork-cookbook-adaptive-card-manage-work-assignments"
description: "Produces a reusable Adaptive Card JSON snapshot of manage work assignments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_work_assignments", "rar_sha256": "7751c10f3b04cd2c8d8510b1d5d6bc3e6a6da53910da527a567128228b1caf5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_work_assignments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-work-assignments:28b80862d1db0c321029f50e71433e99bec26869303670a9045d40b06deb3697", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_work_assignments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_work_assignments_agent.py` is
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
