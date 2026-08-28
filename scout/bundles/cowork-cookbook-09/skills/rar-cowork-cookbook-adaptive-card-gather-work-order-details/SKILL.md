---
name: "rar-cowork-cookbook-adaptive-card-gather-work-order-details"
description: "Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_gather_work_order_details", "rar_sha256": "3f257a54ce69227ef8b96ab50ed1055f30f6cf63436c9adf170c0678896b032f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 3f257a54ce69227e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_gather_work_order_details_agent.py` first:

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
    "version": '2.0.0',
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
