---
name: "rar-cowork-cookbook-bulk-update-analyze-revenue"
description: "Applies a bulk field update across analyze revenue records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_revenue", "rar_sha256": "a8b60b46c68ed73669cf7cf269390d90439806121877b934821f66aa1ee14edb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-revenue:fb9bf65790c38987f44fcc9ec6422b6b6c282609d630216cae1c94bf2370ef33", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_revenue_agent.py` is
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
