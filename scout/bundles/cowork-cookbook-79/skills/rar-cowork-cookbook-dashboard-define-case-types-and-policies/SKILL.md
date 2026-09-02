---
name: "rar-cowork-cookbook-dashboard-define-case-types-and-policies"
description: "Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_case_types_and_policies", "rar_sha256": "9429c2220aa903a7d673c781a3b489383258712f806a3d8d2e218e667caa7387", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_case_types_and_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-case-types-and-policies:c49616661e8b075a322eefea42607aa137c26fd55b1aaf2a3fd4de6c6c033e19", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_case_types_and_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_case_types_and_policies_agent.py` is
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

Define case types and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 9429c2220aa903a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_case_types_and_policies_agent.py` first:

```bash
python3 dashboard_define_case_types_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_case_types_and_policies_agent.py   # or on stdin
python3 dashboard_define_case_types_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define case types and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_case_types_and_policies',
    "version": '2.0.0',
    "display_name": 'Define case types and policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-case-types-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f4b4847bb7a0538',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-case-types-and-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-define-case-types-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineCaseTypesAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCaseTypesAndPolicies'
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
    print(DashboardDefineCaseTypesAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
