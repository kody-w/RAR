---
name: "rar-cowork-cookbook-ppt-exec-measure-project-progress"
description: "Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_project_progress", "rar_sha256": "1394049db3787e0363ca0e39068681273b44e8c3f39f6a5583cd14132045d8ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_measure_project_progress_agent.py` and embedded as the fenced Python below (sha256 1394049db3787e03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_measure_project_progress_agent.py` first:

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
    "version": '2.0.0',
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
