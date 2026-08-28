---
name: "rar-cowork-cookbook-scheduled-brief-transfer-budgets"
description: "Schedulable morning-brief email summarizing transfer budgets for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_budgets", "rar_sha256": "e1022ddeb45777e2741d8412e61ea37bba6c3c149e4c87dcaa0e129a9d6c81dc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_budgets_agent.py` and embedded as the fenced Python below (sha256 e1022ddeb45777e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_budgets_agent.py` first:

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
    "version": '2.0.1',
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
