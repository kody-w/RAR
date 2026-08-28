---
name: "rar-cowork-cookbook-audit-document-safety-protocols"
description: "Audits document safety protocols records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_document_safety_protocols", "rar_sha256": "b1db9b1ab9a133aa0f03ee3ac9aad7918b75e166b3dc7d48b11c818795a2858f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_document_safety_protocols_agent.py` and embedded as the fenced Python below (sha256 b1db9b1ab9a133aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_document_safety_protocols_agent.py` first:

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
    "version": '2.0.1',
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
