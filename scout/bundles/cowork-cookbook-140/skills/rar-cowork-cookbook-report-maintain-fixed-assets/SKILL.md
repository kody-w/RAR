---
name: "rar-cowork-cookbook-report-maintain-fixed-assets"
description: "Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_fixed_assets", "rar_sha256": "60af6f74fecdcb54dee790166f72daba803a2c3935f8490f08388ff3479c230c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 60af6f74fecdcb54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_fixed_assets_agent.py` first:

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
    "version": '2.0.1',
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
