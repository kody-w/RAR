---
name: "rar-cowork-cookbook-scheduled-brief-process-supplier-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives", "rar_sha256": "a17cc1b30f150936a76b992c60fdfa26fd852c5b2ef6b2e3f7f48a298d0b76ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` and in the RCI capsule.

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
