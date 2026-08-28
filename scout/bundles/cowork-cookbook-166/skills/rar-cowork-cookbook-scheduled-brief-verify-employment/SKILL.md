---
name: "rar-cowork-cookbook-scheduled-brief-verify-employment"
description: "Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_verify_employment", "rar_sha256": "e780eb8d83643d392024f76c74d3b835ecc401fa66806816748cce8b431abd80", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_verify_employment_agent.py` and embedded as the fenced Python below (sha256 e780eb8d83643d39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_verify_employment_agent.py` first:

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
    "version": '2.0.0',
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
