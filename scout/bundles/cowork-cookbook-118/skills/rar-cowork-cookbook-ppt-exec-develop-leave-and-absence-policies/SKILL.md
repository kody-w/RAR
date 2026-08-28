---
name: "rar-cowork-cookbook-ppt-exec-develop-leave-and-absence-policies"
description: "Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies", "rar_sha256": "c48c7490f848b4f672284c85d9c2f4d5a5d343ea86fd89316705c3e4320cb57a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 c48c7490f848b4f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_leave_and_absence_policies_agent.py` first:

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
    "version": '2.0.0',
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
