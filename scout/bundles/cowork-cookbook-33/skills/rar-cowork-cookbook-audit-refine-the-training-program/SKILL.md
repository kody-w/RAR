---
name: "rar-cowork-cookbook-audit-refine-the-training-program"
description: "Audits refine the training program records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_refine_the_training_program", "rar_sha256": "68bfe28ada2505857c1d2a384e4b0a8acaee60567361aebc58bbf145361f3c3a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
