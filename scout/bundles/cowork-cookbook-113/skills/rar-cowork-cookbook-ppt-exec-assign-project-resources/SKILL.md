---
name: "rar-cowork-cookbook-ppt-exec-assign-project-resources"
description: "Generates an executive-ready PowerPoint deck on assign project resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_project_resources", "rar_sha256": "8dfe5d51f3348709caf34a20e325a1d91f543b7a77c67dce9ad17734187efc7d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
