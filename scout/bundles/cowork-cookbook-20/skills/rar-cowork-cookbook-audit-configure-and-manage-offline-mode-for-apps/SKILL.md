---
name: "rar-cowork-cookbook-audit-configure-and-manage-offline-mode-for-apps"
description: "Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps", "rar_sha256": "d91755bf4c0ca30d5ee9b2391597a3a58c37da503389d9c7dfe791a8519f3228", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_offline_mode_for_apps_agent.py` and in the RCI capsule.

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

Configure and manage offline mode for apps Completeness Audit — Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 d91755bf4c0ca30d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_offline_mode_for_apps_agent.py` first:

```bash
python3 audit_configure_and_manage_offline_mode_for_apps_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_offline_mode_for_apps_agent.py   # or on stdin
python3 audit_configure_and_manage_offline_mode_for_apps_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage offline mode for apps Completeness Audit — Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps',
    "version": '2.0.1',
    "display_name": 'Configure and manage offline mode for apps Completeness Audit',
    "description": 'Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-configure-and-manage-offline-mode-for-apps',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-offline-mode-for-apps',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40b4c8933d1d2ffb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-offline-mode-for-apps'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-offline-mode-for-apps', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndManageOfflineModeForApps(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageOfflineModeForApps'
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
    print(AuditConfigureAndManageOfflineModeForApps().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
