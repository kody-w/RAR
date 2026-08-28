---
name: "rar-cowork-cookbook-demo-data-collect-customer-feedback"
description: "Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_collect_customer_feedback", "rar_sha256": "0f136f302472294dba11c81462ce4750597b054db1fa55a78e04052d05a8d0b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_collect_customer_feedback`. The original RAPP
agent is preserved byte-for-byte in `demo_data_collect_customer_feedback_agent.py` and in the RCI capsule.

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

Collect customer feedback Demo Data Generator — Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 0f136f302472294d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_collect_customer_feedback_agent.py` first:

```bash
python3 demo_data_collect_customer_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_collect_customer_feedback_agent.py   # or on stdin
python3 demo_data_collect_customer_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collect customer feedback Demo Data Generator — Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_collect_customer_feedback',
    "version": '2.0.1',
    "display_name": 'Collect customer feedback Demo Data Generator',
    "description": 'Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-collect-customer-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-collect-customer-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b77c8e9aebf2d04f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collect-customer-feedback'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-collect-customer-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCollectCustomerFeedback(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCollectCustomerFeedback'
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
    print(DemoDataCollectCustomerFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
