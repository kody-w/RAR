---
name: "rar-cowork-cookbook-scheduled-brief-define-sales-quotations"
description: "Schedulable morning-brief email summarizing define sales quotations for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_sales_quotations", "rar_sha256": "aee091c88f8fded8b064f60b7bc917e895f2c0ae25c4b4c50f8b28108fca9c31", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_sales_quotations_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-sales-quotations:c3a33789136f8ffaab2411cb09c49bf66665175cbdf8f1f50ba74bef397227cc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_sales_quotations`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_sales_quotations_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_sales_quotations_agent.py` and embedded as the fenced Python below (sha256 aee091c88f8fded8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_sales_quotations_agent.py` first:

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
    "version": '2.0.0',
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
