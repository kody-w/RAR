---
name: "rar-cowork-cookbook-report-onboard-new-contractors"
description: "Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_onboard_new_contractors", "rar_sha256": "31548e71fc2af7a8648c8a32325a2cd14a52408abade0324e47faaf36c07c747", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_onboard_new_contractors`. The original RAPP
agent is preserved byte-for-byte in `report_onboard_new_contractors_agent.py` and in the RCI capsule.

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
