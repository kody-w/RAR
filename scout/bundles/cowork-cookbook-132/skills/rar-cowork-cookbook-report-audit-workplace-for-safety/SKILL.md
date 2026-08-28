---
name: "rar-cowork-cookbook-report-audit-workplace-for-safety"
description: "Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_audit_workplace_for_safety", "rar_sha256": "fac15aae175b9e7d8212aa42a7ef1006b6d6efdb4758d3ae5b008bf6e37392d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_audit_workplace_for_safety`. The original RAPP
agent is preserved byte-for-byte in `report_audit_workplace_for_safety_agent.py` and in the RCI capsule.

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

Audit workplace for safety Summary Report — Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-audit-workplace-for-safety
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 fac15aae175b9e7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_audit_workplace_for_safety_agent.py` first:

```bash
python3 report_audit_workplace_for_safety_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_audit_workplace_for_safety_agent.py   # or on stdin
python3 report_audit_workplace_for_safety_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit workplace for safety Summary Report — Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-audit-workplace-for-safety
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_audit_workplace_for_safety',
    "version": '2.0.1',
    "display_name": 'Audit workplace for safety Summary Report',
    "description": 'Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-audit-workplace-for-safety',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-audit-workplace-for-safety',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dfe2e41e6cf1ec06',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/audit-workplace-for-safety'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-audit-workplace-for-safety', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportAuditWorkplaceForSafety(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAuditWorkplaceForSafety'
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
    print(ReportAuditWorkplaceForSafety().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
