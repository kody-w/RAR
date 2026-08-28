---
name: "rar-cowork-cookbook-ppt-exec-manage-employee-travel"
description: "Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_employee_travel", "rar_sha256": "bc85ca854e64357d2e3eb60bab05962f10a6f941dba874082eb07e52f7a94a59", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 bc85ca854e64357d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_employee_travel_agent.py` first:

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
    "version": '2.0.0',
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
