---
name: "rar-cowork-cookbook-scheduled-brief-print-shipping-documentation"
description: "Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_print_shipping_documentation", "rar_sha256": "31347fbe08c523d020bae272a022395148cf1da30b606994d0a26511d8d8a20f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_print_shipping_documentation`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_print_shipping_documentation_agent.py` and in the RCI capsule.

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

Print shipping documentation Scheduled Email Brief — Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 31347fbe08c523d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_print_shipping_documentation_agent.py` first:

```bash
python3 scheduled_brief_print_shipping_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_print_shipping_documentation_agent.py   # or on stdin
python3 scheduled_brief_print_shipping_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Print shipping documentation Scheduled Email Brief — Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_print_shipping_documentation',
    "version": '2.0.1',
    "display_name": 'Print shipping documentation Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-print-shipping-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-print-shipping-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8722bc5d24bf322d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/print-shipping-documentation'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-print-shipping-documentation', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefPrintShippingDocumentation(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPrintShippingDocumentation'
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
    print(ScheduledBriefPrintShippingDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
