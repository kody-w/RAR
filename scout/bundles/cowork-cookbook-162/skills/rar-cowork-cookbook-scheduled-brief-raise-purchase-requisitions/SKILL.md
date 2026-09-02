---
name: "rar-cowork-cookbook-scheduled-brief-raise-purchase-requisitions"
description: "Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_raise_purchase_requisitions", "rar_sha256": "20f0cb121a1eca8fede753e6af23cfbfd98b435ce375cb14c27e6cbe48e3585b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_raise_purchase_requisitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-raise-purchase-requisitions:dd16708500e63420be0bc27f10caf8ba88ae4d5780beccc0af2f58d6ac2c71f3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_raise_purchase_requisitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_raise_purchase_requisitions_agent.py` is
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

Raise purchase requisitions Scheduled Email Brief — Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 20f0cb121a1eca8f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_raise_purchase_requisitions_agent.py` first:

```bash
python3 scheduled_brief_raise_purchase_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_raise_purchase_requisitions_agent.py   # or on stdin
python3 scheduled_brief_raise_purchase_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Raise purchase requisitions Scheduled Email Brief — Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_raise_purchase_requisitions',
    "version": '2.0.0',
    "display_name": 'Raise purchase requisitions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-raise-purchase-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-raise-purchase-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae952f5aa63c5a9e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/raise-purchase-requisitions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-raise-purchase-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRaisePurchaseRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRaisePurchaseRequisitions'
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
    print(ScheduledBriefRaisePurchaseRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
