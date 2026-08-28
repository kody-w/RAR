---
name: "rar-cowork-cookbook-report-onboard-new-contractors"
description: "Builds a structured summary report of onboard new contractors activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_onboard_new_contractors", "rar_sha256": "8c93f22bcdfe0d176e598a59fc6225590e2f9a8a1b21f6db39b11d25ed92fbd1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_onboard_new_contractors_agent.py` and embedded as the fenced Python below (sha256 8c93f22bcdfe0d17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_onboard_new_contractors_agent.py` first:

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
    "version": '2.0.1',
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
