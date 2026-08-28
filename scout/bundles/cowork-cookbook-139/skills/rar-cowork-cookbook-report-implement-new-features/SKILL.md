---
name: "rar-cowork-cookbook-report-implement-new-features"
description: "Builds a structured summary report of implement new features activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_implement_new_features", "rar_sha256": "8ef2387926ab692670d2e286f1ed2c03e231b7b34153e17f172f1ede8cbe3e00", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_implement_new_features_agent.py` and embedded as the fenced Python below (sha256 8ef2387926ab6926…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_implement_new_features_agent.py` first:

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
    "version": '2.0.0',
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
