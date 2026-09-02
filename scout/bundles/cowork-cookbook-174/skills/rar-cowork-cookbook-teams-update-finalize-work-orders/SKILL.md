---
name: "rar-cowork-cookbook-teams-update-finalize-work-orders"
description: "Drafts a Teams channel post on finalize work orders status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_finalize_work_orders", "rar_sha256": "3307e3674850eb7098eab4bd76ed3f9c67a45fc48f859706d5f0f42792918beb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_finalize_work_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-finalize-work-orders:b65a285545ba62e6af4483eec1db75410ba37e6ddffd1a536a2ee23ef04474c0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_finalize_work_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_finalize_work_orders_agent.py` is
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
