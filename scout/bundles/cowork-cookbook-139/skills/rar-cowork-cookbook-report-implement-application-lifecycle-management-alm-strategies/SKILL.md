---
name: "rar-cowork-cookbook-report-implement-application-lifecycle-management-alm-strategies"
description: "Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "3c49031ef6ed42b34b27217f94a62c6c32eb1d16854d9f834bb6bb0ef5000dd1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_implement_application_lifecycle_management_alm_strategies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-implement-application-lifecycle-management-alm-strategies:f3a605a3505c71bd022ea134e88970739e188b111a7dd8d63b02a19aa4ceabb0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_implement_application_lifecycle_management_alm_strategies_agent.py` is
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

Implement application lifecycle management (ALM) strategies Summary Report — Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 3c49031ef6ed42b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_application_lifecycle_management_alm_strategies_agent.py` first:

```bash
python3 report_implement_application_lifecycle_management_alm_strategies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_implement_application_lifecycle_management_alm_strategies_agent.py   # or on stdin
python3 report_implement_application_lifecycle_management_alm_strategies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement application lifecycle management (ALM) strategies Summary Report — Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies',
    "version": '2.0.0',
    "display_name": 'Implement application lifecycle management (ALM) strategies Summary Report',
    "description": 'Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-implement-application-lifecycle-management-alm-strategies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-implement-application-lifecycle-management-alm-strategies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5249fb2ab6fe0830',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/implement-application-lifecycle-management-alm-strategies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-implement-application-lifecycle-management-alm-strategies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportImplementApplicationLifecycleManagementAlmStrategies(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportImplementApplicationLifecycleManagementAlmStrategies'
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
    print(ReportImplementApplicationLifecycleManagementAlmStrategies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
