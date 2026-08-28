---
name: "rar-cowork-cookbook-bulk-update-analyze-revenue"
description: "Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_revenue", "rar_sha256": "a9133ce1c059c01f299bffbef9078a6095febd3c6803772e040ae68b97c14fd3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_analyze_revenue`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_analyze_revenue_agent.py` and in the RCI capsule.

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

Analyze revenue Bulk Field Update — Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 a9133ce1c059c01f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_revenue_agent.py` first:

```bash
python3 bulk_update_analyze_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_revenue_agent.py   # or on stdin
python3 bulk_update_analyze_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze revenue Bulk Field Update — Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_revenue',
    "version": '2.0.1',
    "display_name": 'Analyze revenue Bulk Field Update',
    "description": 'Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-analyze-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '495b04cfb06f3c50',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-revenue'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-analyze-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateAnalyzeRevenue(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeRevenue'
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
    print(BulkUpdateAnalyzeRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
