---
name: "rar-cowork-cookbook-report-define-service-workflows"
description: "Builds a structured summary report of define service workflows activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_service_workflows", "rar_sha256": "726cabbcbef9e7f7775d3c525e08191415955e7d3b3ded181088ba26455c5728", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_service_workflows_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-service-workflows:8d6e0c38d7c2507cfefdc2832794a53153047b5d2d2e270aa6a678122ab84f39", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_service_workflows`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_service_workflows_agent.py` is
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
