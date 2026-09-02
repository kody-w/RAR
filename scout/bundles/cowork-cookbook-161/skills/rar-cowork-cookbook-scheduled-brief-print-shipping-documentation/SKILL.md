---
name: "rar-cowork-cookbook-scheduled-brief-print-shipping-documentation"
description: "Schedulable morning-brief email summarizing print shipping documentation for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_print_shipping_documentation", "rar_sha256": "505ed87297ede4000061d6201e84c889b9ceb4e6a49261ec2189fe393307dedc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_print_shipping_documentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-print-shipping-documentation:47a3de8102449f4c361e9ec3ead21106e40430407abf1f1cfc42e4403b55ca79", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_print_shipping_documentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_print_shipping_documentation_agent.py` is
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
