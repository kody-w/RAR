---
name: "rar-cowork-cookbook-scheduled-brief-finalize-work-orders"
description: "Schedulable morning-brief email summarizing finalize work orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_finalize_work_orders", "rar_sha256": "d49251821ccafdddeb137ec34f2153647bbc44bbc87d272f799cd708583fa913", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_finalize_work_orders_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 d49251821ccafddd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_finalize_work_orders_agent.py` first:

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
    "version": '2.0.1',
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
