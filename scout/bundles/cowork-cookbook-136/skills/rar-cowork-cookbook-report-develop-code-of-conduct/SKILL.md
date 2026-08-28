---
name: "rar-cowork-cookbook-report-develop-code-of-conduct"
description: "Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_code_of_conduct", "rar_sha256": "ef36e18d148ac8a685931d28574f19ee26c6f8d7155d943ab2e1bd0a89c8dfca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_code_of_conduct`. The original RAPP
agent is preserved byte-for-byte in `report_develop_code_of_conduct_agent.py` and in the RCI capsule.

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
