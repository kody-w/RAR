---
name: "rar-cowork-cookbook-report-renew-software-licenses"
description: "Builds a structured summary report of renew software licenses activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_renew_software_licenses", "rar_sha256": "ccaed08910fb69c86bb9741767eb705dc0f82460a2fbe96dd37c8b8a40752017", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_renew_software_licenses_agent.py` and embedded as the fenced Python below (sha256 ccaed08910fb69c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_renew_software_licenses_agent.py` first:

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
    "version": '2.0.0',
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
