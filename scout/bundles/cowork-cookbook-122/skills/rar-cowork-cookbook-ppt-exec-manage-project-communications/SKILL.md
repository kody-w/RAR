---
name: "rar-cowork-cookbook-ppt-exec-manage-project-communications"
description: "Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_project_communications", "rar_sha256": "4fe3d419c55626916d21d37421323bf8c1f0e54ea9134c99f0fc2dced26d1b73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_project_communications`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_project_communications_agent.py` and in the RCI capsule.

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

Manage project communications Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 4fe3d419c5562691…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_project_communications_agent.py` first:

```bash
python3 ppt_exec_manage_project_communications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_project_communications_agent.py   # or on stdin
python3 ppt_exec_manage_project_communications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project communications Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_project_communications',
    "version": '2.0.0',
    "display_name": 'Manage project communications Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-manage-project-communications',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-project-communications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '048444c389f30da8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-communications'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-manage-project-communications', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageProjectCommunications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageProjectCommunications'
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
    print(PptExecManageProjectCommunications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
