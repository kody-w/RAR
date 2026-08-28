---
name: "rar-cowork-cookbook-report-develop-asset-policies"
description: "Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_asset_policies", "rar_sha256": "e746c2574f5b98d427de419e39f1657d3318cdf848a7f8e8d80fc9d5f6ff3b53", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `report_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Summary Report — Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-asset-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 e746c2574f5b98d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_asset_policies_agent.py` first:

```bash
python3 report_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_asset_policies_agent.py   # or on stdin
python3 report_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Summary Report — Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_asset_policies',
    "version": '2.0.1',
    "display_name": 'Develop asset policies Summary Report',
    "description": 'Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e3919b4b2bb9198',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportDevelopAssetPolicies(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopAssetPolicies'
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
    print(ReportDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
