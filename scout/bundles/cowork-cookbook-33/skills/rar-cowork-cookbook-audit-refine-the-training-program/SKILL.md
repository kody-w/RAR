---
name: "rar-cowork-cookbook-audit-refine-the-training-program"
description: "Audits refine the training program records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_refine_the_training_program", "rar_sha256": "68bfe28ada2505857c1d2a384e4b0a8acaee60567361aebc58bbf145361f3c3a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_refine_the_training_program_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-refine-the-training-program:03e3bd98cc26a8a5748c4f13b5c1c6af5e9b87dbe9997dc0655c1dcb10d2bd72", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_refine_the_training_program`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_refine_the_training_program_agent.py` is
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

Refine the training program Completeness Audit — Audits refine the training program records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-refine-the-training-program
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 68bfe28ada250585…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_refine_the_training_program_agent.py` first:

```bash
python3 audit_refine_the_training_program_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_refine_the_training_program_agent.py   # or on stdin
python3 audit_refine_the_training_program_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Refine the training program Completeness Audit — Audits refine the training program records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-refine-the-training-program
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_refine_the_training_program',
    "version": '2.0.0',
    "display_name": 'Refine the training program Completeness Audit',
    "description": 'Audits refine the training program records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-refine-the-training-program',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-refine-the-training-program',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86111226f7ec20d3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/refine-the-training-program'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-refine-the-training-program', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditRefineTheTrainingProgram(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRefineTheTrainingProgram'
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
    print(AuditRefineTheTrainingProgram().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
