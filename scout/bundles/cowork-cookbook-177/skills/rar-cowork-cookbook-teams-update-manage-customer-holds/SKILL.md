---
name: "rar-cowork-cookbook-teams-update-manage-customer-holds"
description: "Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_customer_holds", "rar_sha256": "7ad2018747a96032f9a7fa6e7b3dcbba7a182b9f0be0a4af60028af3c349cdd4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `teams_update_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Teams Channel Update — Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 7ad2018747a96032…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_customer_holds_agent.py` first:

```bash
python3 teams_update_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_customer_holds_agent.py   # or on stdin
python3 teams_update_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Teams Channel Update — Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_customer_holds',
    "version": '2.0.0',
    "display_name": 'Manage customer holds Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe08c03e5a7dbfb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/teams-update-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateManageCustomerHolds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageCustomerHolds'
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
    print(TeamsUpdateManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
