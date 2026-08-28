---
name: "rar-cowork-cookbook-adaptive-card-manage-project-budget"
description: "Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_project_budget", "rar_sha256": "fc1a485981c3bc925cc2051a42ffb551279752fbd79fad458cbf927f5061fdea", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_manage_project_budget`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_manage_project_budget_agent.py` and in the RCI capsule.

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

Manage project budget Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_project_budget_agent.py` and embedded as the fenced Python below (sha256 fc1a485981c3bc92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_project_budget_agent.py` first:

```bash
python3 adaptive_card_manage_project_budget_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_project_budget_agent.py   # or on stdin
python3 adaptive_card_manage_project_budget_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project budget Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_project_budget',
    "version": '2.0.1',
    "display_name": 'Manage project budget Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage project budget status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-project-budget',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-project-budget',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2fd56f0c92669f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/manage-project-budget'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-manage-project-budget', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageProjectBudget(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageProjectBudget'
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
    print(AdaptiveCardManageProjectBudget().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
