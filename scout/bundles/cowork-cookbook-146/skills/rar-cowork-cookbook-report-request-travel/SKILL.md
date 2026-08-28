---
name: "rar-cowork-cookbook-report-request-travel"
description: "Builds a structured summary report of request travel activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_request_travel", "rar_sha256": "d1ccef37bb6fa934731647c78e8b154718ba1508872cc9ad9aecdbb91ce5941d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_request_travel`. The original RAPP
agent is preserved byte-for-byte in `report_request_travel_agent.py` and in the RCI capsule.

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

Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_request_travel_agent.py` and embedded as the fenced Python below (sha256 d1ccef37bb6fa934…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_request_travel_agent.py` first:

```bash
python3 report_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_request_travel_agent.py   # or on stdin
python3 report_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_request_travel',
    "version": '2.0.0',
    "display_name": 'Request travel Summary Report',
    "description": 'Builds a structured summary report of request travel activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '588ed0b9f5b8fff5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRequestTravel(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRequestTravel'
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
    print(ReportRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
