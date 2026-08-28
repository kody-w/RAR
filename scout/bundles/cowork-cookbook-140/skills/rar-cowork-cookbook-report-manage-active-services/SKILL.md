---
name: "rar-cowork-cookbook-report-manage-active-services"
description: "Builds a structured summary report of manage active services activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_services", "rar_sha256": "17a0987d169bc0afd3a7b677af8e29b72f399f4c540b611e110f3264100fd810", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_active_services`. The original RAPP
agent is preserved byte-for-byte in `report_manage_active_services_agent.py` and in the RCI capsule.

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

Manage active services Summary Report — Builds a structured summary report of manage active services activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 17a0987d169bc0af…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_services_agent.py` first:

```bash
python3 report_manage_active_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_active_services_agent.py   # or on stdin
python3 report_manage_active_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active services Summary Report — Builds a structured summary report of manage active services activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_active_services',
    "version": '2.0.1',
    "display_name": 'Manage active services Summary Report',
    "description": 'Builds a structured summary report of manage active services activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-active-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-active-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ed63127770ae1882',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-active-services'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-manage-active-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageActiveServices(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageActiveServices'
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
    print(ReportManageActiveServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
