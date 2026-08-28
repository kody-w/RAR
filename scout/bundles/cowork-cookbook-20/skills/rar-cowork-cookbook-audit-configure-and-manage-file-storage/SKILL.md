---
name: "rar-cowork-cookbook-audit-configure-and-manage-file-storage"
description: "Audits configure and manage file storage records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_file_storage", "rar_sha256": "0d2f89920110023bf7e9b77fe6a5315d468389f5a1b82fe1b059e58415801a37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_file_storage_agent.py` and embedded as the fenced Python below (sha256 0d2f89920110023b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_file_storage_agent.py` first:

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
    "version": '2.0.0',
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
