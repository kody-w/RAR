---
name: "rar-cowork-cookbook-scheduled-brief-verify-employment"
description: "Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_verify_employment", "rar_sha256": "8e8c253db35bc4f38d15b43ec1cb598bf2aeb930eb9dd989433eff00b5217d43", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_verify_employment`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_verify_employment_agent.py` and in the RCI capsule.

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

Verify employment Scheduled Email Brief — Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-verify-employment
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_verify_employment_agent.py` and embedded as the fenced Python below (sha256 8e8c253db35bc4f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_verify_employment_agent.py` first:

```bash
python3 scheduled_brief_verify_employment_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_verify_employment_agent.py   # or on stdin
python3 scheduled_brief_verify_employment_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Verify employment Scheduled Email Brief — Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-verify-employment
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_verify_employment',
    "version": '2.0.1',
    "display_name": 'Verify employment Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-verify-employment',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-verify-employment',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41823f8168c6f8c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/verify-employment'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-verify-employment', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefVerifyEmployment(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefVerifyEmployment'
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
    print(ScheduledBriefVerifyEmployment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
