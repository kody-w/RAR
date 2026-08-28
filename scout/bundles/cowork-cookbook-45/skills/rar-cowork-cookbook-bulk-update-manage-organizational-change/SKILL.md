---
name: "rar-cowork-cookbook-bulk-update-manage-organizational-change"
description: "Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_organizational_change", "rar_sha256": "1b6167ada46eb807421bda8b0d7d434c838c1a9badc43366f98aee8bdcc4c880", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_organizational_change`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_organizational_change_agent.py` and in the RCI capsule.

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

Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_organizational_change_agent.py` and embedded as the fenced Python below (sha256 1b6167ada46eb807…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_organizational_change_agent.py` first:

```bash
python3 bulk_update_manage_organizational_change_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_organizational_change_agent.py   # or on stdin
python3 bulk_update_manage_organizational_change_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage organizational change Bulk Field Update — Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_organizational_change',
    "version": '2.0.0',
    "display_name": 'Manage organizational change Bulk Field Update',
    "description": 'Applies a bulk field update across manage organizational change records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-organizational-change',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-organizational-change',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b72ff409516ba61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-organizational-change'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-organizational-change', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageOrganizationalChange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageOrganizationalChange'
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
    print(BulkUpdateManageOrganizationalChange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
