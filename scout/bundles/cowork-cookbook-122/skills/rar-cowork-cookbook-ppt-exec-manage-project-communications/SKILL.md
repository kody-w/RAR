---
name: "rar-cowork-cookbook-ppt-exec-manage-project-communications"
description: "Generates an executive-ready PowerPoint deck on manage project communications status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_project_communications", "rar_sha256": "da3c0d1ee0286efae1868986ac59eecedde3599668b49370e9b708678eb8064a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_project_communications_agent.py` and embedded as the fenced Python below (sha256 da3c0d1ee0286efa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_project_communications_agent.py` first:

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
    "version": '2.0.1',
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
