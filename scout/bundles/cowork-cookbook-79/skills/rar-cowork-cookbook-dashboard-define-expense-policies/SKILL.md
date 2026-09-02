---
name: "rar-cowork-cookbook-dashboard-define-expense-policies"
description: "Produces a self-contained interactive HTML dashboard for define expense policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_expense_policies", "rar_sha256": "fbfb3513eed11243fa15d412b4c9766f71495b8917d01eccacad77a5be90cfa6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_expense_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-expense-policies:2de72116e94be894436ed90978a3260212969eb88806a8b6ca998a75c10fb1d3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_expense_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_expense_policies_agent.py` is
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
