---
name: "rar-cowork-cookbook-audit-manage-data"
description: "Audits manage data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_data", "rar_sha256": "772b66dc2d7cc3739143cad0090e1cd76556b7e48a9ac23e38761b2266bd075a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_data`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_data_agent.py` and in the RCI capsule.

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

Manage data Completeness Audit — Audits manage data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_data_agent.py` and embedded as the fenced Python below (sha256 772b66dc2d7cc373…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_data_agent.py` first:

```bash
python3 audit_manage_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_data_agent.py   # or on stdin
python3 audit_manage_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data Completeness Audit — Audits manage data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_data',
    "version": '2.0.1',
    "display_name": 'Manage data Completeness Audit',
    "description": 'Audits manage data records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b35930572ce8a61a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/manage-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageData(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageData'
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
    print(AuditManageData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
