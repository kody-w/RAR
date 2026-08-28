---
name: "rar-cowork-cookbook-d365-case-to-resolution-manage-and-work-on-cases"
description: "A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases", "rar_sha256": "b023f705c5fd896d7e42dc31af6f2118a2f416b4c05d9556f872d387c40d41cc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_manage_and_work_on_cases_agent.py` and in the RCI capsule.

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

D365 Manage and work on cases Expert — A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_manage_and_work_on_cases_agent.py` and embedded as the fenced Python below (sha256 b023f705c5fd896d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_manage_and_work_on_cases_agent.py` first:

```bash
python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py   # or on stdin
python3 d365_case_to_resolution_manage_and_work_on_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage and work on cases Expert — A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases',
    "version": '2.0.1',
    "display_name": 'D365 Manage and work on cases Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-case-to-resolution-manage-and-work-on-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution-manage-and-work-on-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fd04f6600b157185',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution-manage-and-work-on-cases', 'uses_skills': {'custom': ['d365-case-to-resolution-manage-and-work-on-cases'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365CaseToResolutionManageAndWorkOnCases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolutionManageAndWorkOnCases'
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
    print(D365CaseToResolutionManageAndWorkOnCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
