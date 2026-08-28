---
name: "rar-cowork-cookbook-d365-forecast-to-plan"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan", "rar_sha256": "ac600a9ffd1657637aec66db9665df38ad9a8c1b28af1b0bf354393a957e7439", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_forecast_to_plan`. The original RAPP
agent is preserved byte-for-byte in `d365_forecast_to_plan_agent.py` and in the RCI capsule.

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

D365 Forecast to plan Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_agent.py` and embedded as the fenced Python below (sha256 ac600a9ffd165763…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_agent.py` first:

```bash
python3 d365_forecast_to_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_agent.py   # or on stdin
python3 d365_forecast_to_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Forecast to plan Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_forecast_to_plan',
    "version": '2.0.0',
    "display_name": 'D365 Forecast to plan Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-forecast-to-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-forecast-to-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd97c4f030e417561',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt+skill', 'upstream_path': 'forecast-to-plan/d365-forecast-to-plan', 'uses_skills': {'custom': ['d365-forecast-to-plan'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class D365ForecastToPlan(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlan'
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
    print(D365ForecastToPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
