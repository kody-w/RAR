---
name: "rar-cowork-cookbook-adaptive-card-gather-work-order-details"
description: "Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_gather_work_order_details", "rar_sha256": "d027f6fde5da0664630a3297479d9a5465826310b4c3eb632483d5aaed94cd87", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_gather_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_gather_work_order_details_agent.py` and in the RCI capsule.

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

Gather work order details Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 d027f6fde5da0664…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_gather_work_order_details_agent.py` first:

```bash
python3 adaptive_card_gather_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_gather_work_order_details_agent.py   # or on stdin
python3 adaptive_card_gather_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gather work order details Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_gather_work_order_details',
    "version": '2.0.1',
    "display_name": 'Gather work order details Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-gather-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-gather-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c46bd0fed844ea40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/gather-work-order-details'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-gather-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardGatherWorkOrderDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardGatherWorkOrderDetails'
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
    print(AdaptiveCardGatherWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
