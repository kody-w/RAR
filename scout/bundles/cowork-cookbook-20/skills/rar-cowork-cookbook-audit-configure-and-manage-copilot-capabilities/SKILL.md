---
name: "rar-cowork-cookbook-audit-configure-and-manage-copilot-capabilities"
description: "Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_copilot_capabilities", "rar_sha256": "1d34845046fe8b713c9f78a9c673fc7b3ee0cd109a324b75b9e40baeb6fb4e2e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_copilot_capabilities`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_copilot_capabilities_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_copilot_capabilities_agent.py` and embedded as the fenced Python below (sha256 1d34845046fe8b71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_copilot_capabilities_agent.py` first:

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
    "version": '2.0.1',
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
