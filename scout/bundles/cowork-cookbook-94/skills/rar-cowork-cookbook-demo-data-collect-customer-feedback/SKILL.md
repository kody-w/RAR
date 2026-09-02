---
name: "rar-cowork-cookbook-demo-data-collect-customer-feedback"
description: "Generates and creates realistic demo records for collect customer feedback in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_collect_customer_feedback", "rar_sha256": "b40710f51a1ec0b04d912f51a29d83347173665098fb56345879f83314ac5d83", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_collect_customer_feedback_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-collect-customer-feedback:aa66f9f60bd4c3bcc659a381a302740d0901d1b79688443d0ebec16d0fb4b84b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_collect_customer_feedback`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_collect_customer_feedback_agent.py` is
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
