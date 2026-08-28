---
name: "rar-cowork-cookbook-audit-configure-and-manage-offline-mode-for-apps"
description: "Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps", "rar_sha256": "6b95fe6280296cb3b470f98a81a38d412da37089aeb6714b8a73842368aa6431", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_offline_mode_for_apps_agent.py` and embedded as the fenced Python below (sha256 6b95fe6280296cb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_offline_mode_for_apps_agent.py` first:

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
    "version": '2.0.0',
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
