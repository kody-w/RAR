---
name: "rar-cowork-cookbook-report-manage-active-services"
description: "Builds a structured summary report of manage active services activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_services", "rar_sha256": "0b190566f252876029ddd13c22a504b280c8f8d2fa014aef35e451bc8b3da7e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_active_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-active-services:d795bdf642b005a0da3c447ec5bcd68d2aad5c0e74ced7e99aafb61618d73187", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_active_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_active_services_agent.py` is
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
