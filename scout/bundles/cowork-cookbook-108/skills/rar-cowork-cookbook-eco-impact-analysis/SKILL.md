---
name: "rar-cowork-cookbook-eco-impact-analysis"
description: "For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/eco_impact_analysis", "rar_sha256": "342629ab28db05ce912e4199dcf7edf9c1988f159a5c388250075d00a78b70b2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/eco_impact_analysis`. The original RAPP
agent is preserved byte-for-byte in `eco_impact_analysis_agent.py` and in the RCI capsule.

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

Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `eco_impact_analysis_agent.py` and embedded as the fenced Python below (sha256 342629ab28db05ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `eco_impact_analysis_agent.py` first:

```bash
python3 eco_impact_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 eco_impact_analysis_agent.py   # or on stdin
python3 eco_impact_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Engineering Change Order Impact Analysis — For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/eco-impact-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/eco_impact_analysis',
    "version": '2.0.0',
    "display_name": 'Engineering Change Order Impact Analysis',
    "description": 'For a proposed item change, finds every BOM, sales order, and inventory location affected and quantifies downstream impact.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'eco-impact-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/eco-impact-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '517aedd76241ae96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/eco-impact-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class EcoImpactAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'EcoImpactAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(EcoImpactAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
