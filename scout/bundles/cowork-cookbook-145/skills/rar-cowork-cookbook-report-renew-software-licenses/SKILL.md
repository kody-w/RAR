---
name: "rar-cowork-cookbook-report-renew-software-licenses"
description: "Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_renew_software_licenses", "rar_sha256": "2bdac0d983e05ca471324fc8477762f1b788662289bc4803071a555472cb72db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_renew_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `report_renew_software_licenses_agent.py` and in the RCI capsule.

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

Renew software licenses Summary Report — Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2bdac0d983e05ca4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_renew_software_licenses_agent.py` first:

```bash
python3 report_renew_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_renew_software_licenses_agent.py   # or on stdin
python3 report_renew_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Renew software licenses Summary Report — Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-renew-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_renew_software_licenses',
    "version": '2.0.1',
    "display_name": 'Renew software licenses Summary Report',
    "description": 'Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-renew-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-renew-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fdec36c9821cf7fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/renew-software-licenses'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-renew-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRenewSoftwareLicenses(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRenewSoftwareLicenses'
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
    print(ReportRenewSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
