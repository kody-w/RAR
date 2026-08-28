---
name: "rar-cowork-cookbook-report-close-a-case"
description: "Builds a structured summary report of close a case activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_close_a_case", "rar_sha256": "c55e2e8471bd9fab4059936272fcd6a0172ad5b8faa733617390823d94b1d63c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_close_a_case`. The original RAPP
agent is preserved byte-for-byte in `report_close_a_case_agent.py` and in the RCI capsule.

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

Close a case Summary Report — Builds a structured summary report of close a case activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_close_a_case_agent.py` and embedded as the fenced Python below (sha256 c55e2e8471bd9fab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_close_a_case_agent.py` first:

```bash
python3 report_close_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_close_a_case_agent.py   # or on stdin
python3 report_close_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close a case Summary Report — Builds a structured summary report of close a case activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_close_a_case',
    "version": '2.0.1',
    "display_name": 'Close a case Summary Report',
    "description": 'Builds a structured summary report of close a case activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-close-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-close-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f80e0b23edd4e4c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/close-a-case'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-close-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCloseACase(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCloseACase'
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
    print(ReportCloseACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
