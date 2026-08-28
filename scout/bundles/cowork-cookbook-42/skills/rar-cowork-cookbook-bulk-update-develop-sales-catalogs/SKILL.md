---
name: "rar-cowork-cookbook-bulk-update-develop-sales-catalogs"
description: "Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_sales_catalogs", "rar_sha256": "4b4f9552c9d82ce873598df7b3e61f38311f7a3cb0142cca9d1a5c9af5082ee6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 4b4f9552c9d82ce8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_sales_catalogs_agent.py` first:

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
    "version": '2.0.0',
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
