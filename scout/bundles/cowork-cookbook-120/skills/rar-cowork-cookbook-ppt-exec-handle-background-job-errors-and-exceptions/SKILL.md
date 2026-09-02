---
name: "rar-cowork-cookbook-ppt-exec-handle-background-job-errors-and-exceptions"
description: "Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions", "rar_sha256": "c938ecee0c0074d5fcbe472c560ff09f1ee8e9eaa7ab0780cd5568af7270224a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_handle_background_job_errors_and_exceptions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-handle-background-job-errors-and-exceptions:5c2801c478dd4aeace302ccd73ddc8fdb909858deef2acad736e8362a4753742", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` is
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

Handle background job errors and exceptions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 c938ecee0c0074d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` first:

```bash
python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py   # or on stdin
python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle background job errors and exceptions Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions',
    "version": '2.0.0',
    "display_name": 'Handle background job errors and exceptions Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-handle-background-job-errors-and-exceptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ceffb5529952b3cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/handle-background-job-errors-and-exceptions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-handle-background-job-errors-and-exceptions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecHandleBackgroundJobErrorsAndExceptions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecHandleBackgroundJobErrorsAndExceptions'
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
    print(PptExecHandleBackgroundJobErrorsAndExceptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
