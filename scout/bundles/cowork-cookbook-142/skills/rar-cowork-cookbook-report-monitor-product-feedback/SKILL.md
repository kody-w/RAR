---
name: "rar-cowork-cookbook-report-monitor-product-feedback"
description: "Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_product_feedback", "rar_sha256": "08ccb5a9295535a3b60d6bd3225205be75c66e7892eae0b6e617ffe45376646e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 08ccb5a9295535a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_product_feedback_agent.py` first:

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
    "version": '2.0.0',
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
