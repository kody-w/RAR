---
name: "rar-cowork-cookbook-production-variance-report"
description: "Compares standard cost to actual cost on completed production orders and highlights material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/production_variance_report", "rar_sha256": "2608c77af910a6353458aadc7ea9c074add4ef0631528c2e3569da734bc4a75e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/production_variance_report`. The original RAPP
agent is preserved byte-for-byte in `production_variance_report_agent.py` and in the RCI capsule.

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

Production Cost Variance Report — Compares standard cost to actual cost on completed production orders and highlights material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/production-variance-report
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `production_variance_report_agent.py` and embedded as the fenced Python below (sha256 2608c77af910a635…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `production_variance_report_agent.py` first:

```bash
python3 production_variance_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 production_variance_report_agent.py   # or on stdin
python3 production_variance_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Production Cost Variance Report — Compares standard cost to actual cost on completed production orders and highlights material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/production-variance-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/production_variance_report',
    "version": '2.0.0',
    "display_name": 'Production Cost Variance Report',
    "description": 'Compares standard cost to actual cost on completed production orders and highlights material variances.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'production-variance-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/production-variance-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e3d5e2dacfbe420',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/production-variance-report', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ProductionVarianceReport(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductionVarianceReport'
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
    print(ProductionVarianceReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
