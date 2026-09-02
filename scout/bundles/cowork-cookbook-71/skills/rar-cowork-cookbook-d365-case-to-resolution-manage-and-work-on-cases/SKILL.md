---
name: "rar-cowork-cookbook-d365-case-to-resolution-manage-and-work-on-cases"
description: "A Dynamics 365 F&SCM expert scoped to the Manage and work on cases area (a level-2 subdomain of Case to resolution) - covers 17 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases", "rar_sha256": "1c40e41758aa86cc75829693710807e9ea86323e38086b629f5f99aa7b1936cb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_case_to_resolution_manage_and_work_on_cases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-case-to-resolution-manage-and-work-on-cases:5f69d02aab9d2c26989cdf8899ec26830f88b512d5d23b0bb5a27faf609318d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_case_to_resolution_manage_and_work_on_cases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_case_to_resolution_manage_and_work_on_cases_agent.py` is
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
