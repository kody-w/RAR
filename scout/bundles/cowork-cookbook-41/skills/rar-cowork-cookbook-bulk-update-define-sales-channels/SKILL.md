---
name: "rar-cowork-cookbook-bulk-update-define-sales-channels"
description: "Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_channels", "rar_sha256": "52ca881f688a3ea5c12062fbbfed390e339ecbb1b92b9c4a16c037b1c6083033", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_sales_channels_agent.py` and in the RCI capsule.

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
