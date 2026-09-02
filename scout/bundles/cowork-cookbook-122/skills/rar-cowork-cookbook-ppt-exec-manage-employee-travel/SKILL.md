---
name: "rar-cowork-cookbook-ppt-exec-manage-employee-travel"
description: "Generates an executive-ready PowerPoint deck on manage employee travel status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_employee_travel", "rar_sha256": "bc85ca854e64357d2e3eb60bab05962f10a6f941dba874082eb07e52f7a94a59", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_manage_employee_travel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-manage-employee-travel:8522b747e67ba516a2407d2f1bd3a8eaee9e5a1fd17d54da385922e358105c52", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_manage_employee_travel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_manage_employee_travel_agent.py` is
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
