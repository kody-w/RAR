---
name: "rar-cowork-cookbook-adaptive-card-gather-work-order-details"
description: "Produces a reusable Adaptive Card JSON snapshot of gather work order details status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_gather_work_order_details", "rar_sha256": "3f257a54ce69227ef8b96ab50ed1055f30f6cf63436c9adf170c0678896b032f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_gather_work_order_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-gather-work-order-details:4247c3fa76843abc2d3978696c558dbec00f690c82f5ace4fdf81f8c7e9fdfa5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_gather_work_order_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_gather_work_order_details_agent.py` is
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
