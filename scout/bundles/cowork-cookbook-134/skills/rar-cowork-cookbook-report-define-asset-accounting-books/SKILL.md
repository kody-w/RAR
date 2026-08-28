---
name: "rar-cowork-cookbook-report-define-asset-accounting-books"
description: "Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_asset_accounting_books", "rar_sha256": "9516572384aa294c4c56587ec31f882739e099138baeb72548dbde15087fd661", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_asset_accounting_books`. The original RAPP
agent is preserved byte-for-byte in `report_define_asset_accounting_books_agent.py` and in the RCI capsule.

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

Define asset accounting books Summary Report — Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-asset-accounting-books
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 9516572384aa294c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_asset_accounting_books_agent.py` first:

```bash
python3 report_define_asset_accounting_books_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_asset_accounting_books_agent.py   # or on stdin
python3 report_define_asset_accounting_books_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define asset accounting books Summary Report — Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-asset-accounting-books
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_asset_accounting_books',
    "version": '2.0.0',
    "display_name": 'Define asset accounting books Summary Report',
    "description": 'Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-asset-accounting-books',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-asset-accounting-books',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a85f01b99255f671',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-asset-accounting-books'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-define-asset-accounting-books', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDefineAssetAccountingBooks(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineAssetAccountingBooks'
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
    print(ReportDefineAssetAccountingBooks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
