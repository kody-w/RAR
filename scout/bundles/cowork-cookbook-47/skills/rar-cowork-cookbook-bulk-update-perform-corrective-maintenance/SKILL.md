---
name: "rar-cowork-cookbook-bulk-update-perform-corrective-maintenance"
description: "Applies a bulk field update across perform corrective maintenance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_perform_corrective_maintenance", "rar_sha256": "3390c559cead385d344fed955958b92f9bae20a4468e6a4410da747333454273", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 3390c559cead385d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_perform_corrective_maintenance_agent.py` first:

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
    "version": '2.0.0',
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

<!-- rci-capsule:v1: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 -->
