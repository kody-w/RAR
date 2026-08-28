---
name: "rar-cowork-cookbook-report-furlough-workers"
description: "Builds a structured summary report of furlough workers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_furlough_workers", "rar_sha256": "fd01a35c56dc7fd97167a392b244f108ff3b546266da8c4e82c7ae50d443fade", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 fd01a35c56dc7fd9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_furlough_workers_agent.py` first:

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
    "version": '2.0.0',
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
