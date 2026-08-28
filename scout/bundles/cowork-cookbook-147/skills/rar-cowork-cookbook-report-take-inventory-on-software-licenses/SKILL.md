---
name: "rar-cowork-cookbook-report-take-inventory-on-software-licenses"
description: "Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_take_inventory_on_software_licenses", "rar_sha256": "1fc5d2adb8440621c6186df385c3a3236632619c56132286925da154a7420d5d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_take_inventory_on_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `report_take_inventory_on_software_licenses_agent.py` and in the RCI capsule.

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
