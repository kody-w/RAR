---
name: "rar-cowork-cookbook-demo-data-manage-bills-of-exchange"
description: "Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_bills_of_exchange", "rar_sha256": "57c5671556245dac6acf204d495fb1ed9d52d35484c2f561e3457f7e90a21b19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_bills_of_exchange_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-bills-of-exchange:446fce72b5787bdbff44c108e20a15c7a22b7d9f17f2423ce6c5dfef4ba32379", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_bills_of_exchange`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_bills_of_exchange_agent.py` is
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

Manage bills of exchange Demo Data Generator — Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 57c5671556245dac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_bills_of_exchange_agent.py` first:

```bash
python3 demo_data_manage_bills_of_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_bills_of_exchange_agent.py   # or on stdin
python3 demo_data_manage_bills_of_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of exchange Demo Data Generator — Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_bills_of_exchange',
    "version": '2.0.0',
    "display_name": 'Manage bills of exchange Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage bills of exchange in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-bills-of-exchange',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55dbc570073694d0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-bills-of-exchange'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-bills-of-exchange', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageBillsOfExchange(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBillsOfExchange'
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
    print(DemoDataManageBillsOfExchange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
