---
name: "rar-cowork-cookbook-production-variance-report"
description: "Compares standard cost to actual cost on completed production orders and highlights material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/production_variance_report", "rar_sha256": "5f124610c88adbdc41d146d211c041bc3cfe9ea647208716c152c67887ef04f9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `production_variance_report_agent.py` and embedded as the fenced Python below (sha256 5f124610c88adbdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `production_variance_report_agent.py` first:

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
    "version": '2.0.1',
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
