---
name: "rar-cowork-cookbook-scheduled-brief-finalize-work-orders"
description: "Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_finalize_work_orders", "rar_sha256": "a3c02bb4e9a724add8613c3dc9cf5524e187a2ed35136a8f929f18d127d3926d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_finalize_work_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-finalize-work-orders:b39ff325a073f488d80eed004fd1737029387e96efe060340b892e7ea373a16e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_finalize_work_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_finalize_work_orders_agent.py` is
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

Finalize work orders Scheduled Email Brief — Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 a3c02bb4e9a724ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_finalize_work_orders_agent.py` first:

```bash
python3 scheduled_brief_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_finalize_work_orders_agent.py   # or on stdin
python3 scheduled_brief_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Scheduled Email Brief — Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_finalize_work_orders',
    "version": '2.0.0',
    "display_name": 'Finalize work orders Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '857b73424625a6b3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefFinalizeWorkOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFinalizeWorkOrders'
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
    print(ScheduledBriefFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
