---
name: "rar-cowork-cookbook-teams-update-finalize-work-orders"
description: "Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_finalize_work_orders", "rar_sha256": "3307e3674850eb7098eab4bd76ed3f9c67a45fc48f859706d5f0f42792918beb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 3307e3674850eb70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_finalize_work_orders_agent.py` first:

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
    "version": '2.0.0',
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
