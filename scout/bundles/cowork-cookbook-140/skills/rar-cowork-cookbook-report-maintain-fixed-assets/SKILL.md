---
name: "rar-cowork-cookbook-report-maintain-fixed-assets"
description: "Builds a structured summary report of maintain fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_fixed_assets", "rar_sha256": "da606bf2f0de85712be5d0f4bb0536a11e6f5024f648bb8a5e31575fa63439fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_maintain_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-maintain-fixed-assets:d98ea6d6c8caef354c81a6430c09b7f150aae0df79254a374391f086ce80e6d4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_maintain_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_maintain_fixed_assets_agent.py` is
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
