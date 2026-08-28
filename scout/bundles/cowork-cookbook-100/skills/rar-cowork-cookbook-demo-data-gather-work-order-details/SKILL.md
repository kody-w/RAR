---
name: "rar-cowork-cookbook-demo-data-gather-work-order-details"
description: "Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_gather_work_order_details", "rar_sha256": "f44a5d6d0c31cce5f249eec7b6a0bffdf811e8958e34813247a42bbc71038557", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_gather_work_order_details`. The original RAPP
agent is preserved byte-for-byte in `demo_data_gather_work_order_details_agent.py` and in the RCI capsule.

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
