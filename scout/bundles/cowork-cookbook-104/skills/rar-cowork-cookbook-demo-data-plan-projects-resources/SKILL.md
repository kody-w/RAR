---
name: "rar-cowork-cookbook-demo-data-plan-projects-resources"
description: "Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_projects_resources", "rar_sha256": "4c765f23fa98565ed26c00e10104ce45bc7ba51b7aa9a064925e1a558ef47d75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_projects_resources`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_projects_resources_agent.py` and in the RCI capsule.

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

Plan projects resources Demo Data Generator — Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 4c765f23fa98565e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_projects_resources_agent.py` first:

```bash
python3 demo_data_plan_projects_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_projects_resources_agent.py   # or on stdin
python3 demo_data_plan_projects_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects resources Demo Data Generator — Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-projects-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_projects_resources',
    "version": '2.0.0',
    "display_name": 'Plan projects resources Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-projects-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-projects-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a33ef3c7f8f5e1a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-projects-resources'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-plan-projects-resources', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataPlanProjectsResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanProjectsResources'
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
    print(DemoDataPlanProjectsResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
