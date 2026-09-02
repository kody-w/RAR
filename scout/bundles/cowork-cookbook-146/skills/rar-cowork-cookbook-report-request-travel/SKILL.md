---
name: "rar-cowork-cookbook-report-request-travel"
description: "Builds a structured summary report of request travel activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_request_travel", "rar_sha256": "d1ccef37bb6fa934731647c78e8b154718ba1508872cc9ad9aecdbb91ce5941d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_request_travel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-request-travel:8f94be1095b6a75c9c89b69f10a539f515ca4ae06db49617d0a19328c2bba830", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_request_travel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_request_travel_agent.py` is
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

Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_request_travel_agent.py` and embedded as the fenced Python below (sha256 d1ccef37bb6fa934…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_request_travel_agent.py` first:

```bash
python3 report_request_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_request_travel_agent.py   # or on stdin
python3 report_request_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Request travel Summary Report — Builds a structured summary report of request travel activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-request-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_request_travel',
    "version": '2.0.0',
    "display_name": 'Request travel Summary Report',
    "description": 'Builds a structured summary report of request travel activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-request-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-request-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '588ed0b9f5b8fff5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/request-travel'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-request-travel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRequestTravel(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRequestTravel'
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
    print(ReportRequestTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
