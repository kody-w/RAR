---
name: "rar-cowork-cookbook-report-conduct-training"
description: "Builds a structured summary report of conduct training activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_training", "rar_sha256": "05438fa6ef208fcaf1c75518eff0b82dd4b53aa29498f2db693c1f06bd69ff2a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_training`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_training_agent.py` and in the RCI capsule.

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

Conduct training Summary Report — Builds a structured summary report of conduct training activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-training
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_training_agent.py` and embedded as the fenced Python below (sha256 05438fa6ef208fca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_training_agent.py` first:

```bash
python3 report_conduct_training_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_training_agent.py   # or on stdin
python3 report_conduct_training_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct training Summary Report — Builds a structured summary report of conduct training activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-training
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_training',
    "version": '2.0.1',
    "display_name": 'Conduct training Summary Report',
    "description": 'Builds a structured summary report of conduct training activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-conduct-training',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-training',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b29d5b2b6664b4fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/conduct-training'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-training', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportConductTraining(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductTraining'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportConductTraining().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
