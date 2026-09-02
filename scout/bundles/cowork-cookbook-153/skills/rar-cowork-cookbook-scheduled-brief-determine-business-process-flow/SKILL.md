---
name: "rar-cowork-cookbook-scheduled-brief-determine-business-process-flow"
description: "Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_determine_business_process_flow", "rar_sha256": "b19b3f06d49b7b1325f2e0a1a8d79414cdcda9510412f6a2aa00a8308bbd1126", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_determine_business_process_flow_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-determine-business-process-flow:96d2d6a9d9984ad81f2c2c0ed195b23a57962d96a33555ed8c70fe15e6f7f2be", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_determine_business_process_flow`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_determine_business_process_flow_agent.py` is
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

Determine business process flow Scheduled Email Brief — Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 b19b3f06d49b7b13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_determine_business_process_flow_agent.py` first:

```bash
python3 scheduled_brief_determine_business_process_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_determine_business_process_flow_agent.py   # or on stdin
python3 scheduled_brief_determine_business_process_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Determine business process flow Scheduled Email Brief — Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_determine_business_process_flow',
    "version": '2.0.0',
    "display_name": 'Determine business process flow Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-determine-business-process-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-determine-business-process-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4553f8f844c66796',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/determine-business-process-flow'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-determine-business-process-flow', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDetermineBusinessProcessFlow(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDetermineBusinessProcessFlow'
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
    print(ScheduledBriefDetermineBusinessProcessFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
