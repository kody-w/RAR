---
name: "rar-cowork-cookbook-audit-configure-and-manage-file-storage"
description: "Audits configure and manage file storage records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_file_storage", "rar_sha256": "0d2f89920110023bf7e9b77fe6a5315d468389f5a1b82fe1b059e58415801a37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_configure_and_manage_file_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-configure-and-manage-file-storage:57b873c19b8f7a05a86805cf951ebca97d2b8afa3092208f94b06fd67f3de4f8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_configure_and_manage_file_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_configure_and_manage_file_storage_agent.py` is
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
