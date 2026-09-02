---
name: "rar-cowork-cookbook-dashboard-develop-currency-policies"
description: "Produces a self-contained interactive HTML dashboard for develop currency policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_currency_policies", "rar_sha256": "3832242466ebbd49bbf14d930e63d3d31ade12c304d8fe17049829ae692e0cb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_currency_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-currency-policies:30d341c6bfaa279e4b60206b8676a4b50a61bf28aff126dd7932918a024c5664", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_currency_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_currency_policies_agent.py` is
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
