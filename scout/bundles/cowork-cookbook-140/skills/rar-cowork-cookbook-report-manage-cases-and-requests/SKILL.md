---
name: "rar-cowork-cookbook-report-manage-cases-and-requests"
description: "Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_cases_and_requests", "rar_sha256": "e2bc1997dc51dd571cdc579b5ac4fa9e8eced7e522ab943bfa000bf293fc87e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_cases_and_requests`. The original RAPP
agent is preserved byte-for-byte in `report_manage_cases_and_requests_agent.py` and in the RCI capsule.

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

Manage cases and requests Summary Report — Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 e2bc1997dc51dd57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_cases_and_requests_agent.py` first:

```bash
python3 report_manage_cases_and_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_cases_and_requests_agent.py   # or on stdin
python3 report_manage_cases_and_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage cases and requests Summary Report — Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_cases_and_requests',
    "version": '2.0.0',
    "display_name": 'Manage cases and requests Summary Report',
    "description": 'Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-cases-and-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-cases-and-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad3d6f8ce2303d5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/manage-cases-and-requests'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-manage-cases-and-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageCasesAndRequests(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCasesAndRequests'
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
    print(ReportManageCasesAndRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
