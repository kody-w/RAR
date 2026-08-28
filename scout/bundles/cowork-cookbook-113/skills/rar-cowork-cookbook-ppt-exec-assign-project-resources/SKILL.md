---
name: "rar-cowork-cookbook-ppt-exec-assign-project-resources"
description: "Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_project_resources", "rar_sha256": "9e9702117d7d8cc58e1a62d6ed817e44d25b36c3224fe262f6efb9702810b517", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assign_project_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assign_project_resources_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 9e9702117d7d8cc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_project_resources_agent.py` first:

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
    "version": '2.0.1',
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
