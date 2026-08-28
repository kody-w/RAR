---
name: "rar-cowork-cookbook-scheduled-brief-start-production"
description: "Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_start_production", "rar_sha256": "8316f27131bffb78f13580bffdf293b28587b2867f2c63d6c57edab2a010ba66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_start_production_agent.py` and embedded as the fenced Python below (sha256 8316f27131bffb78…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_start_production_agent.py` first:

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
    "version": '2.0.0',
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
