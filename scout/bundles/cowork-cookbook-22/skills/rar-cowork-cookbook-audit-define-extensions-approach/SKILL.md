---
name: "rar-cowork-cookbook-audit-define-extensions-approach"
description: "Audits define extensions approach records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_extensions_approach", "rar_sha256": "56f4e2845aedd5e9e1919e3003d934194835b06350124ec4e733674ccb2a0446", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_extensions_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-extensions-approach:f9495e606a5cbaf1b0a21288b8cc82b9a14acec12592969fd8a61637821aacd7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_extensions_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_extensions_approach_agent.py` is
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

Define extensions approach Completeness Audit — Audits define extensions approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_extensions_approach_agent.py` and embedded as the fenced Python below (sha256 56f4e2845aedd5e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_extensions_approach_agent.py` first:

```bash
python3 audit_define_extensions_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_extensions_approach_agent.py   # or on stdin
python3 audit_define_extensions_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define extensions approach Completeness Audit — Audits define extensions approach records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-extensions-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_extensions_approach',
    "version": '2.0.0',
    "display_name": 'Define extensions approach Completeness Audit',
    "description": 'Audits define extensions approach records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-define-extensions-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-extensions-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4321c07165aa90c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-03', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-extensions-approach'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-define-extensions-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineExtensionsApproach(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineExtensionsApproach'
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
    print(AuditDefineExtensionsApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
