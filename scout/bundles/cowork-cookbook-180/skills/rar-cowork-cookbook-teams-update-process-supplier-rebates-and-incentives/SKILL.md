---
name: "rar-cowork-cookbook-teams-update-process-supplier-rebates-and-incentives"
description: "Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives", "rar_sha256": "6cd3252dc7b78785bae95376ea5ca8b21873ea8d98756710a10a2e3e6302c0ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `teams_update_process_supplier_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Process supplier rebates and incentives Teams Channel Update — Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_process_supplier_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 6cd3252dc7b78785…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_process_supplier_rebates_and_incentives_agent.py` first:

```bash
python3 teams_update_process_supplier_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_process_supplier_rebates_and_incentives_agent.py   # or on stdin
python3 teams_update_process_supplier_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier rebates and incentives Teams Channel Update — Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives',
    "version": '2.0.0',
    "display_name": 'Process supplier rebates and incentives Teams Channel Update',
    "description": 'Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-process-supplier-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-process-supplier-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c878686ae633e54f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-rebates-and-incentives'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/teams-update-process-supplier-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateProcessSupplierRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProcessSupplierRebatesAndIncentives'
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
    print(TeamsUpdateProcessSupplierRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
