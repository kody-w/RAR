---
name: "rar-cowork-cookbook-report-manage-active-services"
description: "Builds a structured summary report of manage active services activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_services", "rar_sha256": "0b190566f252876029ddd13c22a504b280c8f8d2fa014aef35e451bc8b3da7e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 0b190566f2528760…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_services_agent.py` first:

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
    "version": '2.0.0',
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
