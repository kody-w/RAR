---
name: "rar-cowork-cookbook-report-conduct-training"
description: "Builds a structured summary report of conduct training activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_training", "rar_sha256": "a62d732e0fc6593433560c16a707c353bc000cb01ea723e94827410f0e7a870a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_conduct_training_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-conduct-training:add367934bbbae854329ea8e4ca2b52aea19a40ab07218ab9a7c650938bc0850", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_conduct_training`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_conduct_training_agent.py` is
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
