---
name: "rar-cowork-cookbook-report-manage-cases-and-requests"
description: "Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_cases_and_requests", "rar_sha256": "e2bc1997dc51dd571cdc579b5ac4fa9e8eced7e522ab943bfa000bf293fc87e9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_cases_and_requests_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-cases-and-requests:62534077f33c585129bb9a4396c415959cd82080c89c6deab43e6d1826ea3575", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_cases_and_requests`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_cases_and_requests_agent.py` is
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

Manage cases and requests Summary Report — Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 e2bc1997dc51dd57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_cases_and_requests_agent.py` first:

```bash
python3 report_manage_cases_and_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_cases_and_requests_agent.py   # or on stdin
python3 report_manage_cases_and_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage cases and requests Summary Report — Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_cases_and_requests',
    "version": '2.0.0',
    "display_name": 'Manage cases and requests Summary Report',
    "description": 'Builds a structured summary report of manage cases and requests activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-cases-and-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-cases-and-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ad3d6f8ce2303d5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/manage-cases-and-requests'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-manage-cases-and-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageCasesAndRequests(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCasesAndRequests'
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
    print(ReportManageCasesAndRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
