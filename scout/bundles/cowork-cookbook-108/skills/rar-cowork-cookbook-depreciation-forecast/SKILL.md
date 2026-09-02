---
name: "rar-cowork-cookbook-depreciation-forecast"
description: "Forecasts the next 12 months of depreciation expense by asset group and by GL account."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/depreciation_forecast", "rar_sha256": "142a9fcc0006429dff6791ac42021d70a510890f3b71798b20dc67a4f1387be8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "depreciation_forecast_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/depreciation-forecast:e099c0ea698eab28f9d84e3ee25853260f217d0d7b671e1357e96391a8223eb1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/depreciation_forecast`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `depreciation_forecast_agent.py` is
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
