---
name: "rar-cowork-cookbook-scheduled-brief-define-banking-policies"
description: "Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_banking_policies", "rar_sha256": "d20d6b5302ca1d7e3395c2a107f618210377030da586f090cb3dadcc81753f09", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_banking_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-banking-policies:3fcf9d9ab2697b6fd15d590bbaa4c149378d957adad7f2ce67a1226d89492515", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_banking_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_banking_policies_agent.py` is
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
