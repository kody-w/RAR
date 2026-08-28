---
name: "rar-cowork-cookbook-bulk-update-develop-sales-catalogs"
description: "Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_sales_catalogs", "rar_sha256": "ca8b4b2b51e1387467c708f6a497fef85f22578e0367c628ffbc93b60ce18073", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Bulk Field Update — Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 ca8b4b2b51e13874…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_sales_catalogs_agent.py` first:

```bash
python3 bulk_update_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_sales_catalogs_agent.py   # or on stdin
python3 bulk_update_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Bulk Field Update — Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_sales_catalogs',
    "version": '2.0.1',
    "display_name": 'Develop sales catalogs Bulk Field Update',
    "description": 'Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdc358bcaab5f7fe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDevelopSalesCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopSalesCatalogs'
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
    print(BulkUpdateDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
