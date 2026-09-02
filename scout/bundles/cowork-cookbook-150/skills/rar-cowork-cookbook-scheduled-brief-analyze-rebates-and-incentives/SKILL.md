---
name: "rar-cowork-cookbook-scheduled-brief-analyze-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives", "rar_sha256": "aa313be370e20877dfe8ae9805be78b721a0d664450d1a274aad894aa91e7fcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_analyze_rebates_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-analyze-rebates-and-incentives:efabe176d972f92cbe7e4f02041c6ec0ba0779a6693d8c3e6124589d825f1419", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_analyze_rebates_and_incentives_agent.py` is
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
