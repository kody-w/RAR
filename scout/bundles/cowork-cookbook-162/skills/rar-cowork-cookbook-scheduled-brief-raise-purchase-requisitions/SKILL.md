---
name: "rar-cowork-cookbook-scheduled-brief-raise-purchase-requisitions"
description: "Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_raise_purchase_requisitions", "rar_sha256": "20f0cb121a1eca8fede753e6af23cfbfd98b435ce375cb14c27e6cbe48e3585b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_raise_purchase_requisitions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_raise_purchase_requisitions_agent.py` and in the RCI capsule.

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
