---
name: "rar-cowork-cookbook-demo-data-manage-customer-collections"
description: "Generates and creates realistic demo records for manage customer collections in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_customer_collections", "rar_sha256": "ed267f9cfa6b5d9a0aadb2941467be23c4f0cf3d2578ddb0995e86190dde7cbf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_customer_collections_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-customer-collections:085555c289643961106b3fd1c18821a1a200201b949951f4609d0ebfeb68ed35", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_customer_collections`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_customer_collections_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 ed267f9cfa6b5d9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_customer_collections_agent.py` first:

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
    "version": '2.0.0',
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
