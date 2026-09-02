---
name: "rar-cowork-cookbook-ppt-exec-assign-project-resources"
description: "Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_project_resources", "rar_sha256": "8dfe5d51f3348709caf34a20e325a1d91f543b7a77c67dce9ad17734187efc7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_assign_project_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-assign-project-resources:b9dd73c818fe1af9548e9b032a1f48517a7cad5191da09e8833440ead4207636", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_assign_project_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_assign_project_resources_agent.py` is
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

Assign project resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 8dfe5d51f3348709…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_project_resources_agent.py` first:

```bash
python3 ppt_exec_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assign_project_resources_agent.py   # or on stdin
python3 ppt_exec_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assign_project_resources',
    "version": '2.0.0',
    "display_name": 'Assign project resources Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9ebe5872353b4ef4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecAssignProjectResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssignProjectResources'
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
    print(PptExecAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
