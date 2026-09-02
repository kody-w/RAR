---
name: "rar-cowork-cookbook-audit-document-safety-protocols"
description: "Audits document safety protocols records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_document_safety_protocols", "rar_sha256": "cf33b25ab9808a54cd17278af3e668cfe9ce074035d3a10137c33dbb6619f5d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_document_safety_protocols_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-document-safety-protocols:5243d49ed7a9011abffa5c739c93a0c9fde266387cce79aa1c58c3a4123373de", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_document_safety_protocols`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_document_safety_protocols_agent.py` is
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

Document safety protocols Completeness Audit — Audits document safety protocols records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-document-safety-protocols
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 cf33b25ab9808a54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_document_safety_protocols_agent.py` first:

```bash
python3 audit_document_safety_protocols_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_document_safety_protocols_agent.py   # or on stdin
python3 audit_document_safety_protocols_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document safety protocols Completeness Audit — Audits document safety protocols records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-document-safety-protocols
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_document_safety_protocols',
    "version": '2.0.0',
    "display_name": 'Document safety protocols Completeness Audit',
    "description": 'Audits document safety protocols records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-document-safety-protocols',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-document-safety-protocols',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21e96ede907225da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/document-safety-protocols'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-document-safety-protocols', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDocumentSafetyProtocols(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDocumentSafetyProtocols'
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
    print(AuditDocumentSafetyProtocols().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
