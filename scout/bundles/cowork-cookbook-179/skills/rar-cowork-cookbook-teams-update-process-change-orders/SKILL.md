---
name: "rar-cowork-cookbook-teams-update-process-change-orders"
description: "Drafts a Teams channel post on process change orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_change_orders", "rar_sha256": "07515db6f44a597fd5e97284b97e3985dc87ace23a9181e583906ed6a38b9b5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_process_change_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-process-change-orders:e60e6256db5e2cd3f995638d594a6898d8b72fa6065c5457d0f10885c5f2433e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_process_change_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_process_change_orders_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
