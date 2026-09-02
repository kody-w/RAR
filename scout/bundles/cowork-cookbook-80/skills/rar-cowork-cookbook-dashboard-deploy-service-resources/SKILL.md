---
name: "rar-cowork-cookbook-dashboard-deploy-service-resources"
description: "Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_service_resources", "rar_sha256": "07af1aea86ff49644d6a24d9acc658a379e27770d8c0327022b373bdef5c15a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_deploy_service_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-deploy-service-resources:d40dce17920c9ada154545954cbe71ca4241fb9982e2b8a96c2996dfe683e11a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_deploy_service_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_deploy_service_resources_agent.py` is
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

Deploy service resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-service-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 07af1aea86ff4964…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_service_resources_agent.py` first:

```bash
python3 dashboard_deploy_service_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_deploy_service_resources_agent.py   # or on stdin
python3 dashboard_deploy_service_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy service resources Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-service-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_deploy_service_resources',
    "version": '2.0.0',
    "display_name": 'Deploy service resources Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-deploy-service-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-deploy-service-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '362effaf2c23e5cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/deploy-service-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-deploy-service-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDeployServiceResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDeployServiceResources'
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
    print(DashboardDeployServiceResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
