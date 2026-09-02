---
name: "rar-cowork-cookbook-report-take-inventory-on-software-licenses"
description: "Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_take_inventory_on_software_licenses", "rar_sha256": "1fc5d2adb8440621c6186df385c3a3236632619c56132286925da154a7420d5d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_take_inventory_on_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-take-inventory-on-software-licenses:e7297c2104969171e68b19fea26aee91fd1b3b5f4b29d58e8649efb846871f5c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_take_inventory_on_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_take_inventory_on_software_licenses_agent.py` is
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

Take inventory on software licenses Summary Report — Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 1fc5d2adb8440621…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 report_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 report_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Summary Report — Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_take_inventory_on_software_licenses',
    "version": '2.0.0',
    "display_name": 'Take inventory on software licenses Summary Report',
    "description": 'Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0448ed59a2a33328',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTakeInventoryOnSoftwareLicenses'
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
    print(ReportTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
