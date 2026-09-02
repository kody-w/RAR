---
name: "rar-cowork-cookbook-ppt-exec-develop-leave-and-absence-policies"
description: "Generates an executive-ready PowerPoint deck on develop leave and absence policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies", "rar_sha256": "c48c7490f848b4f672284c85d9c2f4d5a5d343ea86fd89316705c3e4320cb57a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_leave_and_absence_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-leave-and-absence-policies:608b63b4758665e0eb0e25cefe1442af060be2b9dc249de009b37183a847910e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_leave_and_absence_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_leave_and_absence_policies_agent.py` is
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
