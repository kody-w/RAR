---
name: "rar-cowork-cookbook-ppt-exec-develop-program-charter"
description: "Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_program_charter", "rar_sha256": "cb0b12992260c3fd396b51f84c0c246c38e42166065a8822299dcb72146b0d7b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_program_charter_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-program-charter:3a4eb7157c3603cf4fb1b23f9a89b1cbbfd6d01bc8660e7a6469dd50f71d8a52", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_program_charter`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_program_charter_agent.py` is
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

Develop program charter Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 cb0b12992260c3fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_program_charter_agent.py` first:

```bash
python3 ppt_exec_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_program_charter_agent.py   # or on stdin
python3 ppt_exec_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_program_charter',
    "version": '2.0.0',
    "display_name": 'Develop program charter Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85b16b7513b6b194',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDevelopProgramCharter(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProgramCharter'
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
    print(PptExecDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
