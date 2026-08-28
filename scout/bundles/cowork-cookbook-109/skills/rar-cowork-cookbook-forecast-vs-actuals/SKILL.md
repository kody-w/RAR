---
name: "rar-cowork-cookbook-forecast-vs-actuals"
description: "Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/forecast_vs_actuals", "rar_sha256": "3cfece934e659bf2cdf6d88df6072b643d5375a0d0a8457bce05d38f655c233e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/forecast_vs_actuals`. The original RAPP
agent is preserved byte-for-byte in `forecast_vs_actuals_agent.py` and in the RCI capsule.

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

Demand Forecast vs Actuals Variance — Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/forecast-vs-actuals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `forecast_vs_actuals_agent.py` and embedded as the fenced Python below (sha256 3cfece934e659bf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `forecast_vs_actuals_agent.py` first:

```bash
python3 forecast_vs_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 forecast_vs_actuals_agent.py   # or on stdin
python3 forecast_vs_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Demand Forecast vs Actuals Variance — Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/forecast-vs-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/forecast_vs_actuals',
    "version": '2.0.1',
    "display_name": 'Demand Forecast vs Actuals Variance',
    "description": 'Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'forecast-vs-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/forecast-vs-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a1ce85e9fd68cbd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/forecast-vs-actuals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ForecastVsActuals(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ForecastVsActuals'
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
    print(ForecastVsActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
