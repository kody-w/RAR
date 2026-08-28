---
name: "rar-cowork-cookbook-scheduled-brief-determine-business-process-flow"
description: "Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_determine_business_process_flow", "rar_sha256": "b19b3f06d49b7b1325f2e0a1a8d79414cdcda9510412f6a2aa00a8308bbd1126", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_determine_business_process_flow`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_determine_business_process_flow_agent.py` and in the RCI capsule.

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
