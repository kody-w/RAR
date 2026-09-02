---
name: "rar-cowork-cookbook-dashboard-develop-a-business-continuity-plan"
description: "Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_a_business_continuity_plan", "rar_sha256": "7d98d9fcdb6e63560835a845f960fac665939c7a36b03f6180bf60ae2e5de9d1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_develop_a_business_continuity_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-develop-a-business-continuity-plan:801a62422ceeb0754ccb798216c2ebc303db631a0f552cb44ed18ee317de80b0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_develop_a_business_continuity_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_develop_a_business_continuity_plan_agent.py` is
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

Develop a business continuity plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_a_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 7d98d9fcdb6e6356…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_a_business_continuity_plan_agent.py` first:

```bash
python3 dashboard_develop_a_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_a_business_continuity_plan_agent.py   # or on stdin
python3 dashboard_develop_a_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop a business continuity plan Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_a_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Develop a business continuity plan Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for develop a business continuity plan - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-a-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-a-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ddb9bc8bffd5769',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/develop-a-business-continuity-plan'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-develop-a-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDevelopABusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopABusinessContinuityPlan'
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
    print(DashboardDevelopABusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
