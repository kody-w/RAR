---
name: "rar-cowork-cookbook-teams-update-manage-customer-holds"
description: "Drafts a Teams channel post on manage customer holds status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_customer_holds", "rar_sha256": "7ad2018747a96032f9a7fa6e7b3dcbba7a182b9f0be0a4af60028af3c349cdd4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_customer_holds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-customer-holds:62e756ae441429e0d56269b82a145b9e23a2aed844de20240edb5fed3df44bfd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_customer_holds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_customer_holds_agent.py` is
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
