---
name: "rar-cowork-cookbook-dashboard-develop-merchandise-and-assortment-plans"
description: "Produces a self-contained interactive HTML dashboard for develop merchandise and assortment plans - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans", "rar_sha256": "23f2b9c2ff11ec390d2a7e364ef5f1d07f665f95ddb1add31d653c7e70a78ea1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_merchandise_and_assortment_plans_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-merchandise-and-assortment-plans:7cbd08be26873f2441418152628a74b3f8c94893f5f08d90600278876adc44d3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_merchandise_and_assortment_plans`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_merchandise_and_assortment_plans_agent.py` is
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
