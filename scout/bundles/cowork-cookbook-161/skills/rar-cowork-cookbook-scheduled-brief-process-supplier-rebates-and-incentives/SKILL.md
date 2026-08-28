---
name: "rar-cowork-cookbook-scheduled-brief-process-supplier-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing process supplier rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_process_supplier_rebates_and_incentives", "rar_sha256": "e7e6ce8178999eb19a128ffc5251ebb50ad48db74c8c924acf3ef40f1a953646", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 e7e6ce8178999eb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_process_supplier_rebates_and_incentives_agent.py` first:

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
    "version": '2.0.1',
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
