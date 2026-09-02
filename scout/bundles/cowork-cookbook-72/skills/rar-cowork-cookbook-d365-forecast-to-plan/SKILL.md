---
name: "rar-cowork-cookbook-d365-forecast-to-plan"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Forecast to plan end-to-end process - covers 5 L2 areas and 45 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan", "rar_sha256": "ac600a9ffd1657637aec66db9665df38ad9a8c1b28af1b0bf354393a957e7439", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_forecast_to_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-forecast-to-plan:73d463ff3bb6c4eae6a6813d811c5caba534c04e9868bedfffd7c561bd34927e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_forecast_to_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_forecast_to_plan_agent.py` is
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
