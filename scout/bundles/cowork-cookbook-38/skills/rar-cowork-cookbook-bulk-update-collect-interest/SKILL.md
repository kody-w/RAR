---
name: "rar-cowork-cookbook-bulk-update-collect-interest"
description: "Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_collect_interest", "rar_sha256": "26cbba41597e4e1a906e61408bf3164d8edc6c38dc59ead91723103a5c58ae91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_collect_interest`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_collect_interest_agent.py` and in the RCI capsule.

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

Collect interest Bulk Field Update — Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_collect_interest_agent.py` and embedded as the fenced Python below (sha256 26cbba41597e4e1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_collect_interest_agent.py` first:

```bash
python3 bulk_update_collect_interest_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_collect_interest_agent.py   # or on stdin
python3 bulk_update_collect_interest_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect interest Bulk Field Update — Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-collect-interest
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_collect_interest',
    "version": '2.0.0',
    "display_name": 'Collect interest Bulk Field Update',
    "description": 'Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-collect-interest',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-collect-interest',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f440add5373570fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/collect-interest'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-collect-interest', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateCollectInterest(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateCollectInterest'
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
    print(BulkUpdateCollectInterest().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
