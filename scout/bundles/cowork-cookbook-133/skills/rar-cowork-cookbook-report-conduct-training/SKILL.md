---
name: "rar-cowork-cookbook-report-conduct-training"
description: "Builds a structured summary report of conduct training activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_training", "rar_sha256": "a62d732e0fc6593433560c16a707c353bc000cb01ea723e94827410f0e7a870a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_training_agent.py` and embedded as the fenced Python below (sha256 a62d732e0fc65934…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_training_agent.py` first:

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
    "version": '2.0.0',
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
