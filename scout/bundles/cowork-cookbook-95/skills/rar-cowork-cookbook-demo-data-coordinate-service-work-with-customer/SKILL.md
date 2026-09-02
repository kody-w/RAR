---
name: "rar-cowork-cookbook-demo-data-coordinate-service-work-with-customer"
description: "Generates and creates realistic demo records for coordinate service work with customer in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_coordinate_service_work_with_customer", "rar_sha256": "9d04af5b6068c589b3265a0141d9cd8aa75d04aba79cf3ce82ef3976b05e6a36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_coordinate_service_work_with_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-coordinate-service-work-with-customer:563b783efb10deefe637bbc0902a59a2fe338cc7d470f303ae61451976a19cf6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_coordinate_service_work_with_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_coordinate_service_work_with_customer_agent.py` is
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
