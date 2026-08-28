---
name: "rar-cowork-cookbook-ppt-exec-measure-project-progress"
description: "Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_project_progress", "rar_sha256": "9f0b27b4ac5b9e0ce6762557269bfe4b6e4e1ec3009eccfe50609fe72a226bb0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_measure_project_progress`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_measure_project_progress_agent.py` and in the RCI capsule.

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

Measure project progress Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 9f0b27b4ac5b9e0c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_project_progress_agent.py` first:

```bash
python3 ppt_exec_measure_project_progress_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_measure_project_progress_agent.py   # or on stdin
python3 ppt_exec_measure_project_progress_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure project progress Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_measure_project_progress',
    "version": '2.0.1',
    "display_name": 'Measure project progress Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-measure-project-progress',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-measure-project-progress',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'de13a76a5a95821a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/measure-project-progress'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-measure-project-progress', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecMeasureProjectProgress(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMeasureProjectProgress'
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
    print(PptExecMeasureProjectProgress().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
