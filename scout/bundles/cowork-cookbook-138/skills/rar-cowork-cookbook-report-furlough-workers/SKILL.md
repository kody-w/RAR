---
name: "rar-cowork-cookbook-report-furlough-workers"
description: "Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_furlough_workers", "rar_sha256": "29e89f008e07429e846611cd5195d10a1742d1d37bc16a5c4a68322e5c00db71", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_furlough_workers`. The original RAPP
agent is preserved byte-for-byte in `report_furlough_workers_agent.py` and in the RCI capsule.

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

Furlough workers Summary Report — Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 29e89f008e07429e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_furlough_workers_agent.py` first:

```bash
python3 report_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_furlough_workers_agent.py   # or on stdin
python3 report_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Summary Report — Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_furlough_workers',
    "version": '2.0.1',
    "display_name": 'Furlough workers Summary Report',
    "description": 'Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4ba22e8f5dcd0f3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportFurloughWorkers(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportFurloughWorkers'
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
    print(ReportFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
