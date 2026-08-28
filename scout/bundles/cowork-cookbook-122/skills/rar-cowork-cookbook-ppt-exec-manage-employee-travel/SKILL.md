---
name: "rar-cowork-cookbook-ppt-exec-manage-employee-travel"
description: "Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_employee_travel", "rar_sha256": "93161318e000b20f614b74330f89bc09d74c132c6ca0cbbeb0454a67fd2b8c61", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_employee_travel`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_employee_travel_agent.py` and in the RCI capsule.

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

Manage employee travel Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 93161318e000b20f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_employee_travel_agent.py` first:

```bash
python3 ppt_exec_manage_employee_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_employee_travel_agent.py   # or on stdin
python3 ppt_exec_manage_employee_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage employee travel Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_employee_travel',
    "version": '2.0.1',
    "display_name": 'Manage employee travel Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-manage-employee-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-employee-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'def8ddb6346250da',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-employee-travel'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-manage-employee-travel', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageEmployeeTravel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageEmployeeTravel'
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
    print(PptExecManageEmployeeTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
