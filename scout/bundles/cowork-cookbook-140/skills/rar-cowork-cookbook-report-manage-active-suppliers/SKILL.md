---
name: "rar-cowork-cookbook-report-manage-active-suppliers"
description: "Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_suppliers", "rar_sha256": "745da2d6224e93dab03d00fe93fdb12208505d7036fc6a4da4abc7be95c228cc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_active_suppliers`. The original RAPP
agent is preserved byte-for-byte in `report_manage_active_suppliers_agent.py` and in the RCI capsule.

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

Manage active suppliers Summary Report — Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-suppliers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 745da2d6224e93da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_suppliers_agent.py` first:

```bash
python3 report_manage_active_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_active_suppliers_agent.py   # or on stdin
python3 report_manage_active_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active suppliers Summary Report — Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_active_suppliers',
    "version": '2.0.1',
    "display_name": 'Manage active suppliers Summary Report',
    "description": 'Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-active-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-active-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4c71a3005198da6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-active-suppliers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-active-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageActiveSuppliers(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageActiveSuppliers'
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
    print(ReportManageActiveSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
