---
name: "rar-cowork-cookbook-demo-data-coordinate-service-work-with-customer"
description: "Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_coordinate_service_work_with_customer", "rar_sha256": "9d04af5b6068c589b3265a0141d9cd8aa75d04aba79cf3ce82ef3976b05e6a36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 9d04af5b6068c589…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_coordinate_service_work_with_customer_agent.py` first:

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
    "version": '2.0.0',
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
