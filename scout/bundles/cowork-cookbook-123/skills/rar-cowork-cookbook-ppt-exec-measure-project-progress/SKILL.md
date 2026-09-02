---
name: "rar-cowork-cookbook-ppt-exec-measure-project-progress"
description: "Generates an executive-ready PowerPoint deck on measure project progress status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_measure_project_progress", "rar_sha256": "1394049db3787e0363ca0e39068681273b44e8c3f39f6a5583cd14132045d8ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_measure_project_progress_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-measure-project-progress:1610bcbe8fefc070cb4b2ee8502a34699f8cb951d31ffd9d7367374295493573", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_measure_project_progress`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_measure_project_progress_agent.py` is
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
