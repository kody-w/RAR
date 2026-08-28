---
name: "rar-cowork-cookbook-report-develop-asset-policies"
description: "Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_asset_policies", "rar_sha256": "585d35d7f5bd21101e0a459a26dd4e6ffb96521d4ffdb3dce59704258df2bd78", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 585d35d7f5bd2110…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_asset_policies_agent.py` first:

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
    "version": '2.0.0',
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
