---
name: "rar-cowork-cookbook-report-collaborate-on-service-work"
description: "Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_collaborate_on_service_work", "rar_sha256": "4940d893bcb7c93d33dcc053e73bafb979e7c2e67da351512847efda171db445", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_collaborate_on_service_work`. The original RAPP
agent is preserved byte-for-byte in `report_collaborate_on_service_work_agent.py` and in the RCI capsule.

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

Collaborate on service work Summary Report — Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-collaborate-on-service-work
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 4940d893bcb7c93d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_collaborate_on_service_work_agent.py` first:

```bash
python3 report_collaborate_on_service_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_collaborate_on_service_work_agent.py   # or on stdin
python3 report_collaborate_on_service_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collaborate on service work Summary Report — Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-collaborate-on-service-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_collaborate_on_service_work',
    "version": '2.0.1',
    "display_name": 'Collaborate on service work Summary Report',
    "description": 'Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-collaborate-on-service-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-collaborate-on-service-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd44216c2d2c0320c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collaborate-on-service-work'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-collaborate-on-service-work', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCollaborateOnServiceWork(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCollaborateOnServiceWork'
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
    print(ReportCollaborateOnServiceWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
