---
name: "rar-cowork-cookbook-audit-manage-data"
description: "Audits manage data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_data", "rar_sha256": "34040db81ec1d1ca5b31ff7b6d0b8ebae4ba245f1255219e7ca7c46c2812af33", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_data_agent.py` and embedded as the fenced Python below (sha256 34040db81ec1d1ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_data_agent.py` first:

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
    "version": '2.0.0',
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
