---
name: "rar-cowork-cookbook-teams-update-finalize-work-orders"
description: "Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_finalize_work_orders", "rar_sha256": "c7e769fe849cf0ad0013278e777aef675888350503876bc1f951a83bf56ed565", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `teams_update_finalize_work_orders_agent.py` and in the RCI capsule.

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

Finalize work orders Teams Channel Update — Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-finalize-work-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 c7e769fe849cf0ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_finalize_work_orders_agent.py` first:

```bash
python3 teams_update_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_finalize_work_orders_agent.py   # or on stdin
python3 teams_update_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Teams Channel Update — Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_finalize_work_orders',
    "version": '2.0.1',
    "display_name": 'Finalize work orders Teams Channel Update',
    "description": 'Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e3f761ccb503c829',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/teams-update-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateFinalizeWorkOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateFinalizeWorkOrders'
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
    print(TeamsUpdateFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
