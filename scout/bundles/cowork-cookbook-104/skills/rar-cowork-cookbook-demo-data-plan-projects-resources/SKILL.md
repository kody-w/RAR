---
name: "rar-cowork-cookbook-demo-data-plan-projects-resources"
description: "Generates and creates realistic demo records for plan projects resources in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_projects_resources", "rar_sha256": "89d6ce3e25d45c06b39755534358477082c3f0e1e1680a6716d93f61ebb631af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_projects_resources_agent.py` and embedded as the fenced Python below (sha256 89d6ce3e25d45c06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_projects_resources_agent.py` first:

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
    "version": '2.0.1',
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
