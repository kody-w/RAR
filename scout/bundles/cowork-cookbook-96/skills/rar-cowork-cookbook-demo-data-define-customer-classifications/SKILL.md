---
name: "rar-cowork-cookbook-demo-data-define-customer-classifications"
description: "Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_customer_classifications", "rar_sha256": "c33e6192dc13adf3189f14eef4bb171fae4bd2c617fbb02bfa00faab337739bc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_customer_classifications`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_customer_classifications_agent.py` and in the RCI capsule.

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

Define customer classifications Demo Data Generator — Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 c33e6192dc13adf3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_customer_classifications_agent.py` first:

```bash
python3 demo_data_define_customer_classifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_customer_classifications_agent.py   # or on stdin
python3 demo_data_define_customer_classifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer classifications Demo Data Generator — Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-customer-classifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_customer_classifications',
    "version": '2.0.1',
    "display_name": 'Define customer classifications Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-define-customer-classifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-customer-classifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4c8de195b9b8a9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-customer-classifications'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-define-customer-classifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataDefineCustomerClassifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCustomerClassifications'
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
    print(DemoDataDefineCustomerClassifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
