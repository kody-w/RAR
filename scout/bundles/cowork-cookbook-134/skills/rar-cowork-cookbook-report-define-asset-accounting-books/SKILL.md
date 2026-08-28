---
name: "rar-cowork-cookbook-report-define-asset-accounting-books"
description: "Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_asset_accounting_books", "rar_sha256": "398eec4ca7cdb47f6ed5e895c2650ad123cf962d4bedd22fb0714f938fb113d9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_asset_accounting_books_agent.py` and embedded as the fenced Python below (sha256 398eec4ca7cdb47f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_asset_accounting_books_agent.py` first:

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
    "version": '2.0.1',
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
