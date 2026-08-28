---
name: "rar-cowork-cookbook-report-define-service-workflows"
description: "Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_service_workflows", "rar_sha256": "726cabbcbef9e7f7775d3c525e08191415955e7d3b3ded181088ba26455c5728", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_service_workflows`. The original RAPP
agent is preserved byte-for-byte in `report_define_service_workflows_agent.py` and in the RCI capsule.

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

Define service workflows Summary Report — Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 726cabbcbef9e7f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_service_workflows_agent.py` first:

```bash
python3 report_define_service_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_service_workflows_agent.py   # or on stdin
python3 report_define_service_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service workflows Summary Report — Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-service-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_service_workflows',
    "version": '2.0.0',
    "display_name": 'Define service workflows Summary Report',
    "description": 'Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-service-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-service-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b3c2b5feb23b2547',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-workflows'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-define-service-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDefineServiceWorkflows(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineServiceWorkflows'
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
    print(ReportDefineServiceWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
