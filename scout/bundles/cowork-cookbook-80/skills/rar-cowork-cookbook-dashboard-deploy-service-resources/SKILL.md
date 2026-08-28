---
name: "rar-cowork-cookbook-dashboard-deploy-service-resources"
description: "Produces a self-contained interactive HTML dashboard for deploy service resources - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_service_resources", "rar_sha256": "7749d32e974b938af6459f33d0931f24d3089707ebf934e0489d9419439ccedc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 7749d32e974b938a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_service_resources_agent.py` first:

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
    "version": '2.0.1',
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
