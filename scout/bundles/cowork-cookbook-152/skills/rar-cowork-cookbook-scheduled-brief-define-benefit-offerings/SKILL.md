---
name: "rar-cowork-cookbook-scheduled-brief-define-benefit-offerings"
description: "Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_benefit_offerings", "rar_sha256": "ca59e718a783de4ae0ee51d54860041e19cac53563d67587c6fb35502c193a7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_benefit_offerings`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_benefit_offerings_agent.py` and in the RCI capsule.

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
