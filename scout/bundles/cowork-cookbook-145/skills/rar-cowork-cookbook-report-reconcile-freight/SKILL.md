---
name: "rar-cowork-cookbook-report-reconcile-freight"
description: "Builds a structured summary report of reconcile freight activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_freight", "rar_sha256": "c46341e32572e2974f24c13b6300f63bf5df9b31fd480069785c64149c4cc4a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_reconcile_freight_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-reconcile-freight:a96eb56f9ceed95a39a03c7138f6eb28969cac2155f429ce30cb9f2f2f6578c8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_reconcile_freight`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_reconcile_freight_agent.py` is
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
