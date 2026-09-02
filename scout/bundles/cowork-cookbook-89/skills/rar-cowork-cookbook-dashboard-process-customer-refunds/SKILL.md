---
name: "rar-cowork-cookbook-dashboard-process-customer-refunds"
description: "Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_process_customer_refunds", "rar_sha256": "1605ecd4bbfcc389bd4edde4953e4b4ac4368893e7a032227f64d78f31986b3f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_process_customer_refunds_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-process-customer-refunds:5c86258f3f37e4cf767294f1accecb26c61f211c70c78695a442578436d78507", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_process_customer_refunds`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_process_customer_refunds_agent.py` is
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

Process customer refunds Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 1605ecd4bbfcc389…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_process_customer_refunds_agent.py` first:

```bash
python3 dashboard_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_process_customer_refunds_agent.py   # or on stdin
python3 dashboard_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_process_customer_refunds',
    "version": '2.0.0',
    "display_name": 'Process customer refunds Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for process customer refunds - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '78f9eb434a061b19',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardProcessCustomerRefunds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProcessCustomerRefunds'
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
    print(DashboardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
