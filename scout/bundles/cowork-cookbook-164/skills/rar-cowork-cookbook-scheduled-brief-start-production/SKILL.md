---
name: "rar-cowork-cookbook-scheduled-brief-start-production"
description: "Schedulable morning-brief email summarizing start production for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_start_production", "rar_sha256": "8316f27131bffb78f13580bffdf293b28587b2867f2c63d6c57edab2a010ba66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_start_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-start-production:a60b4d75f0ddbe14e24fab337e6d14e8c93e5583cc9252d0ac2dbf3d9e5ee2fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_start_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_start_production_agent.py` is
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
