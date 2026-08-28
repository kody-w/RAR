---
name: "rar-cowork-cookbook-report-reconcile-freight"
description: "Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_freight", "rar_sha256": "a75c1a862f424628bec4e510e2d64d64516a84d9f1e19e9f0ca49a1ec25ddff3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `report_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Summary Report — Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 a75c1a862f424628…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_freight_agent.py` first:

```bash
python3 report_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_reconcile_freight_agent.py   # or on stdin
python3 report_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Summary Report — Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_reconcile_freight',
    "version": '2.0.1',
    "display_name": 'Reconcile freight Summary Report',
    "description": 'Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9ab726032ba6c7a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportReconcileFreight(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReconcileFreight'
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
    print(ReportReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
