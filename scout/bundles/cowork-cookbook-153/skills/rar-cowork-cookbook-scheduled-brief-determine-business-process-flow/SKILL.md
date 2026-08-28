---
name: "rar-cowork-cookbook-scheduled-brief-determine-business-process-flow"
description: "Schedulable morning-brief email summarizing determine business process flow for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_determine_business_process_flow", "rar_sha256": "010966bf7f3841ea34f10ff531b0fda980cadea221f1ceaf520531119f494dcf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_determine_business_process_flow_agent.py` and embedded as the fenced Python below (sha256 010966bf7f3841ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_determine_business_process_flow_agent.py` first:

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
    "version": '2.0.1',
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
