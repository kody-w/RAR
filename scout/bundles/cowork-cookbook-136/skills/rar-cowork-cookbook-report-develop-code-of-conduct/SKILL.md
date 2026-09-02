---
name: "rar-cowork-cookbook-report-develop-code-of-conduct"
description: "Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_code_of_conduct", "rar_sha256": "ef36e18d148ac8a685931d28574f19ee26c6f8d7155d943ab2e1bd0a89c8dfca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_code_of_conduct_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-code-of-conduct:f4b7ea1cdb0c88a61086601000da3f88e5eeea401be1be04f77b3c23a3cf6703", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_code_of_conduct`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_code_of_conduct_agent.py` is
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

Develop code of conduct Summary Report — Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-code-of-conduct
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 ef36e18d148ac8a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_code_of_conduct_agent.py` first:

```bash
python3 report_develop_code_of_conduct_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_code_of_conduct_agent.py   # or on stdin
python3 report_develop_code_of_conduct_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop code of conduct Summary Report — Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-code-of-conduct
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_code_of_conduct',
    "version": '2.0.0',
    "display_name": 'Develop code of conduct Summary Report',
    "description": 'Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-code-of-conduct',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-code-of-conduct',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '405c6690fd28560b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/develop-code-of-conduct'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-develop-code-of-conduct', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopCodeOfConduct(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopCodeOfConduct'
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
    print(ReportDevelopCodeOfConduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
