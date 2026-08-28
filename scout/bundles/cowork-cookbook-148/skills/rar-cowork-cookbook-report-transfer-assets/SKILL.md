---
name: "rar-cowork-cookbook-report-transfer-assets"
description: "Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_transfer_assets", "rar_sha256": "794f2828eba0e5def121dd61251d7ced483d773a3b7a13c09d1a5d4ea211172b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_transfer_assets`. The original RAPP
agent is preserved byte-for-byte in `report_transfer_assets_agent.py` and in the RCI capsule.

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

Transfer assets Summary Report — Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-transfer-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 794f2828eba0e5de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_transfer_assets_agent.py` first:

```bash
python3 report_transfer_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_transfer_assets_agent.py   # or on stdin
python3 report_transfer_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer assets Summary Report — Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-transfer-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_transfer_assets',
    "version": '2.0.0',
    "display_name": 'Transfer assets Summary Report',
    "description": 'Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-transfer-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-transfer-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa370a70ab5c0b75',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/transfer-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-transfer-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportTransferAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTransferAssets'
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
    print(ReportTransferAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
