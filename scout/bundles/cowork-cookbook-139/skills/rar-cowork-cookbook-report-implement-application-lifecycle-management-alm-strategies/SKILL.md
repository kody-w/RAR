---
name: "rar-cowork-cookbook-report-implement-application-lifecycle-management-alm-strategies"
description: "Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "3c49031ef6ed42b34b27217f94a62c6c32eb1d16854d9f834bb6bb0ef5000dd1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies`. The original RAPP
agent is preserved byte-for-byte in `report_implement_application_lifecycle_management_alm_strategies_agent.py` and in the RCI capsule.

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
