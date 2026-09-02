---
name: "rar-cowork-cookbook-report-transfer-assets"
description: "Builds a structured summary report of transfer assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_transfer_assets", "rar_sha256": "794f2828eba0e5def121dd61251d7ced483d773a3b7a13c09d1a5d4ea211172b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_transfer_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-transfer-assets:ab9be87a38d34657cbaeab94524894dc769cb72d7582b6a0cf67300828b3a153", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_transfer_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_transfer_assets_agent.py` is
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
