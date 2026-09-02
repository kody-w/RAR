---
name: "rar-cowork-cookbook-audit-configure-and-manage-copilot-capabilities"
description: "Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_copilot_capabilities", "rar_sha256": "18b1883e216fc6fbfe310f4d8ef8f4431a08cb4f7704f7d8707ce584510abc1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_configure_and_manage_copilot_capabilities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-configure-and-manage-copilot-capabilities:7d3fea447fb77b788066bb0d32283305c378afd73ec10ecbaa10b3e0ffc7ed23", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_configure_and_manage_copilot_capabilities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_configure_and_manage_copilot_capabilities_agent.py` is
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

Configure and manage copilot capabilities Completeness Audit — Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 18b1883e216fc6fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_copilot_capabilities_agent.py` first:

```bash
python3 audit_configure_and_manage_copilot_capabilities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_copilot_capabilities_agent.py   # or on stdin
python3 audit_configure_and_manage_copilot_capabilities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage copilot capabilities Completeness Audit — Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_copilot_capabilities',
    "version": '2.0.0',
    "display_name": 'Configure and manage copilot capabilities Completeness Audit',
    "description": 'Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-configure-and-manage-copilot-capabilities',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-copilot-capabilities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '38ae10b02046a03b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-copilot-capabilities'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-copilot-capabilities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndManageCopilotCapabilities(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageCopilotCapabilities'
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
    print(AuditConfigureAndManageCopilotCapabilities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
