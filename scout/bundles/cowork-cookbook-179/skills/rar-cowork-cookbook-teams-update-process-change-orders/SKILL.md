---
name: "rar-cowork-cookbook-teams-update-process-change-orders"
description: "Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_change_orders", "rar_sha256": "07515db6f44a597fd5e97284b97e3985dc87ace23a9181e583906ed6a38b9b5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_change_orders`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_change_orders_agent.py` and in the RCI capsule.

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

Process change orders Teams Channel Update — Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-change-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 07515db6f44a597f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_change_orders_agent.py` first:

```bash
python3 teams_update_process_change_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_change_orders_agent.py   # or on stdin
python3 teams_update_process_change_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change orders Teams Channel Update — Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-change-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_change_orders',
    "version": '2.0.0',
    "display_name": 'Process change orders Teams Channel Update',
    "description": 'Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-change-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-change-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '766175e4197c8af9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-orders'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/teams-update-process-change-orders', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateProcessChangeOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessChangeOrders'
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
    print(TeamsUpdateProcessChangeOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
