---
name: "rar-cowork-cookbook-report-implement-new-features"
description: "Builds a structured summary report of implement new features activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_new_features", "rar_sha256": "249c4b11e8b7f047c9592698490c5021d40be784fc44730c91e20a26ab97af99", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_implement_new_features`. The original RAPP
agent is preserved byte-for-byte in `report_implement_new_features_agent.py` and in the RCI capsule.

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

Implement new features Summary Report — Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 249c4b11e8b7f047…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_new_features_agent.py` first:

```bash
python3 report_implement_new_features_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_implement_new_features_agent.py   # or on stdin
python3 report_implement_new_features_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement new features Summary Report — Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-implement-new-features
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_implement_new_features',
    "version": '2.0.1',
    "display_name": 'Implement new features Summary Report',
    "description": 'Builds a structured summary report of implement new features activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-implement-new-features',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-implement-new-features',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77ae80761843bc09',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/implement-new-features'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-implement-new-features', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportImplementNewFeatures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportImplementNewFeatures'
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
    print(ReportImplementNewFeatures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
