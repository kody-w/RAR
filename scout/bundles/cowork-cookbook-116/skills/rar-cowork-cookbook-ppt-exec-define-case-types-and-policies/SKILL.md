---
name: "rar-cowork-cookbook-ppt-exec-define-case-types-and-policies"
description: "Generates an executive-ready PowerPoint deck on define case types and policies status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_case_types_and_policies", "rar_sha256": "9e6cf285ed9b59ff43d78af82cd5afc1ca13cb92e7b53975a16b9073595d9ad8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_case_types_and_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-case-types-and-policies:6565087c5f74dd964eb1348dda710d37fcfb5b94c8acbcb7ca48abbfac8ad87a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_case_types_and_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_case_types_and_policies_agent.py` is
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
