---
name: "rar-cowork-cookbook-teams-update-process-change-orders"
description: "Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_change_orders", "rar_sha256": "ea18e97a646531d9937c2db2a806e55735a25f9b67a0582d6a195f0b8b2a3886", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 ea18e97a646531d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_change_orders_agent.py` first:

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
    "version": '2.0.1',
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
