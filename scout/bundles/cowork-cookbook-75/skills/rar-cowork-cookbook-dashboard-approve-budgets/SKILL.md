---
name: "rar-cowork-cookbook-dashboard-approve-budgets"
description: "Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_approve_budgets", "rar_sha256": "c1f22fc11f2c4a3d45a1dcc921e0eb80f25c858a0d1dc7e465484c67a9e9de5e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_approve_budgets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_approve_budgets_agent.py` and in the RCI capsule.

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

Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 c1f22fc11f2c4a3d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_approve_budgets_agent.py` first:

```bash
python3 dashboard_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_approve_budgets_agent.py   # or on stdin
python3 dashboard_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_approve_budgets',
    "version": '2.0.0',
    "display_name": 'Approve budgets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bb8ba26f7d41ca4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardApproveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardApproveBudgets'
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
    print(DashboardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
