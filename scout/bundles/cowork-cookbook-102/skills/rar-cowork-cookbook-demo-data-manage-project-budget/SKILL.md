---
name: "rar-cowork-cookbook-demo-data-manage-project-budget"
description: "Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_project_budget", "rar_sha256": "bab413d07abd10b9b2f3f73c10e61e3f3d41fc098a53fb4bdfedacab65ab7f21", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_project_budget`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_project_budget_agent.py` and in the RCI capsule.

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

Manage project budget Demo Data Generator — Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 bab413d07abd10b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_project_budget_agent.py` first:

```bash
python3 demo_data_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_project_budget_agent.py   # or on stdin
python3 demo_data_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Demo Data Generator — Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_project_budget',
    "version": '2.0.1',
    "display_name": 'Manage project budget Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5edc64f507583617',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManageProjectBudget(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageProjectBudget'
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
    print(DemoDataManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
