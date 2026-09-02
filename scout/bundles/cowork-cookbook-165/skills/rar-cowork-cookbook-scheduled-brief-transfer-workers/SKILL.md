---
name: "rar-cowork-cookbook-scheduled-brief-transfer-workers"
description: "Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_workers", "rar_sha256": "e71faa8de020906f6ff44cb70c984c0dea5a9ad46ae301944112633fd6a932b7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_transfer_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-transfer-workers:e599afbd70675a9daca3984ce73f2205fa7eb1d8ccbc516e3db04f59c8b9c1b6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_transfer_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_transfer_workers_agent.py` is
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

Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 e71faa8de020906f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_workers_agent.py` first:

```bash
python3 scheduled_brief_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_workers_agent.py   # or on stdin
python3 scheduled_brief_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_workers',
    "version": '2.0.0',
    "display_name": 'Transfer workers Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f8c71f75a13d0a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefTransferWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferWorkers'
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
    print(ScheduledBriefTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
