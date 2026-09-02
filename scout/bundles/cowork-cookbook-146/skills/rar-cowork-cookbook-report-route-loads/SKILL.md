---
name: "rar-cowork-cookbook-report-route-loads"
description: "Builds a structured summary report of route loads activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_route_loads", "rar_sha256": "1a6f99532348de5cfd827f1ade3f1b0e4f9942f46af60714da0e5ba498b49312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_route_loads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-route-loads:c743107f8a955e114574475860d76eb80b896cc859821a90275ac267c9540b5b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_route_loads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_route_loads_agent.py` is
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

Route loads Summary Report — Builds a structured summary report of route loads activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_route_loads_agent.py` and embedded as the fenced Python below (sha256 1a6f99532348de5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_route_loads_agent.py` first:

```bash
python3 report_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_route_loads_agent.py   # or on stdin
python3 report_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Summary Report — Builds a structured summary report of route loads activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_route_loads',
    "version": '2.0.0',
    "display_name": 'Route loads Summary Report',
    "description": 'Builds a structured summary report of route loads activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dd14cf61ee848cbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRouteLoads(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRouteLoads'
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
    print(ReportRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
