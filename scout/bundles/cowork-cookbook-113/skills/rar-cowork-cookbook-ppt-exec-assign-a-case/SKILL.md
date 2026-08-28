---
name: "rar-cowork-cookbook-ppt-exec-assign-a-case"
description: "Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_a_case", "rar_sha256": "e811620566d06c5db875934630ddc9924f617152ca392dd2d7b7ec5ea903a0c1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assign_a_case`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assign_a_case_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 e811620566d06c5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_a_case_agent.py` first:

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
    "version": '2.0.1',
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
