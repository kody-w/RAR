---
name: "rar-cowork-cookbook-scheduled-brief-transfer-budgets"
description: "Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_budgets", "rar_sha256": "9d3270e5b26aea4cc3fdef0e0c9e241f772550ec3fe014d4cd6e586185715264", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_transfer_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_transfer_budgets_agent.py` and in the RCI capsule.

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
