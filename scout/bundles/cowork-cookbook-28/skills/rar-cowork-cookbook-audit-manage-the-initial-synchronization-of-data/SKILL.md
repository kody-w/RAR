---
name: "rar-cowork-cookbook-audit-manage-the-initial-synchronization-of-data"
description: "Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_the_initial_synchronization_of_data", "rar_sha256": "7c0aaffbc088825cc683ef111fce3f6cb26c8ea3c6ac8f6ab3f060d700b32bc3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_manage_the_initial_synchronization_of_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-manage-the-initial-synchronization-of-data:03b23d3a0467892b06e894aed1bed28859dcab1a94286c9d5c743e0da8fba430", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_manage_the_initial_synchronization_of_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_manage_the_initial_synchronization_of_data_agent.py` is
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

Manage the initial synchronization of data Completeness Audit — Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 7c0aaffbc088825c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 audit_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 audit_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Completeness Audit — Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_the_initial_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the initial synchronization of data Completeness Audit',
    "description": 'Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14a85acfb27fdc76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditManageTheInitialSynchronizationOfData(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageTheInitialSynchronizationOfData'
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
    print(AuditManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
