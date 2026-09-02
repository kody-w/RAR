---
name: "rar-cowork-cookbook-bulk-update-invoice-project-milestones"
description: "Applies a bulk field update across invoice project milestones records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_invoice_project_milestones", "rar_sha256": "56ad9be129217ee746185fa27830702ca52e4a619ec9bbbc9691ec6abd42917b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_invoice_project_milestones_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-invoice-project-milestones:4ec61f45360c4703cf382b775dfb2cc0d3af0027ee48d5f4cb4a453e847ea025", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_invoice_project_milestones`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_invoice_project_milestones_agent.py` is
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
