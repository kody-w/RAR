---
name: "rar-cowork-cookbook-ppt-exec-develop-program-charter"
description: "Generates an executive-ready PowerPoint deck on develop program charter status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_program_charter", "rar_sha256": "585a65cf2a682005dedd566abaffc6cdf181573436cc435f940adb0bf677a638", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 585a65cf2a682005…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_program_charter_agent.py` first:

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
    "version": '2.0.1',
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
