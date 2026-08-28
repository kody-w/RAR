---
name: "rar-cowork-cookbook-report-develop-supplier-segments"
description: "Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_supplier_segments", "rar_sha256": "eb94c034f8b27e77c37de0219da5338a32141909618bdf1d22dbb522910f2070", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_supplier_segments`. The original RAPP
agent is preserved byte-for-byte in `report_develop_supplier_segments_agent.py` and in the RCI capsule.

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

Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 eb94c034f8b27e77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_supplier_segments_agent.py` first:

```bash
python3 report_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_supplier_segments_agent.py   # or on stdin
python3 report_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Summary Report — Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_supplier_segments',
    "version": '2.0.0',
    "display_name": 'Develop supplier segments Summary Report',
    "description": 'Builds a structured summary report of develop supplier segments activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c0a665999e95fbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopSupplierSegments(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSupplierSegments'
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
    print(ReportDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
