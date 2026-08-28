---
name: "rar-cowork-cookbook-dashboard-develop-currency-policies"
description: "Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_currency_policies", "rar_sha256": "30c22d420a0af79afb20f7502aad8868efece4a069f6674127daa46c60260f5e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_currency_policies_agent.py` and embedded as the fenced Python below (sha256 30c22d420a0af79a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_currency_policies_agent.py` first:

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
    "version": '2.0.1',
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
