---
name: "rar-cowork-cookbook-scheduled-brief-analyze-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives", "rar_sha256": "aa313be370e20877dfe8ae9805be78b721a0d664450d1a274aad894aa91e7fcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Analyze rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 aa313be370e20877…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives',
    "version": '2.0.0',
    "display_name": 'Analyze rebates and incentives Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63a9d8859abbba8b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefAnalyzeRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeRebatesAndIncentives'
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
    print(ScheduledBriefAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
