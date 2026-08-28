---
name: "rar-cowork-cookbook-bulk-update-collect-interest"
description: "Applies a bulk field update across collect interest records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_collect_interest", "rar_sha256": "6be325c321c4dd92f5d7f08ca487bcb444882062c47f38bac34f7a593874e7e1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_collect_interest_agent.py` and embedded as the fenced Python below (sha256 6be325c321c4dd92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_collect_interest_agent.py` first:

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
    "version": '2.0.1',
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
