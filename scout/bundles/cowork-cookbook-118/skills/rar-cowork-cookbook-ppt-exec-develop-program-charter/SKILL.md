---
name: "rar-cowork-cookbook-ppt-exec-develop-program-charter"
description: "Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_program_charter", "rar_sha256": "cb0b12992260c3fd396b51f84c0c246c38e42166065a8822299dcb72146b0d7b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_program_charter`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_program_charter_agent.py` and in the RCI capsule.

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
