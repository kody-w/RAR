---
name: "rar-cowork-cookbook-scheduled-brief-define-banking-policies"
description: "Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_banking_policies", "rar_sha256": "d20d6b5302ca1d7e3395c2a107f618210377030da586f090cb3dadcc81753f09", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Scheduled Email Brief — Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 d20d6b5302ca1d7e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_banking_policies_agent.py` first:

```bash
python3 scheduled_brief_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_banking_policies_agent.py   # or on stdin
python3 scheduled_brief_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Scheduled Email Brief — Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_banking_policies',
    "version": '2.0.0',
    "display_name": 'Define banking policies Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fdeb9e068a6bc27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefDefineBankingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineBankingPolicies'
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
    print(ScheduledBriefDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
