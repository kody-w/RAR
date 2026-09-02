---
name: "rar-cowork-cookbook-report-close-a-case"
description: "Builds a structured summary report of close a case activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_close_a_case", "rar_sha256": "87d9fe26852c77dae6306831960f334e91736996697074243662fd2b0ed5e9ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_close_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-close-a-case:012641a2a454028eb28b1b516dbbcd065d90deb62d44d492083cb799886009cf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_close_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_close_a_case_agent.py` is
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

Close a case Summary Report — Builds a structured summary report of close a case activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_close_a_case_agent.py` and embedded as the fenced Python below (sha256 87d9fe26852c77da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_close_a_case_agent.py` first:

```bash
python3 report_close_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_close_a_case_agent.py   # or on stdin
python3 report_close_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close a case Summary Report — Builds a structured summary report of close a case activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_close_a_case',
    "version": '2.0.0',
    "display_name": 'Close a case Summary Report',
    "description": 'Builds a structured summary report of close a case activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-close-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-close-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f80e0b23edd4e4c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/close-a-case'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-close-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCloseACase(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCloseACase'
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
    print(ReportCloseACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
