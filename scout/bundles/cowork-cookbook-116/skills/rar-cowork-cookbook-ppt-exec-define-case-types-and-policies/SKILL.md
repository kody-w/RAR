---
name: "rar-cowork-cookbook-ppt-exec-define-case-types-and-policies"
description: "Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_case_types_and_policies", "rar_sha256": "9e6cf285ed9b59ff43d78af82cd5afc1ca13cb92e7b53975a16b9073595d9ad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 9e6cf285ed9b59ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_case_types_and_policies_agent.py` first:

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
    "version": '2.0.0',
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
