---
name: "rar-cowork-cookbook-demo-data-gather-work-order-details"
description: "Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_gather_work_order_details", "rar_sha256": "f44a5d6d0c31cce5f249eec7b6a0bffdf811e8958e34813247a42bbc71038557", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_gather_work_order_details_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-gather-work-order-details:642cd81759373df6739c4b6fb22eba2e45baa13d1a279b5c2662a4cc07ffe9f3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_gather_work_order_details`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_gather_work_order_details_agent.py` is
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

Gather work order details Demo Data Generator — Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-gather-work-order-details
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 f44a5d6d0c31cce5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_gather_work_order_details_agent.py` first:

```bash
python3 demo_data_gather_work_order_details_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_gather_work_order_details_agent.py   # or on stdin
python3 demo_data_gather_work_order_details_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Gather work order details Demo Data Generator — Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-gather-work-order-details
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_gather_work_order_details',
    "version": '2.0.0',
    "display_name": 'Gather work order details Demo Data Generator',
    "description": 'Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-gather-work-order-details',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-gather-work-order-details',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a60de396b4a1e9b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/gather-work-order-details'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-gather-work-order-details', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataGatherWorkOrderDetails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataGatherWorkOrderDetails'
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
    print(DemoDataGatherWorkOrderDetails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
