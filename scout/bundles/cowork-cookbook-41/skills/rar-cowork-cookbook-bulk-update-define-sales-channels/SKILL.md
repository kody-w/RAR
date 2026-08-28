---
name: "rar-cowork-cookbook-bulk-update-define-sales-channels"
description: "Applies a bulk field update across define sales channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_sales_channels", "rar_sha256": "1c452b85d6fe36f4d431c304758e394fc6e5dd57be505b94ac226e99151d4652", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 1c452b85d6fe36f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_sales_channels_agent.py` first:

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
    "version": '2.0.1',
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
