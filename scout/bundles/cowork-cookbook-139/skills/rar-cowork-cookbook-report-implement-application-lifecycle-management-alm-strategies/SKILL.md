---
name: "rar-cowork-cookbook-report-implement-application-lifecycle-management-alm-strategies"
description: "Builds a structured summary report of implement application lifecycle management (ALM) strategies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_application_lifecycle_management_alm_strategies", "rar_sha256": "603ccae32899b79c231c919110d62d9aed4ef06d992a00a34750adfb10813d12", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_application_lifecycle_management_alm_strategies_agent.py` and embedded as the fenced Python below (sha256 603ccae32899b79c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_application_lifecycle_management_alm_strategies_agent.py` first:

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
    "version": '2.0.1',
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
