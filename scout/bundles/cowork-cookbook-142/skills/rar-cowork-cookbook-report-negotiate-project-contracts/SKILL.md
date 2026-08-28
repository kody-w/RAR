---
name: "rar-cowork-cookbook-report-negotiate-project-contracts"
description: "Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_negotiate_project_contracts", "rar_sha256": "4b30e64d9e5f438927734e07f9d75ee3740b9f23c3a8adf0a34ad8cf4584abbd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_negotiate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `report_negotiate_project_contracts_agent.py` and in the RCI capsule.

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

Negotiate project contracts Summary Report — Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 4b30e64d9e5f4389…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_negotiate_project_contracts_agent.py` first:

```bash
python3 report_negotiate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_negotiate_project_contracts_agent.py   # or on stdin
python3 report_negotiate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Negotiate project contracts Summary Report — Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-negotiate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_negotiate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Negotiate project contracts Summary Report',
    "description": 'Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-negotiate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-negotiate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f93199aaa6a1405a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/negotiate-project-contracts'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-negotiate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportNegotiateProjectContracts(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportNegotiateProjectContracts'
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
    print(ReportNegotiateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
