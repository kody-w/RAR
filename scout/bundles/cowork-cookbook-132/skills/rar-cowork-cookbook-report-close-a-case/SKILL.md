---
name: "rar-cowork-cookbook-report-close-a-case"
description: "Builds a structured summary report of close a case activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_close_a_case", "rar_sha256": "87d9fe26852c77dae6306831960f334e91736996697074243662fd2b0ed5e9ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_close_a_case_agent.py` and embedded as the fenced Python below (sha256 87d9fe26852c77da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_close_a_case_agent.py` first:

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
    "version": '2.0.0',
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
