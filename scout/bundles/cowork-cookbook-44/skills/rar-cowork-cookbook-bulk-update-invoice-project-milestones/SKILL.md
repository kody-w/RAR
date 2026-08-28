---
name: "rar-cowork-cookbook-bulk-update-invoice-project-milestones"
description: "Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_invoice_project_milestones", "rar_sha256": "793431149676e016ab118eab1796c05982d58e72d378beb1dbad8762f8686196", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_invoice_project_milestones`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_invoice_project_milestones_agent.py` and in the RCI capsule.

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

Invoice project milestones Bulk Field Update — Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 793431149676e016…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_invoice_project_milestones_agent.py` first:

```bash
python3 bulk_update_invoice_project_milestones_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_invoice_project_milestones_agent.py   # or on stdin
python3 bulk_update_invoice_project_milestones_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project milestones Bulk Field Update — Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_invoice_project_milestones',
    "version": '2.0.1',
    "display_name": 'Invoice project milestones Bulk Field Update',
    "description": 'Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-invoice-project-milestones',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-invoice-project-milestones',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86b957fa7238f331',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-milestones'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/bulk-update-invoice-project-milestones', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateInvoiceProjectMilestones(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateInvoiceProjectMilestones'
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
    print(BulkUpdateInvoiceProjectMilestones().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
