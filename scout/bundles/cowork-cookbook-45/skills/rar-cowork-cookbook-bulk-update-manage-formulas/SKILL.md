---
name: "rar-cowork-cookbook-bulk-update-manage-formulas"
description: "Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_formulas", "rar_sha256": "f65368002c1578c2d9887665fceebbdf8942f61525cebf43548e1162547e69d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_formulas_agent.py` and embedded as the fenced Python below (sha256 f65368002c1578c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_formulas_agent.py` first:

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
    "version": '2.0.1',
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
