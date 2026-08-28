---
name: "rar-cowork-cookbook-demo-data-coordinate-service-work-with-customer"
description: "Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_coordinate_service_work_with_customer", "rar_sha256": "59a6a01ae34b39f98432ba7e2dbd32f62b2df0b3a9b7ae063e6de9a6fe479a58", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_coordinate_service_work_with_customer`. The original RAPP
agent is preserved byte-for-byte in `demo_data_coordinate_service_work_with_customer_agent.py` and in the RCI capsule.

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

Coordinate service work with customer Demo Data Generator — Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 59a6a01ae34b39f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_coordinate_service_work_with_customer_agent.py` first:

```bash
python3 demo_data_coordinate_service_work_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_coordinate_service_work_with_customer_agent.py   # or on stdin
python3 demo_data_coordinate_service_work_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Coordinate service work with customer Demo Data Generator — Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_coordinate_service_work_with_customer',
    "version": '2.0.1',
    "display_name": 'Coordinate service work with customer Demo Data Generator',
    "description": 'Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-coordinate-service-work-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-coordinate-service-work-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f270701101f59708',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/coordinate-service-work-with-customer'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-coordinate-service-work-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCoordinateServiceWorkWithCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCoordinateServiceWorkWithCustomer'
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
    print(DemoDataCoordinateServiceWorkWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
