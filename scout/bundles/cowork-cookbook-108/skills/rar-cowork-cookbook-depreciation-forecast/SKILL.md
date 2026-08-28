---
name: "rar-cowork-cookbook-depreciation-forecast"
description: "Forecasts the next 12 months of depreciation expense by asset group and by GL account."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/depreciation_forecast", "rar_sha256": "fd371646e8813a1b684fddd900489f5cd40a56cf8c4a5bda51c1f8ba914a88c3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `depreciation_forecast_agent.py` and embedded as the fenced Python below (sha256 fd371646e8813a1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `depreciation_forecast_agent.py` first:

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
    "version": '2.0.1',
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
