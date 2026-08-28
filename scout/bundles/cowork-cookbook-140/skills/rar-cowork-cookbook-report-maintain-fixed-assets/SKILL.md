---
name: "rar-cowork-cookbook-report-maintain-fixed-assets"
description: "Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_fixed_assets", "rar_sha256": "da606bf2f0de85712be5d0f4bb0536a11e6f5024f648bb8a5e31575fa63439fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_fixed_assets_agent.py` and in the RCI capsule.

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

Maintain fixed assets Summary Report — Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 da606bf2f0de8571…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_fixed_assets_agent.py` first:

```bash
python3 report_maintain_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_fixed_assets_agent.py   # or on stdin
python3 report_maintain_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain fixed assets Summary Report — Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_fixed_assets',
    "version": '2.0.0',
    "display_name": 'Maintain fixed assets Summary Report',
    "description": 'Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-maintain-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '86418d75d5ed0f4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-maintain-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportMaintainFixedAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainFixedAssets'
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
    print(ReportMaintainFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
