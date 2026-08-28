---
name: "rar-cowork-cookbook-scheduled-brief-start-production"
description: "Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_start_production", "rar_sha256": "74a8c9125bb60b3e99d2622361ec110ad2abb6e0ba676797c566fd037c5f1a3e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_start_production`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_start_production_agent.py` and in the RCI capsule.

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

Start production Scheduled Email Brief — Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-start-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_start_production_agent.py` and embedded as the fenced Python below (sha256 74a8c9125bb60b3e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_start_production_agent.py` first:

```bash
python3 scheduled_brief_start_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_start_production_agent.py   # or on stdin
python3 scheduled_brief_start_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Start production Scheduled Email Brief — Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-start-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_start_production',
    "version": '2.0.1',
    "display_name": 'Start production Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-start-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-start-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a9a46acf85647145',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/start-production'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-start-production', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefStartProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefStartProduction'
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
    print(ScheduledBriefStartProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
