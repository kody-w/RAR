---
name: "rar-cowork-cookbook-dashboard-develop-order-management-policies"
description: "Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_order_management_policies", "rar_sha256": "0d844b9151934b1dbc21b50f2667a4ed1660fcdc8673f7244152d6c59b49259c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_order_management_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_order_management_policies_agent.py` and in the RCI capsule.

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

Develop order management policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 0d844b9151934b1d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_order_management_policies_agent.py` first:

```bash
python3 dashboard_develop_order_management_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_order_management_policies_agent.py   # or on stdin
python3 dashboard_develop_order_management_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop order management policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_order_management_policies',
    "version": '2.0.1',
    "display_name": 'Develop order management policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-develop-order-management-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-order-management-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bd3040feac9114e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-order-management-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-develop-order-management-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopOrderManagementPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopOrderManagementPolicies'
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
    print(DashboardDevelopOrderManagementPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
