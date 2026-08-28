---
name: "rar-cowork-cookbook-report-collaborate-on-service-work"
description: "Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_collaborate_on_service_work", "rar_sha256": "6c50fe61f3db933719968d981157b019a5143234eab2a1f2ec844dbc66281116", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 6c50fe61f3db9337…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_collaborate_on_service_work_agent.py` first:

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
    "version": '2.0.0',
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
