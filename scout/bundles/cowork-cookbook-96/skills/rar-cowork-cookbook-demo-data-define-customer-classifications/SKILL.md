---
name: "rar-cowork-cookbook-demo-data-define-customer-classifications"
description: "Generates and creates realistic demo records for define customer classifications in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_customer_classifications", "rar_sha256": "86daf0e1799b3a45f367fc9d833c6d66c07015430de796f47a2e5e90f80a891c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_define_customer_classifications_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-define-customer-classifications:f3ea8f78c2a3d8f25d49da93d2566806dfb9c5a03af6d036a04d39438a5666d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_define_customer_classifications`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_define_customer_classifications_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_customer_classifications_agent.py` and embedded as the fenced Python below (sha256 86daf0e1799b3a45…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_customer_classifications_agent.py` first:

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
    "version": '2.0.0',
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
