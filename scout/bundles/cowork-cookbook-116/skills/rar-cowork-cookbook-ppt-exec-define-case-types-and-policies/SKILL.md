---
name: "rar-cowork-cookbook-ppt-exec-define-case-types-and-policies"
description: "Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_case_types_and_policies", "rar_sha256": "83b172380a8291b4891c5e22aeb6d5cb6c6d47b2e40ebc27bd96131bb98fdb95", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_case_types_and_policies`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_case_types_and_policies_agent.py` and in the RCI capsule.

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

Define case types and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 83b172380a8291b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_case_types_and_policies_agent.py` first:

```bash
python3 ppt_exec_define_case_types_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_case_types_and_policies_agent.py   # or on stdin
python3 ppt_exec_define_case_types_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define case types and policies Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_case_types_and_policies',
    "version": '2.0.1',
    "display_name": 'Define case types and policies Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-case-types-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-case-types-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cbeb4b823c893f64',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-case-types-and-policies'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-case-types-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineCaseTypesAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineCaseTypesAndPolicies'
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
    print(PptExecDefineCaseTypesAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
