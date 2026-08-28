---
name: "rar-cowork-cookbook-audit-manage-the-initial-synchronization-of-data"
description: "Audits manage the initial synchronization of data records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_the_initial_synchronization_of_data", "rar_sha256": "bd2f8b89ec2513e774fe12533f81a496f96c8d0df4740c5025df1d33f9700b7e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 bd2f8b89ec2513e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_the_initial_synchronization_of_data_agent.py` first:

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
    "version": '2.0.1',
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
