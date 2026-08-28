---
name: "rar-cowork-cookbook-bulk-update-recognize-revenue"
description: "Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_recognize_revenue", "rar_sha256": "3ab183e591defcb3345ecb611f98a3f46c3ad7950c106fc6610397109eaff98d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_recognize_revenue`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_recognize_revenue_agent.py` and in the RCI capsule.

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

Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_recognize_revenue_agent.py` and embedded as the fenced Python below (sha256 3ab183e591defcb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_recognize_revenue_agent.py` first:

```bash
python3 bulk_update_recognize_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_recognize_revenue_agent.py   # or on stdin
python3 bulk_update_recognize_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize revenue Bulk Field Update — Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-recognize-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_recognize_revenue',
    "version": '2.0.0',
    "display_name": 'Recognize revenue Bulk Field Update',
    "description": 'Applies a bulk field update across recognize revenue records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-recognize-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-recognize-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a05d801d8a420018',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/recognize-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-recognize-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateRecognizeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecognizeRevenue'
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
    print(BulkUpdateRecognizeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
