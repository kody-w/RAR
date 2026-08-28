---
name: "rar-cowork-cookbook-report-manage-open-purchases"
description: "Builds a structured summary report of manage open purchases activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_open_purchases", "rar_sha256": "b6767337ce28f5d2fcec2a0b9d0c63031cf22f1bbc3159e0e3cb9af8f9aaf3da", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 b6767337ce28f5d2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_open_purchases_agent.py` first:

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
    "version": '2.0.1',
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
