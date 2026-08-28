---
name: "rar-cowork-cookbook-report-reconcile-freight"
description: "Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_freight", "rar_sha256": "c46341e32572e2974f24c13b6300f63bf5df9b31fd480069785c64149c4cc4a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 c46341e32572e297…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_freight_agent.py` first:

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
    "version": '2.0.0',
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
