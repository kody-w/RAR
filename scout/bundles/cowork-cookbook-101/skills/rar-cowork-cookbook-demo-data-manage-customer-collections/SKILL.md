---
name: "rar-cowork-cookbook-demo-data-manage-customer-collections"
description: "Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_customer_collections", "rar_sha256": "12594d892b09c0c83ddfa77bc9db4edde9f14aa9985b9b9d84327e94abbd524a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_customer_collections_agent.py` and in the RCI capsule.

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

Manage customer collections Demo Data Generator — Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 12594d892b09c0c8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_customer_collections_agent.py` first:

```bash
python3 demo_data_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_customer_collections_agent.py   # or on stdin
python3 demo_data_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Demo Data Generator — Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_customer_collections',
    "version": '2.0.1',
    "display_name": 'Manage customer collections Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b121a4da052620ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageCustomerCollections(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageCustomerCollections'
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
    print(DemoDataManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
