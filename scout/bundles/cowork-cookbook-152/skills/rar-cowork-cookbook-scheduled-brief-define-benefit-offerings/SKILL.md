---
name: "rar-cowork-cookbook-scheduled-brief-define-benefit-offerings"
description: "Schedulable morning-brief email summarizing define benefit offerings for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_benefit_offerings", "rar_sha256": "1645baa930945c1a576d63d864457becd6d155f8ec34447f09249e6107d69359", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_benefit_offerings_agent.py` and embedded as the fenced Python below (sha256 1645baa930945c1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_benefit_offerings_agent.py` first:

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
    "version": '2.0.1',
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
