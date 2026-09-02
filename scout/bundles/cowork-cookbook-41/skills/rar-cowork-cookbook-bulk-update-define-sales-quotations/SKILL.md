---
name: "rar-cowork-cookbook-bulk-update-define-sales-quotations"
description: "Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_quotations", "rar_sha256": "89cee9c85a83ee47656bbf84e068758b8a4ac95d28ac75020f6e87bce8b81c5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_sales_quotations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-sales-quotations:186ad44170b0852973a321d3e150f525fe3a72c0f62f2d33b04dda91b7169b86", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_sales_quotations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_sales_quotations_agent.py` is
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

Define sales quotations Bulk Field Update — Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 89cee9c85a83ee47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_quotations_agent.py` first:

```bash
python3 bulk_update_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_sales_quotations_agent.py   # or on stdin
python3 bulk_update_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Bulk Field Update — Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_sales_quotations',
    "version": '2.0.0',
    "display_name": 'Define sales quotations Bulk Field Update',
    "description": 'Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c937ab11d2770c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineSalesQuotations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineSalesQuotations'
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
    print(BulkUpdateDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
