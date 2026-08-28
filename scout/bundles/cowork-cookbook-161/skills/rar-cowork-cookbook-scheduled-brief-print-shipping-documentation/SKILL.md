---
name: "rar-cowork-cookbook-scheduled-brief-print-shipping-documentation"
description: "Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_print_shipping_documentation", "rar_sha256": "505ed87297ede4000061d6201e84c889b9ceb4e6a49261ec2189fe393307dedc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_print_shipping_documentation_agent.py` and embedded as the fenced Python below (sha256 505ed87297ede400…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_print_shipping_documentation_agent.py` first:

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
    "version": '2.0.0',
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
