---
name: "rar-cowork-cookbook-dashboard-define-customer-order-requirements"
description: "Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_customer_order_requirements", "rar_sha256": "33347d6b28ccb3c296b07b399f1eb9901b79d1fabb924470a842cd0bb52fed4f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_customer_order_requirements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-customer-order-requirements:8a04884ce95834dd7d6e8023f869c2d37ba6e413ad9c0056ea35bd71670c0b0a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_customer_order_requirements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_customer_order_requirements_agent.py` is
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

Define customer order requirements Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_customer_order_requirements_agent.py` and embedded as the fenced Python below (sha256 33347d6b28ccb3c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_customer_order_requirements_agent.py` first:

```bash
python3 dashboard_define_customer_order_requirements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_customer_order_requirements_agent.py   # or on stdin
python3 dashboard_define_customer_order_requirements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define customer order requirements Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_customer_order_requirements',
    "version": '2.0.0',
    "display_name": 'Define customer order requirements Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define customer order requirements - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-customer-order-requirements',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-customer-order-requirements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fcd89656acf904c0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/define-customer-order-requirements'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-define-customer-order-requirements', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDefineCustomerOrderRequirements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCustomerOrderRequirements'
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
    print(DashboardDefineCustomerOrderRequirements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
