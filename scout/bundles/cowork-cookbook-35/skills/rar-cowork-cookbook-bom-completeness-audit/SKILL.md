---
name: "rar-cowork-cookbook-bom-completeness-audit"
description: "Audits active BOMs for missing components, expired versions, and items that are obsolete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bom_completeness_audit", "rar_sha256": "1391ef31c56ca86c0f6d4198c1ec90b6cbf7e21b8a9acff91d6223765a9d24e8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bom_completeness_audit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bom-completeness-audit:b1a8226125e402170d3c9b046af5fcc3698a29e34f941193a27a6286f455d159", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bom_completeness_audit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bom_completeness_audit_agent.py` is
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

BOM Completeness Audit — Audits active BOMs for missing components, expired versions, and items that are obsolete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bom_completeness_audit_agent.py` and embedded as the fenced Python below (sha256 1391ef31c56ca86c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bom_completeness_audit_agent.py` first:

```bash
python3 bom_completeness_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bom_completeness_audit_agent.py   # or on stdin
python3 bom_completeness_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
BOM Completeness Audit — Audits active BOMs for missing components, expired versions, and items that are obsolete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bom-completeness-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bom_completeness_audit',
    "version": '2.0.0',
    "display_name": 'BOM Completeness Audit',
    "description": 'Audits active BOMs for missing components, expired versions, and items that are obsolete.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bom-completeness-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/bom-completeness-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6d2f831e34b92f83',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/bom-completeness-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.429, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class BomCompletenessAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BomCompletenessAudit'
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
    print(BomCompletenessAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
