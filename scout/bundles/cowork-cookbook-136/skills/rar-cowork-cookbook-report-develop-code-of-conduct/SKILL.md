---
name: "rar-cowork-cookbook-report-develop-code-of-conduct"
description: "Builds a structured summary report of develop code of conduct activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_code_of_conduct", "rar_sha256": "0ee25bca302c185db4042bb83be1dadcac97272362e97c1f3d062378960c613a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_code_of_conduct_agent.py` and embedded as the fenced Python below (sha256 0ee25bca302c185d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_code_of_conduct_agent.py` first:

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
    "version": '2.0.1',
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
