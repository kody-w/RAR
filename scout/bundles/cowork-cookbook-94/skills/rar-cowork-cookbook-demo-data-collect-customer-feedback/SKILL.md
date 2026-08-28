---
name: "rar-cowork-cookbook-demo-data-collect-customer-feedback"
description: "Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_collect_customer_feedback", "rar_sha256": "b40710f51a1ec0b04d912f51a29d83347173665098fb56345879f83314ac5d83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_collect_customer_feedback_agent.py` and embedded as the fenced Python below (sha256 b40710f51a1ec0b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_collect_customer_feedback_agent.py` first:

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
    "version": '2.0.0',
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
