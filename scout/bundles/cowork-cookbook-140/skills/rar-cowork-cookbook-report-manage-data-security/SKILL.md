---
name: "rar-cowork-cookbook-report-manage-data-security"
description: "Builds a structured summary report of manage data security activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_data_security", "rar_sha256": "ccfded01eb1aae6ad320546c6f35708f94be9a939cb5d0ae3dd3e5e949f37eb4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_data_security_agent.py` and embedded as the fenced Python below (sha256 ccfded01eb1aae6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_data_security_agent.py` first:

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
    "version": '2.0.1',
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
