---
name: "rar-cowork-cookbook-ppt-exec-define-employee-career-paths"
description: "Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_employee_career_paths", "rar_sha256": "eb4659f310a3b4df58309b4eca7b430f41ff9183466d1a4a04a8e2f372454668", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 eb4659f310a3b4df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_employee_career_paths_agent.py` first:

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
    "version": '2.0.1',
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
