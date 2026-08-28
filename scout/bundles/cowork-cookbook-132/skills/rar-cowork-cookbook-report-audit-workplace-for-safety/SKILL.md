---
name: "rar-cowork-cookbook-report-audit-workplace-for-safety"
description: "Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_audit_workplace_for_safety", "rar_sha256": "9041c2b1c4d12f859e356c6e72d07f080bf6453955067b414959c21b137c9268", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 9041c2b1c4d12f85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_audit_workplace_for_safety_agent.py` first:

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
    "version": '2.0.0',
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
