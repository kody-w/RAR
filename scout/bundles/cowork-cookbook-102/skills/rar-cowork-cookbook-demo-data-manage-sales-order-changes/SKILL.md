---
name: "rar-cowork-cookbook-demo-data-manage-sales-order-changes"
description: "Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_sales_order_changes", "rar_sha256": "d54fee2e0b7cb32d4c44b517efc30ccd03fb72ea0fe3c657d7ff6cfda3769053", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_manage_sales_order_changes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-manage-sales-order-changes:5f44f6e8859fab1a87201c1b80a7acf4751228d2deca2c7b130d088d3c7732d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_manage_sales_order_changes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_manage_sales_order_changes_agent.py` is
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

Manage sales order changes Demo Data Generator — Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_sales_order_changes_agent.py` and embedded as the fenced Python below (sha256 d54fee2e0b7cb32d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_sales_order_changes_agent.py` first:

```bash
python3 demo_data_manage_sales_order_changes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_sales_order_changes_agent.py   # or on stdin
python3 demo_data_manage_sales_order_changes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order changes Demo Data Generator — Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_sales_order_changes',
    "version": '2.0.0',
    "display_name": 'Manage sales order changes Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage sales order changes in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-manage-sales-order-changes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-sales-order-changes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd2a39f6956d20e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-changes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-sales-order-changes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageSalesOrderChanges(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageSalesOrderChanges'
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
    print(DemoDataManageSalesOrderChanges().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
