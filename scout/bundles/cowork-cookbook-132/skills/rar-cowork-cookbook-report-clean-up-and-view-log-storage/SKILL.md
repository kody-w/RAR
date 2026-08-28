---
name: "rar-cowork-cookbook-report-clean-up-and-view-log-storage"
description: "Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_clean_up_and_view_log_storage", "rar_sha256": "ffdeb326be8a9a71e8a3096a625ea77003862555d40a869d335af1cee64d7050", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_clean_up_and_view_log_storage`. The original RAPP
agent is preserved byte-for-byte in `report_clean_up_and_view_log_storage_agent.py` and in the RCI capsule.

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

Clean up and view log storage Summary Report — Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 ffdeb326be8a9a71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_clean_up_and_view_log_storage_agent.py` first:

```bash
python3 report_clean_up_and_view_log_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_clean_up_and_view_log_storage_agent.py   # or on stdin
python3 report_clean_up_and_view_log_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and view log storage Summary Report — Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_clean_up_and_view_log_storage',
    "version": '2.0.1',
    "display_name": 'Clean up and view log storage Summary Report',
    "description": 'Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-clean-up-and-view-log-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-clean-up-and-view-log-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ff76faecf7e378cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/clean-up-and-view-log-storage'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-clean-up-and-view-log-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCleanUpAndViewLogStorage(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCleanUpAndViewLogStorage'
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
    print(ReportCleanUpAndViewLogStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
