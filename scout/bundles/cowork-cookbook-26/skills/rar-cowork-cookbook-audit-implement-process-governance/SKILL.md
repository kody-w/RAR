---
name: "rar-cowork-cookbook-audit-implement-process-governance"
description: "Audits implement process governance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_implement_process_governance", "rar_sha256": "72854e1589df2791f3600aa40891644d6c3cf287dc71db3dfa36f1a100d90395", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_implement_process_governance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-implement-process-governance:5625a896a0ab8f4ca22516b615abaf903646d4e46ae7d7c4a60a5d8e589c079a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_implement_process_governance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_implement_process_governance_agent.py` is
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

Implement process governance Completeness Audit — Audits implement process governance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_implement_process_governance_agent.py` and embedded as the fenced Python below (sha256 72854e1589df2791…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_implement_process_governance_agent.py` first:

```bash
python3 audit_implement_process_governance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_implement_process_governance_agent.py   # or on stdin
python3 audit_implement_process_governance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement process governance Completeness Audit — Audits implement process governance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-implement-process-governance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_implement_process_governance',
    "version": '2.0.0',
    "display_name": 'Implement process governance Completeness Audit',
    "description": 'Audits implement process governance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-implement-process-governance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-implement-process-governance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a31359a2132581f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-process-governance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-implement-process-governance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditImplementProcessGovernance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditImplementProcessGovernance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditImplementProcessGovernance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
