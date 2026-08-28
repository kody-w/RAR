---
name: "rar-cowork-cookbook-scheduled-brief-raise-purchase-requisitions"
description: "Schedulable morning-brief email summarizing raise purchase requisitions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_raise_purchase_requisitions", "rar_sha256": "a87536354f56c46b350138a93d3e704f59a21a6f68bbf01fac0f60155c2a5145", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 a87536354f56c46b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_raise_purchase_requisitions_agent.py` first:

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
    "version": '2.0.1',
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
