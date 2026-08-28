---
name: "rar-cowork-cookbook-ppt-exec-define-employee-career-paths"
description: "Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_employee_career_paths", "rar_sha256": "4f59c8cca92ff2f498702fb96ef0a65cd149704af8101735808524cacf47c363", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_employee_career_paths`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_employee_career_paths_agent.py` and in the RCI capsule.

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

Define employee career paths Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 4f59c8cca92ff2f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_employee_career_paths_agent.py` first:

```bash
python3 ppt_exec_define_employee_career_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_employee_career_paths_agent.py   # or on stdin
python3 ppt_exec_define_employee_career_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define employee career paths Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_employee_career_paths',
    "version": '2.0.0',
    "display_name": 'Define employee career paths Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-employee-career-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f826fb140594ffdc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-employee-career-paths'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-employee-career-paths', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineEmployeeCareerPaths(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineEmployeeCareerPaths'
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
    print(PptExecDefineEmployeeCareerPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
