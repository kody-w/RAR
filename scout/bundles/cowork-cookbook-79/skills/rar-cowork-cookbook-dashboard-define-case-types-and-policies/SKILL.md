---
name: "rar-cowork-cookbook-dashboard-define-case-types-and-policies"
description: "Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_case_types_and_policies", "rar_sha256": "9429c2220aa903a7d673c781a3b489383258712f806a3d8d2e218e667caa7387", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_case_types_and_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_case_types_and_policies_agent.py` and in the RCI capsule.

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
