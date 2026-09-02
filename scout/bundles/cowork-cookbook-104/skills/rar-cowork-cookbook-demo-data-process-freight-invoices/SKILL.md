---
name: "rar-cowork-cookbook-demo-data-process-freight-invoices"
description: "Generates and creates realistic demo records for process freight invoices in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_freight_invoices", "rar_sha256": "3a002f9fe031426e777667ed0631fe7bae288b9b2114947f031289eefe395dfb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_process_freight_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-process-freight-invoices:f470154836e52280427e0c13cf054f861c530b0005aa93480894ddd07bfb82dc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_process_freight_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_process_freight_invoices_agent.py` is
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
