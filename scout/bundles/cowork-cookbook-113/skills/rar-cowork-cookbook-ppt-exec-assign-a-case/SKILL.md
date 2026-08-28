---
name: "rar-cowork-cookbook-ppt-exec-assign-a-case"
description: "Generates an executive-ready PowerPoint deck on assign a case status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_a_case", "rar_sha256": "689ad6a6eebeb0ee24b8bb4271cc1e415e19bda325dc3dd69571a140b5b59a62", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
