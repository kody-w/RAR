---
name: "rar-cowork-cookbook-report-govern-projects"
description: "Builds a structured summary report of govern projects activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_govern_projects", "rar_sha256": "9eb84b632b246a3b372b392a203f6cd3783ee6ea7897c90d46d33181a9a48600", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_govern_projects`. The original RAPP
agent is preserved byte-for-byte in `report_govern_projects_agent.py` and in the RCI capsule.

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

Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_govern_projects_agent.py` and embedded as the fenced Python below (sha256 9eb84b632b246a3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_govern_projects_agent.py` first:

```bash
python3 report_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_govern_projects_agent.py   # or on stdin
python3 report_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_govern_projects',
    "version": '2.0.0',
    "display_name": 'Govern projects Summary Report',
    "description": 'Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57acd2619178a5de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportGovernProjects(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportGovernProjects'
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
    print(ReportGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
