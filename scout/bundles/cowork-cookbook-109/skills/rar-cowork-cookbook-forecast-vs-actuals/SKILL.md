---
name: "rar-cowork-cookbook-forecast-vs-actuals"
description: "Compares demand forecast lines to actual sales orders for the same period and items, computes forecast accuracy, and flags poor performers."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/forecast_vs_actuals", "rar_sha256": "bc7bdf6d2cbaf70172d7b13ba0c150ba2bc8acd1e4cf7117692b4685f9a754a5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "forecast_vs_actuals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/forecast-vs-actuals:0f69450b5f23495607de5bcf13b43c9dce60c567229c91d12b546c399771b01f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/forecast_vs_actuals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `forecast_vs_actuals_agent.py` is
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
