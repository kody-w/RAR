---
name: "rar-cowork-cookbook-bulk-update-define-sales-quotations"
description: "Applies a bulk field update across define sales quotations records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_quotations", "rar_sha256": "89cee9c85a83ee47656bbf84e068758b8a4ac95d28ac75020f6e87bce8b81c5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_sales_quotations_agent.py` and in the RCI capsule.

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
