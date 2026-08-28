---
name: "rar-cowork-cookbook-forecast-vs-actuals"
description: "Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/forecast_vs_actuals", "rar_sha256": "bc7bdf6d2cbaf70172d7b13ba0c150ba2bc8acd1e4cf7117692b4685f9a754a5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `forecast_vs_actuals_agent.py` and embedded as the fenced Python below (sha256 bc7bdf6d2cbaf701…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `forecast_vs_actuals_agent.py` first:

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
    "version": '2.0.0',
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
