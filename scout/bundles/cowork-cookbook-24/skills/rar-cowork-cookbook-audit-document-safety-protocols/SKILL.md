---
name: "rar-cowork-cookbook-audit-document-safety-protocols"
description: "Audits document safety protocols records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_document_safety_protocols", "rar_sha256": "cf33b25ab9808a54cd17278af3e668cfe9ce074035d3a10137c33dbb6619f5d3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_document_safety_protocols`. The original RAPP
agent is preserved byte-for-byte in `audit_document_safety_protocols_agent.py` and in the RCI capsule.

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
