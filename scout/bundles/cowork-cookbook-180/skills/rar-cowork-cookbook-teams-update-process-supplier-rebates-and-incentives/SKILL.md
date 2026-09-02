---
name: "rar-cowork-cookbook-teams-update-process-supplier-rebates-and-incentives"
description: "Drafts a Teams channel post on process supplier rebates and incentives status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives", "rar_sha256": "6cd3252dc7b78785bae95376ea5ca8b21873ea8d98756710a10a2e3e6302c0ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_process_supplier_rebates_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-process-supplier-rebates-and-incentives:013c43e3feba0ad6a349840b03dc47ab85a154f21757882302898e14fc95dcdd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_process_supplier_rebates_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_process_supplier_rebates_and_incentives_agent.py` is
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
