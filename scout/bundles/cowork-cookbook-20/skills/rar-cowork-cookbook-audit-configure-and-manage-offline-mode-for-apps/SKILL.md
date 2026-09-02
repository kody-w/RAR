---
name: "rar-cowork-cookbook-audit-configure-and-manage-offline-mode-for-apps"
description: "Audits configure and manage offline mode for apps records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps", "rar_sha256": "6b95fe6280296cb3b470f98a81a38d412da37089aeb6714b8a73842368aa6431", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_configure_and_manage_offline_mode_for_apps_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-configure-and-manage-offline-mode-for-apps:fd7901b11f4a103d4cde92d802173f987b9c8c9da11e4e1817f92f6a717b694b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_configure_and_manage_offline_mode_for_apps`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_configure_and_manage_offline_mode_for_apps_agent.py` is
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
