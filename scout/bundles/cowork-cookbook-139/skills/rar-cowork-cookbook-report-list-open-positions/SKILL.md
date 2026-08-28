---
name: "rar-cowork-cookbook-report-list-open-positions"
description: "Builds a structured summary report of list open positions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_list_open_positions", "rar_sha256": "f51ffea5849c62b99564e4d3114ddff7404e42ca166c84e449b93a61bc186111", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 f51ffea5849c62b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_list_open_positions_agent.py` first:

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
    "version": '2.0.0',
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
