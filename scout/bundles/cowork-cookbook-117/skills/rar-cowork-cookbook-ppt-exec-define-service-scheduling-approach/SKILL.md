---
name: "rar-cowork-cookbook-ppt-exec-define-service-scheduling-approach"
description: "Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_service_scheduling_approach", "rar_sha256": "ed1bb67f659b88cf1efb2d59d2cf4872277094d8444cef7037bd0905bcb347a6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_service_scheduling_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-service-scheduling-approach:4c7eab4273d917e792b525fdc132251ecdac2ba1f42d3541f94ac115862812f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_service_scheduling_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_service_scheduling_approach_agent.py` is
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

Define service scheduling approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 ed1bb67f659b88cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_service_scheduling_approach_agent.py` first:

```bash
python3 ppt_exec_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_service_scheduling_approach_agent.py   # or on stdin
python3 ppt_exec_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_service_scheduling_approach',
    "version": '2.0.0',
    "display_name": 'Define service scheduling approach Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define service scheduling approach status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ec7fe53544a9a40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineServiceSchedulingApproach(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineServiceSchedulingApproach'
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
    print(PptExecDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
