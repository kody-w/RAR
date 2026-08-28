---
name: "rar-cowork-cookbook-dashboard-develop-merchandise-and-assortment-plans"
description: "Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans", "rar_sha256": "23f2b9c2ff11ec390d2a7e364ef5f1d07f665f95ddb1add31d653c7e70a78ea1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_merchandise_and_assortment_plans_agent.py` and embedded as the fenced Python below (sha256 23f2b9c2ff11ec39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_merchandise_and_assortment_plans_agent.py` first:

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
    "version": '2.0.0',
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
