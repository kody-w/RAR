---
name: "rar-cowork-cookbook-audit-manage-and-implement-encryption"
description: "Audits manage and implement encryption records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_and_implement_encryption", "rar_sha256": "6e544ebae7531d73140b606e63e4da68ab79e3382434ce9221eda85e945fbba2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_and_implement_encryption`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_and_implement_encryption_agent.py` and in the RCI capsule.

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

Manage and implement encryption Completeness Audit — Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 6e544ebae7531d73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_and_implement_encryption_agent.py` first:

```bash
python3 audit_manage_and_implement_encryption_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_and_implement_encryption_agent.py   # or on stdin
python3 audit_manage_and_implement_encryption_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage and implement encryption Completeness Audit — Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_and_implement_encryption',
    "version": '2.0.0',
    "display_name": 'Manage and implement encryption Completeness Audit',
    "description": 'Audits manage and implement encryption records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-and-implement-encryption',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-and-implement-encryption',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ce67394e458c4c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-and-implement-encryption'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-and-implement-encryption', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageAndImplementEncryption(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageAndImplementEncryption'
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
    print(AuditManageAndImplementEncryption().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
