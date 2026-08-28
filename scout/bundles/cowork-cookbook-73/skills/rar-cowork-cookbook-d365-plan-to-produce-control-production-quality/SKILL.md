---
name: "rar-cowork-cookbook-d365-plan-to-produce-control-production-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce_control_production_quality", "rar_sha256": "76c4b1cd1ee315aa93724ad7c1cf0744e27b00162db7681bd80adaa8c4bc0e9f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_plan_to_produce_control_production_quality`. The original RAPP
agent is preserved byte-for-byte in `d365_plan_to_produce_control_production_quality_agent.py` and in the RCI capsule.

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

D365 Control production quality Expert — A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_control_production_quality_agent.py` and embedded as the fenced Python below (sha256 76c4b1cd1ee315aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_control_production_quality_agent.py` first:

```bash
python3 d365_plan_to_produce_control_production_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_plan_to_produce_control_production_quality_agent.py   # or on stdin
python3 d365_plan_to_produce_control_production_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Control production quality Expert — A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_plan_to_produce_control_production_quality',
    "version": '2.0.1',
    "display_name": 'D365 Control production quality Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-plan-to-produce-control-production-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-plan-to-produce-control-production-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a6e6b6671934857',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'plan-to-produce/d365-plan-to-produce-control-production-quality', 'uses_skills': {'custom': ['d365-plan-to-produce-control-production-quality'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365PlanToProduceControlProductionQuality(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365PlanToProduceControlProductionQuality'
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
    print(D365PlanToProduceControlProductionQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
