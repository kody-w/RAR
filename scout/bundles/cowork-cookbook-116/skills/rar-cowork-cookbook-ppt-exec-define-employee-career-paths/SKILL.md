---
name: "rar-cowork-cookbook-ppt-exec-define-employee-career-paths"
description: "Generates an executive-ready PowerPoint deck on define employee career paths status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_employee_career_paths", "rar_sha256": "4f59c8cca92ff2f498702fb96ef0a65cd149704af8101735808524cacf47c363", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_employee_career_paths_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-employee-career-paths:02a974410ad37b37ab7c3d5031d4e7b9ecfae502f5046690ce3044c932a94678", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_employee_career_paths`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_employee_career_paths_agent.py` is
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
