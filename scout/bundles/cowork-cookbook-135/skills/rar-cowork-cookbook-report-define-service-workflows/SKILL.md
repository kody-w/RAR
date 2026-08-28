---
name: "rar-cowork-cookbook-report-define-service-workflows"
description: "Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_service_workflows", "rar_sha256": "8855cab921ada40891ea5fad08cfce5e1d1e94f1cb3fb663bc80ddb5abed8353", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_service_workflows_agent.py` and embedded as the fenced Python below (sha256 8855cab921ada408…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_service_workflows_agent.py` first:

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
    "version": '2.0.1',
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
