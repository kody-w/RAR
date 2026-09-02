---
name: "rar-cowork-cookbook-bulk-update-develop-sales-catalogs"
description: "Applies a bulk field update across develop sales catalogs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_sales_catalogs", "rar_sha256": "4b4f9552c9d82ce873598df7b3e61f38311f7a3cb0142cca9d1a5c9af5082ee6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_sales_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-sales-catalogs:5dcd4ece29f908a026b8abd6cd2865e523da3190f8afe9ee041a3c8397ea1840", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_sales_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_sales_catalogs_agent.py` is
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
