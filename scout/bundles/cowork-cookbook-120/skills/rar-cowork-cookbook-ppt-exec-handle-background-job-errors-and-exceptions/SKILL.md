---
name: "rar-cowork-cookbook-ppt-exec-handle-background-job-errors-and-exceptions"
description: "Generates an executive-ready PowerPoint deck on handle background job errors and exceptions status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions", "rar_sha256": "e240b0efadf2ae85745e07884e9b72f256f0e842c334c9a8969f4d9cf763cee2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 e240b0efadf2ae85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` first:

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
    "version": '2.0.1',
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
