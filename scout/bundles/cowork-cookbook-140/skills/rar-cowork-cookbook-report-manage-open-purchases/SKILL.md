---
name: "rar-cowork-cookbook-report-manage-open-purchases"
description: "Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_open_purchases", "rar_sha256": "40954f247e4ebccf6c7716742bc301fa03dc5485fc031ff29b5da72574eedec3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_open_purchases`. The original RAPP
agent is preserved byte-for-byte in `report_manage_open_purchases_agent.py` and in the RCI capsule.

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

Manage open purchases Summary Report — Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 40954f247e4ebccf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_open_purchases_agent.py` first:

```bash
python3 report_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_open_purchases_agent.py   # or on stdin
python3 report_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Summary Report — Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_open_purchases',
    "version": '2.0.0',
    "display_name": 'Manage open purchases Summary Report',
    "description": 'Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3ebb5636d58dd2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageOpenPurchases(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageOpenPurchases'
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
    print(ReportManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
