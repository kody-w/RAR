---
name: "rar-cowork-cookbook-audit-manage-and-implement-encryption"
description: "Audits manage and implement encryption records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_and_implement_encryption", "rar_sha256": "8abff1da2b2c737be4b767d3af4780d8a873ad40d814c603ccaf3dfb037bac35", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_and_implement_encryption_agent.py` and embedded as the fenced Python below (sha256 8abff1da2b2c737b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_and_implement_encryption_agent.py` first:

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
    "version": '2.0.1',
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
