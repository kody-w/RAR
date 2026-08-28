---
name: "rar-cowork-cookbook-report-manage-active-suppliers"
description: "Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_suppliers", "rar_sha256": "bf1c5560ede53e0d13f28e11334479a0bf0cab5285f1bf8cc718d785a70b753b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 bf1c5560ede53e0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_suppliers_agent.py` first:

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
    "version": '2.0.0',
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
