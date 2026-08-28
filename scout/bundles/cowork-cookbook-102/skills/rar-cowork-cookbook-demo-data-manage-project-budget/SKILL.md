---
name: "rar-cowork-cookbook-demo-data-manage-project-budget"
description: "Generates and creates realistic demo records for manage project budget in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_project_budget", "rar_sha256": "84a278256788bea2bb3e22736bb718d997a2f66d5b7637de3589368bed0e536e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 84a278256788bea2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_project_budget_agent.py` first:

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
    "version": '2.0.0',
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
