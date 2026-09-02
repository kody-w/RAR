---
name: "rar-cowork-cookbook-report-monitor-product-feedback"
description: "Builds a structured summary report of monitor product feedback activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_product_feedback", "rar_sha256": "08ccb5a9295535a3b60d6bd3225205be75c66e7892eae0b6e617ffe45376646e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_monitor_product_feedback_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-monitor-product-feedback:ff9662c1a0d714e90886b182d9cb00c9a9a2b0689d80a26e4276c5dcb99ed6b4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_monitor_product_feedback`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_monitor_product_feedback_agent.py` is
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
