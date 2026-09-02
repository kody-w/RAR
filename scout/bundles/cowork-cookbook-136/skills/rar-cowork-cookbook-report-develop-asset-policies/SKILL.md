---
name: "rar-cowork-cookbook-report-develop-asset-policies"
description: "Builds a structured summary report of develop asset policies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_asset_policies", "rar_sha256": "585d35d7f5bd21101e0a459a26dd4e6ffb96521d4ffdb3dce59704258df2bd78", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_asset_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-asset-policies:5155165be749c1519805e5dbac8a0e84ec0577259cd8718c07b35e0828900a53", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_asset_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_asset_policies_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
