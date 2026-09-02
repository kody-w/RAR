---
name: "rar-cowork-cookbook-production-variance-report"
description: "Compares standard cost to actual cost on completed production orders and highlights material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/production_variance_report", "rar_sha256": "2608c77af910a6353458aadc7ea9c074add4ef0631528c2e3569da734bc4a75e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "production_variance_report_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/production-variance-report:f25fe384da6f4fbc116816ab938a300cddcedd1a680805a115c2a56861b1ce0d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/production_variance_report`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `production_variance_report_agent.py` is
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
