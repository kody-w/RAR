---
name: "rar-cowork-cookbook-audit-refine-the-training-program"
description: "Audits refine the training program records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_refine_the_training_program", "rar_sha256": "2cf346d2642b6ee5d09dcd862f5e2ed27525d9f0569908026048ee13212f04f3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_refine_the_training_program`. The original RAPP
agent is preserved byte-for-byte in `audit_refine_the_training_program_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 2cf346d2642b6ee5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_refine_the_training_program_agent.py` first:

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
    "version": '2.0.1',
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
