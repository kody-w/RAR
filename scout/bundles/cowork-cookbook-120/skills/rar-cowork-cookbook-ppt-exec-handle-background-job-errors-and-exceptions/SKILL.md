---
name: "rar-cowork-cookbook-ppt-exec-handle-background-job-errors-and-exceptions"
description: "Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions", "rar_sha256": "c938ecee0c0074d5fcbe472c560ff09f1ee8e9eaa7ab0780cd5568af7270224a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` and in the RCI capsule.

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
