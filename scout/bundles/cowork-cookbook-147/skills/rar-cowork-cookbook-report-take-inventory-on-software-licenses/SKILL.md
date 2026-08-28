---
name: "rar-cowork-cookbook-report-take-inventory-on-software-licenses"
description: "Builds a structured summary report of take inventory on software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_take_inventory_on_software_licenses", "rar_sha256": "4901c5dbd7a08679b1885b4ac97af1989e1288f445c54e7216e5ce006179aed0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 4901c5dbd7a08679…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_take_inventory_on_software_licenses_agent.py` first:

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
    "version": '2.0.1',
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
