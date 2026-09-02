---
name: "rar-cowork-cookbook-scheduled-brief-define-benefit-offerings"
description: "Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_benefit_offerings", "rar_sha256": "ca59e718a783de4ae0ee51d54860041e19cac53563d67587c6fb35502c193a7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_benefit_offerings_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-benefit-offerings:c415e74a2ddca37ace1b7e29005c1c8380440c0e031ca51bc9cd6c7501dea61b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_benefit_offerings`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_benefit_offerings_agent.py` is
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

Define benefit offerings Scheduled Email Brief — Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 ca59e718a783de4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_benefit_offerings_agent.py` first:

```bash
python3 scheduled_brief_define_benefit_offerings_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_benefit_offerings_agent.py   # or on stdin
python3 scheduled_brief_define_benefit_offerings_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define benefit offerings Scheduled Email Brief — Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_benefit_offerings',
    "version": '2.0.0',
    "display_name": 'Define benefit offerings Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-benefit-offerings',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-benefit-offerings',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '245d0eca27e671cd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-benefit-offerings'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-define-benefit-offerings', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineBenefitOfferings(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineBenefitOfferings'
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
    print(ScheduledBriefDefineBenefitOfferings().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
