---
name: "rar-cowork-cookbook-scheduled-brief-perform-corrective-and-preventative-actions"
description: "Schedulable morning-brief email summarizing perform corrective and preventative actions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_perform_corrective_and_preventative_actions", "rar_sha256": "9b56a91589535a69492388e28d3b366e4168e90e7a3f512e93cfa61529151143", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 9b56a91589535a69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_perform_corrective_and_preventative_actions_agent.py` first:

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
    "version": '2.0.0',
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
