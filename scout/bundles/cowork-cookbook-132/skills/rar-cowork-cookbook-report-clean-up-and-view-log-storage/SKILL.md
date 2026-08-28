---
name: "rar-cowork-cookbook-report-clean-up-and-view-log-storage"
description: "Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_clean_up_and_view_log_storage", "rar_sha256": "e955fe703f1d4c5e40fd8e400b788414d829fa3de9cc99396f477640e4a9b2ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 e955fe703f1d4c5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_clean_up_and_view_log_storage_agent.py` first:

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
    "version": '2.0.0',
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
