---
name: "rar-cowork-cookbook-report-collaborate-on-service-work"
description: "Builds a structured summary report of collaborate on service work activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_collaborate_on_service_work", "rar_sha256": "6c50fe61f3db933719968d981157b019a5143234eab2a1f2ec844dbc66281116", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_collaborate_on_service_work_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-collaborate-on-service-work:6d9dda27814c8613b0fed2949ebb81d2dda3fd92057cc0f3d7cd18943220e056", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_collaborate_on_service_work`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_collaborate_on_service_work_agent.py` is
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
