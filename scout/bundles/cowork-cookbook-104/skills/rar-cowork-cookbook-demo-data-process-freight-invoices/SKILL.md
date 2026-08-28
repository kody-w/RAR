---
name: "rar-cowork-cookbook-demo-data-process-freight-invoices"
description: "Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_freight_invoices", "rar_sha256": "3a002f9fe031426e777667ed0631fe7bae288b9b2114947f031289eefe395dfb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 3a002f9fe031426e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_freight_invoices_agent.py` first:

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
    "version": '2.0.0',
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
