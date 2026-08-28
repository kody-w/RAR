---
name: "rar-cowork-cookbook-demo-data-process-freight-invoices"
description: "Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_freight_invoices", "rar_sha256": "5531a0e79ea719362c3a9686802d528d289756a5c9ee2a9faea760b735fa0544", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_process_freight_invoices`. The original RAPP
agent is preserved byte-for-byte in `demo_data_process_freight_invoices_agent.py` and in the RCI capsule.

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

Process freight invoices Demo Data Generator — Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-freight-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 5531a0e79ea71936…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_freight_invoices_agent.py` first:

```bash
python3 demo_data_process_freight_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_process_freight_invoices_agent.py   # or on stdin
python3 demo_data_process_freight_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process freight invoices Demo Data Generator — Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-freight-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_process_freight_invoices',
    "version": '2.0.1',
    "display_name": 'Process freight invoices Demo Data Generator',
    "description": 'Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-process-freight-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-process-freight-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b90d786f3d8a9286',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/process-freight-invoices'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-process-freight-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataProcessFreightInvoices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcessFreightInvoices'
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
    print(DemoDataProcessFreightInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
