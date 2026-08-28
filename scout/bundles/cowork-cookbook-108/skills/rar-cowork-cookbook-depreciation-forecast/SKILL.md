---
name: "rar-cowork-cookbook-depreciation-forecast"
description: "Forecasts the next 12 months of depreciation expense by asset group and by GL account."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/depreciation_forecast", "rar_sha256": "142a9fcc0006429dff6791ac42021d70a510890f3b71798b20dc67a4f1387be8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/depreciation_forecast`. The original RAPP
agent is preserved byte-for-byte in `depreciation_forecast_agent.py` and in the RCI capsule.

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

Depreciation Forecast (12 months) — Forecasts the next 12 months of depreciation expense by asset group and by GL account.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/depreciation-forecast
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `depreciation_forecast_agent.py` and embedded as the fenced Python below (sha256 142a9fcc0006429d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `depreciation_forecast_agent.py` first:

```bash
python3 depreciation_forecast_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 depreciation_forecast_agent.py   # or on stdin
python3 depreciation_forecast_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciation Forecast (12 months) — Forecasts the next 12 months of depreciation expense by asset group and by GL account.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/depreciation-forecast
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/depreciation_forecast',
    "version": '2.0.0',
    "display_name": 'Depreciation Forecast (12 months)',
    "description": 'Forecasts the next 12 months of depreciation expense by asset group and by GL account.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'depreciation-forecast',
        "upstream_url": 'https://coworkcookbook.com/recipes/depreciation-forecast',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f0a730a4d17f59e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/depreciation-forecast', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DepreciationForecast(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DepreciationForecast'
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
    print(DepreciationForecast().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
