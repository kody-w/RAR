---
name: "rar-cowork-cookbook-scheduled-brief-process-supplier-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives", "rar_sha256": "a17cc1b30f150936a76b992c60fdfa26fd852c5b2ef6b2e3f7f48a298d0b76ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_process_supplier_rebates_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-process-supplier-rebates-and-incentives:0ea7f8459ba9815826893530b6d9303302f7d52945b0ae706476200a0b959adf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` is
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

Process supplier rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 a17cc1b30f150936…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` first:

```bash
python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py   # or on stdin
python3 scheduled_brief_process_supplier_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives',
    "version": '2.0.0',
    "display_name": 'Process supplier rebates and incentives Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-process-supplier-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-process-supplier-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a0bb8f0739ebe944',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-rebates-and-incentives'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-process-supplier-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefProcessSupplierRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefProcessSupplierRebatesAndIncentives'
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
    print(ScheduledBriefProcessSupplierRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
