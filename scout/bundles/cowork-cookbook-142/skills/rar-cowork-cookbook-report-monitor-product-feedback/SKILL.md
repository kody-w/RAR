---
name: "rar-cowork-cookbook-report-monitor-product-feedback"
description: "Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_product_feedback", "rar_sha256": "54c102f8dcc10972104e7a27add4161ecce313a3feff05965dc1f31b509887bd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_product_feedback`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_product_feedback_agent.py` and in the RCI capsule.

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

Monitor product feedback Summary Report — Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-product-feedback
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 54c102f8dcc10972…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_product_feedback_agent.py` first:

```bash
python3 report_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_product_feedback_agent.py   # or on stdin
python3 report_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Summary Report — Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_product_feedback',
    "version": '2.0.1',
    "display_name": 'Monitor product feedback Summary Report',
    "description": 'Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '18dab3225fe56f69',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportMonitorProductFeedback(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorProductFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
