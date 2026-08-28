---
name: "rar-cowork-cookbook-dashboard-define-expense-policies"
description: "Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_expense_policies", "rar_sha256": "a05d0c1ca91ef917adcc61be2861464dd4e67a2b8bf8913cdfc8785fcfd6a925", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_expense_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_expense_policies_agent.py` and in the RCI capsule.

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

Define expense policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-expense-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 a05d0c1ca91ef917…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_expense_policies_agent.py` first:

```bash
python3 dashboard_define_expense_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_expense_policies_agent.py   # or on stdin
python3 dashboard_define_expense_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define expense policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-expense-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_expense_policies',
    "version": '2.0.1',
    "display_name": 'Define expense policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-expense-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-expense-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '00ece8a5f8d4265b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-expense-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-expense-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineExpensePolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineExpensePolicies'
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
    print(DashboardDefineExpensePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
