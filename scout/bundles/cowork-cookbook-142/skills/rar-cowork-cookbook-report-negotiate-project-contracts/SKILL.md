---
name: "rar-cowork-cookbook-report-negotiate-project-contracts"
description: "Builds a structured summary report of negotiate project contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_negotiate_project_contracts", "rar_sha256": "d9adee62a083d6ed8a8a837db736897006e10a5609562520e37a951153c2a53b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_negotiate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 d9adee62a083d6ed…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_negotiate_project_contracts_agent.py` first:

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
    "version": '2.0.1',
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
