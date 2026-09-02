---
name: "rar-cowork-cookbook-report-manage-active-suppliers"
description: "Builds a structured summary report of manage active suppliers activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_suppliers", "rar_sha256": "bf1c5560ede53e0d13f28e11334479a0bf0cab5285f1bf8cc718d785a70b753b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_active_suppliers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-active-suppliers:fbe77d48ea7ce801a3793b7d2d0b6a7ebac48cd06974a68deee139da3767dd94", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_active_suppliers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_active_suppliers_agent.py` is
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
