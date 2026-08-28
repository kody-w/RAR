---
name: "rar-cowork-cookbook-report-manage-data-security"
description: "Builds a structured summary report of manage data security activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_data_security", "rar_sha256": "f7bd1c353fd18ff90776dcd6926188354081d912785fc77bc82c7c638428f885", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_data_security`. The original RAPP
agent is preserved byte-for-byte in `report_manage_data_security_agent.py` and in the RCI capsule.

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

Manage data security Summary Report — Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 f7bd1c353fd18ff9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_data_security_agent.py` first:

```bash
python3 report_manage_data_security_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_data_security_agent.py   # or on stdin
python3 report_manage_data_security_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage data security Summary Report — Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-data-security
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_data_security',
    "version": '2.0.0',
    "display_name": 'Manage data security Summary Report',
    "description": 'Builds a structured summary report of manage data security activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-data-security',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-data-security',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97cb62000c7814d5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/manage-data-security'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-data-security', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageDataSecurity(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageDataSecurity'
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
    print(ReportManageDataSecurity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
