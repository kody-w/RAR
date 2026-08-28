---
name: "rar-cowork-cookbook-dashboard-define-case-types-and-policies"
description: "Produces a self-contained interactive HTML dashboard for define case types and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_case_types_and_policies", "rar_sha256": "ebfeac5ec64787f6f1a9d8c3db34dcb27120b43ddcea676a9f4632fe72d5c63e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 ebfeac5ec64787f6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_case_types_and_policies_agent.py` first:

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
    "version": '2.0.1',
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
