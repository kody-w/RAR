---
name: "rar-cowork-cookbook-ppt-exec-assign-a-case"
description: "Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_a_case", "rar_sha256": "689ad6a6eebeb0ee24b8bb4271cc1e415e19bda325dc3dd69571a140b5b59a62", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_assign_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-assign-a-case:875e8f135b6aab1cb8d7eab549cef8cb8f72ca8a0a3a99ee4c7ffe7affadb967", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_assign_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_assign_a_case_agent.py` is
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

Assign a case Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 689ad6a6eebeb0ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_a_case_agent.py` first:

```bash
python3 ppt_exec_assign_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assign_a_case_agent.py   # or on stdin
python3 ppt_exec_assign_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign a case Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assign_a_case',
    "version": '2.0.0',
    "display_name": 'Assign a case Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-assign-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assign-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '258015f5354a1703',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/assign-a-case'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-assign-a-case', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecAssignACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssignACase'
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
    print(PptExecAssignACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
