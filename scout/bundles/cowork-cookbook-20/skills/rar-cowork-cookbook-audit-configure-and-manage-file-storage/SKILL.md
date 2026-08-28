---
name: "rar-cowork-cookbook-audit-configure-and-manage-file-storage"
description: "Audits configure and manage file storage records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_file_storage", "rar_sha256": "414199c91c256f65a4c6b6552367efc3566d148f8c70878a99e846264e332649", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_file_storage`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_file_storage_agent.py` and in the RCI capsule.

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

Configure and manage file storage Completeness Audit — Audits configure and manage file storage records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 414199c91c256f65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_file_storage_agent.py` first:

```bash
python3 audit_configure_and_manage_file_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_file_storage_agent.py   # or on stdin
python3 audit_configure_and_manage_file_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage file storage Completeness Audit — Audits configure and manage file storage records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_file_storage',
    "version": '2.0.1',
    "display_name": 'Configure and manage file storage Completeness Audit',
    "description": 'Audits configure and manage file storage records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-configure-and-manage-file-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-file-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36d71ae6492a2c3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/configure-and-manage-file-storage'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-file-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndManageFileStorage(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageFileStorage'
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
    print(AuditConfigureAndManageFileStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
