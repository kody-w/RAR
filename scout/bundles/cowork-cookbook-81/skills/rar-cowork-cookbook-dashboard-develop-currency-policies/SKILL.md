---
name: "rar-cowork-cookbook-dashboard-develop-currency-policies"
description: "Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_currency_policies", "rar_sha256": "3832242466ebbd49bbf14d930e63d3d31ade12c304d8fe17049829ae692e0cb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_currency_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_currency_policies_agent.py` and in the RCI capsule.

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

Develop currency policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-currency-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 3832242466ebbd49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_currency_policies_agent.py` first:

```bash
python3 dashboard_develop_currency_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_currency_policies_agent.py   # or on stdin
python3 dashboard_develop_currency_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop currency policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-currency-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_currency_policies',
    "version": '2.0.0',
    "display_name": 'Develop currency policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-develop-currency-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-currency-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '35ff7dbf412180a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-currency-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-develop-currency-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardDevelopCurrencyPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopCurrencyPolicies'
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
    print(DashboardDevelopCurrencyPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
