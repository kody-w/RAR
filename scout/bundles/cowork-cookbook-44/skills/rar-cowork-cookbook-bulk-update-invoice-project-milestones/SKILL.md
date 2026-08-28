---
name: "rar-cowork-cookbook-bulk-update-invoice-project-milestones"
description: "Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_invoice_project_milestones", "rar_sha256": "56ad9be129217ee746185fa27830702ca52e4a619ec9bbbc9691ec6abd42917b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_invoice_project_milestones_agent.py` and embedded as the fenced Python below (sha256 56ad9be129217ee7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_invoice_project_milestones_agent.py` first:

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
    "version": '2.0.0',
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
