---
name: "rar-cowork-cookbook-d365-case-to-resolution-manage-and-work-on-cases"
description: "A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases", "rar_sha256": "1c40e41758aa86cc75829693710807e9ea86323e38086b629f5f99aa7b1936cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_manage_and_work_on_cases_agent.py` and embedded as the fenced Python below (sha256 1c40e41758aa86cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_manage_and_work_on_cases_agent.py` first:

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
    "version": '2.0.0',
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
