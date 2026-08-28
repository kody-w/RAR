---
name: "rar-cowork-cookbook-report-list-open-positions"
description: "Builds a structured summary report of list open positions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_list_open_positions", "rar_sha256": "f377591283af517fb75fee439e6220c7993e7a97cafc0d971206b64571d572db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_list_open_positions`. The original RAPP
agent is preserved byte-for-byte in `report_list_open_positions_agent.py` and in the RCI capsule.

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

List open positions Summary Report — Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 f377591283af517f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_list_open_positions_agent.py` first:

```bash
python3 report_list_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_list_open_positions_agent.py   # or on stdin
python3 report_list_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
List open positions Summary Report — Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_list_open_positions',
    "version": '2.0.1',
    "display_name": 'List open positions Summary Report',
    "description": 'Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-list-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-list-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32ea5259d6f85cb8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/list-open-positions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-list-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportListOpenPositions(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportListOpenPositions'
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
    print(ReportListOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
