---
name: "rar-cowork-cookbook-bulk-update-analyze-revenue"
description: "Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_revenue", "rar_sha256": "a8b60b46c68ed73669cf7cf269390d90439806121877b934821f66aa1ee14edb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_revenue_agent.py` and embedded as the fenced Python below (sha256 a8b60b46c68ed736…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_revenue_agent.py` first:

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
    "version": '2.0.0',
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
