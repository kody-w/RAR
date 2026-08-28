---
name: "rar-cowork-cookbook-dashboard-deploy-service-resources"
description: "Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_service_resources", "rar_sha256": "07af1aea86ff49644d6a24d9acc658a379e27770d8c0327022b373bdef5c15a2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_deploy_service_resources`. The original RAPP
agent is preserved byte-for-byte in `dashboard_deploy_service_resources_agent.py` and in the RCI capsule.

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
