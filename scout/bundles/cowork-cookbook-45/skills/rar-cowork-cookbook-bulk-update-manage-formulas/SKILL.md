---
name: "rar-cowork-cookbook-bulk-update-manage-formulas"
description: "Applies a bulk field update across manage formulas records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_formulas", "rar_sha256": "da977b07cf1503840cc15e446281007bce5c9dce850fa3f8121a95a4803f0c48", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_formulas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-formulas:ff18c2b4563b02fa368b4af4bba574acf3a2497afcb06ec89c67afab09d087d2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_formulas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_formulas_agent.py` is
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
