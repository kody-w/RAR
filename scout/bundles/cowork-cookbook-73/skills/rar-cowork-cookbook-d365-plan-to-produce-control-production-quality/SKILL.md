---
name: "rar-cowork-cookbook-d365-plan-to-produce-control-production-quality"
description: "A Dynamics 365 F&SCM expert scoped to the Control production quality area (a level-2 subdomain of Plan to produce) - covers 8 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_plan_to_produce_control_production_quality", "rar_sha256": "0300a0b47e6e6e1540b3ec1913f2894d9f32b8c39432e1453da882750777a063", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_plan_to_produce_control_production_quality_agent.py` and embedded as the fenced Python below (sha256 0300a0b47e6e6e15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_plan_to_produce_control_production_quality_agent.py` first:

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
    "version": '2.0.0',
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
