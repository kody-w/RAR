---
name: "rar-cowork-cookbook-ppt-exec-develop-leave-and-absence-policies"
description: "Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies", "rar_sha256": "782fd3762a5d4008a7ab46386d50bc21451b7b0b9cf8fdffce79b30553ee3086", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_leave_and_absence_policies_agent.py` and in the RCI capsule.

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

Develop leave and absence policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 782fd3762a5d4008…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_leave_and_absence_policies_agent.py` first:

```bash
python3 ppt_exec_develop_leave_and_absence_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_leave_and_absence_policies_agent.py   # or on stdin
python3 ppt_exec_develop_leave_and_absence_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop leave and absence policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies',
    "version": '2.0.1',
    "display_name": 'Develop leave and absence policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-develop-leave-and-absence-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-leave-and-absence-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00a61c6fc28a54f0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/develop-leave-and-absence-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-develop-leave-and-absence-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopLeaveAndAbsencePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopLeaveAndAbsencePolicies'
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
    print(PptExecDevelopLeaveAndAbsencePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
