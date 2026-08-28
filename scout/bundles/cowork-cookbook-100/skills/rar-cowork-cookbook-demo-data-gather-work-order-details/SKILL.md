---
name: "rar-cowork-cookbook-demo-data-gather-work-order-details"
description: "Generates and creates realistic demo records for gather work order details in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_gather_work_order_details", "rar_sha256": "f4e565f6a1d1954fd25d69ceebf4f3870f71c5ebb7e384307c2d0090133ed666", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_gather_work_order_details_agent.py` and embedded as the fenced Python below (sha256 f4e565f6a1d1954f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_gather_work_order_details_agent.py` first:

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
    "version": '2.0.1',
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
