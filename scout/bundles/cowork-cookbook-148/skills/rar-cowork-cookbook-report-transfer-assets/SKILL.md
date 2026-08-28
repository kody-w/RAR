---
name: "rar-cowork-cookbook-report-transfer-assets"
description: "Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_transfer_assets", "rar_sha256": "e7c8d163c1f364e961ab1ebc7aaa6ff8b1b2e613e0213a3c187784ff7c0e0369", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_transfer_assets_agent.py` and embedded as the fenced Python below (sha256 e7c8d163c1f364e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_transfer_assets_agent.py` first:

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
    "version": '2.0.1',
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
