---
name: "rar-cowork-cookbook-scheduled-brief-verify-employment"
description: "Schedulable morning-brief email summarizing verify employment for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_verify_employment", "rar_sha256": "e780eb8d83643d392024f76c74d3b835ecc401fa66806816748cce8b431abd80", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_verify_employment_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-verify-employment:d7057760b552024aef8df43a08f5ac0f08945cb6f5eadb6143a6bf41929a008f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_verify_employment`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_verify_employment_agent.py` is
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
