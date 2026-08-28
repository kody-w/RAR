---
name: "rar-cowork-cookbook-audit-configure-and-manage-copilot-capabilities"
description: "Audits configure and manage copilot capabilities records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_copilot_capabilities", "rar_sha256": "18b1883e216fc6fbfe310f4d8ef8f4431a08cb4f7704f7d8707ce584510abc1b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
