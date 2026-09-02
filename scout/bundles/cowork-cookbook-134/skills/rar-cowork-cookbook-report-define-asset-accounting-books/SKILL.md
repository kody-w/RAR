---
name: "rar-cowork-cookbook-report-define-asset-accounting-books"
description: "Builds a structured summary report of define asset accounting books activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_asset_accounting_books", "rar_sha256": "9516572384aa294c4c56587ec31f882739e099138baeb72548dbde15087fd661", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_asset_accounting_books_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-asset-accounting-books:1cc2defa29c16d9b110e96b0683e5ad102bb16e4e0d2bd26a07f6e56778daf2a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_asset_accounting_books`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_asset_accounting_books_agent.py` is
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
