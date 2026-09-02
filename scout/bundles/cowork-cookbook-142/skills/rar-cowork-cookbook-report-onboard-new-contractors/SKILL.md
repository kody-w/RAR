---
name: "rar-cowork-cookbook-report-onboard-new-contractors"
description: "Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_onboard_new_contractors", "rar_sha256": "31548e71fc2af7a8648c8a32325a2cd14a52408abade0324e47faaf36c07c747", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_onboard_new_contractors_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-onboard-new-contractors:d3a0683fbd7792ad9048da3f6bbad4e30be7f7c54d4129438c58b2d0f324536c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_onboard_new_contractors`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_onboard_new_contractors_agent.py` is
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

Onboard new contractors Summary Report — Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 31548e71fc2af7a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_onboard_new_contractors_agent.py` first:

```bash
python3 report_onboard_new_contractors_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_onboard_new_contractors_agent.py   # or on stdin
python3 report_onboard_new_contractors_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new contractors Summary Report — Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-onboard-new-contractors
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_onboard_new_contractors',
    "version": '2.0.0',
    "display_name": 'Onboard new contractors Summary Report',
    "description": 'Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-onboard-new-contractors',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-onboard-new-contractors',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b6deb4cb574b91a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/onboard-new-contractors'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-onboard-new-contractors', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportOnboardNewContractors(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportOnboardNewContractors'
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
    print(ReportOnboardNewContractors().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
