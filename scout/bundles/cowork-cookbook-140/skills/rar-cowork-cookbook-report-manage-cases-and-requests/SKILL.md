---
name: "rar-cowork-cookbook-report-manage-cases-and-requests"
description: "Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_cases_and_requests", "rar_sha256": "5aa28caa3e558d1d6b862b6367e76bac478e2d3b9c01824a1aaa47248a9782b8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 5aa28caa3e558d1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_cases_and_requests_agent.py` first:

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
    "version": '2.0.1',
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
