---
name: "rar-cowork-cookbook-dashboard-define-expense-policies"
description: "Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_expense_policies", "rar_sha256": "fbfb3513eed11243fa15d412b4c9766f71495b8917d01eccacad77a5be90cfa6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_expense_policies_agent.py` and embedded as the fenced Python below (sha256 fbfb3513eed11243…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_expense_policies_agent.py` first:

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
    "version": '2.0.0',
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
