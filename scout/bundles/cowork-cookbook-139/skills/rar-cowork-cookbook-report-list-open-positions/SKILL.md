---
name: "rar-cowork-cookbook-report-list-open-positions"
description: "Builds a structured summary report of list open positions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_list_open_positions", "rar_sha256": "f51ffea5849c62b99564e4d3114ddff7404e42ca166c84e449b93a61bc186111", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_list_open_positions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-list-open-positions:6e9189bddc9ad39cb04a6624d42f99487cf8045fb0b11c3cd2fac79f955b8888", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_list_open_positions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_list_open_positions_agent.py` is
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

List open positions Summary Report — Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_list_open_positions_agent.py` and embedded as the fenced Python below (sha256 f51ffea5849c62b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_list_open_positions_agent.py` first:

```bash
python3 report_list_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_list_open_positions_agent.py   # or on stdin
python3 report_list_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
List open positions Summary Report — Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-list-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_list_open_positions',
    "version": '2.0.0',
    "display_name": 'List open positions Summary Report',
    "description": 'Builds a structured summary report of list open positions activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-list-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-list-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32ea5259d6f85cb8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/list-open-positions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-list-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportListOpenPositions(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportListOpenPositions'
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
    print(ReportListOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
