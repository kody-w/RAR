---
name: "rar-cowork-cookbook-bulk-update-manage-formulas"
description: "Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_formulas", "rar_sha256": "da977b07cf1503840cc15e446281007bce5c9dce850fa3f8121a95a4803f0c48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_formulas`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_formulas_agent.py` and in the RCI capsule.

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

Manage formulas Bulk Field Update — Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-formulas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 da977b07cf150384…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_formulas_agent.py` first:

```bash
python3 bulk_update_manage_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_formulas_agent.py   # or on stdin
python3 bulk_update_manage_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage formulas Bulk Field Update — Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_formulas',
    "version": '2.0.0',
    "display_name": 'Manage formulas Bulk Field Update',
    "description": 'Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-manage-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e866a7036aa530b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-formulas'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/bulk-update-manage-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageFormulas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageFormulas'
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
    print(BulkUpdateManageFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
