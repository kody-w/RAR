---
name: "rar-cowork-cookbook-dashboard-develop-order-management-policies"
description: "Produces a self-contained interactive HTML dashboard for develop order management policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_order_management_policies", "rar_sha256": "1d450ec284c842e9b180cec43bcee81190759c433ef5453f0ac544f4b193db35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_order_management_policies_agent.py` and embedded as the fenced Python below (sha256 1d450ec284c842e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_order_management_policies_agent.py` first:

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
    "version": '2.0.0',
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
