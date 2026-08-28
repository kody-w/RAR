---
name: "rar-cowork-cookbook-ppt-exec-plan-service-demand"
description: "Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_service_demand", "rar_sha256": "6ae6976e40f00d2607c0c1cf796cdf9a080cd75c9f1ef287d9ea0d0f10cf9050", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_service_demand`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_service_demand_agent.py` and in the RCI capsule.

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

Plan service demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_service_demand_agent.py` and embedded as the fenced Python below (sha256 6ae6976e40f00d26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_service_demand_agent.py` first:

```bash
python3 ppt_exec_plan_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_service_demand_agent.py   # or on stdin
python3 ppt_exec_plan_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan service demand Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_service_demand',
    "version": '2.0.0',
    "display_name": 'Plan service demand Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on plan service demand status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-plan-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44163428fdb76af7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/plan-service-demand'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-plan-service-demand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPlanServiceDemand(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanServiceDemand'
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
    print(PptExecPlanServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
