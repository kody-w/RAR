---
name: "rar-cowork-cookbook-scheduled-brief-transfer-budgets"
description: "Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_budgets", "rar_sha256": "9d3270e5b26aea4cc3fdef0e0c9e241f772550ec3fe014d4cd6e586185715264", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_transfer_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-transfer-budgets:be103b9cd928b2b77cc7422db03052ea82d9c1308c048546c83fb6eca690e7ec", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_transfer_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_transfer_budgets_agent.py` is
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

Transfer budgets Scheduled Email Brief — Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 9d3270e5b26aea4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_budgets_agent.py` first:

```bash
python3 scheduled_brief_transfer_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_budgets_agent.py   # or on stdin
python3 scheduled_brief_transfer_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer budgets Scheduled Email Brief — Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_budgets',
    "version": '2.0.0',
    "display_name": 'Transfer budgets Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-transfer-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1c7fbd23724611fd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/transfer-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-transfer-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefTransferBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferBudgets'
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
    print(ScheduledBriefTransferBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
