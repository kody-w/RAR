---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-quotations"
description: "Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_quotations", "rar_sha256": "644aec4af22a08adbf960780982a8a66c26fa67fba5053037a028f3dc3f729b6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_sales_quotations`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_sales_quotations_agent.py` and in the RCI capsule.

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

Define sales quotations Scheduled Email Brief — Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 644aec4af22a08ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_quotations_agent.py` first:

```bash
python3 scheduled_brief_define_sales_quotations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_sales_quotations_agent.py   # or on stdin
python3 scheduled_brief_define_sales_quotations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales quotations Scheduled Email Brief — Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_sales_quotations',
    "version": '2.0.1',
    "display_name": 'Define sales quotations Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-sales-quotations',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-sales-quotations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b3e67fc242e2cb4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-sales-quotations'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/scheduled-brief-define-sales-quotations', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineSalesQuotations(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineSalesQuotations'
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
    print(ScheduledBriefDefineSalesQuotations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
