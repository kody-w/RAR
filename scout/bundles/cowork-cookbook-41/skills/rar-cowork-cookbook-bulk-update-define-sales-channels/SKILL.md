---
name: "rar-cowork-cookbook-bulk-update-define-sales-channels"
description: "Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_channels", "rar_sha256": "52ca881f688a3ea5c12062fbbfed390e339ecbb1b92b9c4a16c037b1c6083033", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_sales_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-sales-channels:1e2c617ae904c6ea79d774c7d6fc4c58d68c9ff16537ee4db05128334a8a2b45", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_sales_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_sales_channels_agent.py` is
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

Define sales channels Bulk Field Update — Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 52ca881f688a3ea5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_channels_agent.py` first:

```bash
python3 bulk_update_define_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_sales_channels_agent.py   # or on stdin
python3 bulk_update_define_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales channels Bulk Field Update — Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_sales_channels',
    "version": '2.0.0',
    "display_name": 'Define sales channels Bulk Field Update',
    "description": 'Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f3a77d154bcb18e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-channels'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-define-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateDefineSalesChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineSalesChannels'
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
    print(BulkUpdateDefineSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
