---
name: "rar-cowork-cookbook-audit-insure-assets"
description: "Audits insure assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_insure_assets", "rar_sha256": "27018a2610fcc6d3c6ef950ecc82e59653083c113a65236050bc08ec23dd4390", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_insure_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-insure-assets:9f94019152fb813d3f34524e46fd1b0ce5d5681560408868b8d9aca92bfcacd5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_insure_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_insure_assets_agent.py` is
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

Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_insure_assets_agent.py` and embedded as the fenced Python below (sha256 27018a2610fcc6d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_insure_assets_agent.py` first:

```bash
python3 audit_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_insure_assets_agent.py   # or on stdin
python3 audit_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_insure_assets',
    "version": '2.0.0',
    "display_name": 'Insure assets Completeness Audit',
    "description": 'Audits insure assets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05d7a5efc476e910',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditInsureAssets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInsureAssets'
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
    print(AuditInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
