---
name: "rar-cowork-cookbook-report-audit-workplace-for-safety"
description: "Builds a structured summary report of audit workplace for safety activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_audit_workplace_for_safety", "rar_sha256": "9041c2b1c4d12f859e356c6e72d07f080bf6453955067b414959c21b137c9268", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_audit_workplace_for_safety_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-audit-workplace-for-safety:a9247bcd140554c1591d47c12f82d03986688d424a2562b43971cd4bb2ee9d37", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_audit_workplace_for_safety`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_audit_workplace_for_safety_agent.py` is
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
