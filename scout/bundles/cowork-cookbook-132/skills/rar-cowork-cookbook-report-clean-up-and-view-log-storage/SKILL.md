---
name: "rar-cowork-cookbook-report-clean-up-and-view-log-storage"
description: "Builds a structured summary report of clean up and view log storage activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_clean_up_and_view_log_storage", "rar_sha256": "e955fe703f1d4c5e40fd8e400b788414d829fa3de9cc99396f477640e4a9b2ca", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_clean_up_and_view_log_storage_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-clean-up-and-view-log-storage:459b7e55fc6c1479f050d53caa342b03ea0c32cc467e3a9a2528e34e5fae6475", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_clean_up_and_view_log_storage`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_clean_up_and_view_log_storage_agent.py` is
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
