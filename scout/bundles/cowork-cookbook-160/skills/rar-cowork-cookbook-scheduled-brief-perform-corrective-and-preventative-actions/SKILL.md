---
name: "rar-cowork-cookbook-scheduled-brief-perform-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions", "rar_sha256": "3350c00ac324619f6da3d94ac93bc10a60f246ab127d2f47a855f563cd8ae09e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Perform corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 3350c00ac324619f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` first:

```bash
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py   # or on stdin
python3 scheduled_brief_perform_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective and preventative actions Scheduled Email Brief — Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions',
    "version": '2.0.1',
    "display_name": 'Perform corrective and preventative actions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-perform-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4386c40b04d7c5e9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/perform-corrective-and-preventative-actions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-perform-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPerformCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPerformCorrectiveAndPreventativeActions'
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
    print(ScheduledBriefPerformCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
