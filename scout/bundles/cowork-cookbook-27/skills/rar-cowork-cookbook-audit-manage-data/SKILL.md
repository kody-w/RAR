---
name: "rar-cowork-cookbook-audit-manage-data"
description: "Audits manage data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_data", "rar_sha256": "34040db81ec1d1ca5b31ff7b6d0b8ebae4ba245f1255219e7ca7c46c2812af33", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-data:f45596087a2ec586f8a8ba5f43a2b8e4956df4981a09e074783d2702bb7c6d29", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_data_agent.py` is
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
