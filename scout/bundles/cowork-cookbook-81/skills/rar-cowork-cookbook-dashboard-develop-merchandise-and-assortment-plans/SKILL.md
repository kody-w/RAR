---
name: "rar-cowork-cookbook-dashboard-develop-merchandise-and-assortment-plans"
description: "Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans", "rar_sha256": "1b9a8435aeca4a2c0ba2e3791c444038815852b0e2a3731b5d968630ec0b73b0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_merchandise_and_assortment_plans_agent.py` and in the RCI capsule.

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

Develop merchandise and assortment plans Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 1b9a8435aeca4a2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_merchandise_and_assortment_plans_agent.py` first:

```bash
python3 dashboard_develop_merchandise_and_assortment_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_merchandise_and_assortment_plans_agent.py   # or on stdin
python3 dashboard_develop_merchandise_and_assortment_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop merchandise and assortment plans Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans',
    "version": '2.0.1',
    "display_name": 'Develop merchandise and assortment plans Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-merchandise-and-assortment-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-merchandise-and-assortment-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32070af110876bcc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-merchandise-and-assortment-plans'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-develop-merchandise-and-assortment-plans', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopMerchandiseAndAssortmentPlans(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopMerchandiseAndAssortmentPlans'
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
    print(DashboardDevelopMerchandiseAndAssortmentPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
