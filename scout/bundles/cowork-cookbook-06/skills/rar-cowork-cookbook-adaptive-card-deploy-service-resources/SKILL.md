---
name: "rar-cowork-cookbook-adaptive-card-deploy-service-resources"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_service_resources", "rar_sha256": "2f8ea7e99d6a23a2e637d10f2d058bd3d8b02ffc81dd70387bdc787624f1fee5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_deploy_service_resources`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_deploy_service_resources_agent.py` and in the RCI capsule.

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

Deploy service resources Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 2f8ea7e99d6a23a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_service_resources_agent.py` first:

```bash
python3 adaptive_card_deploy_service_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_deploy_service_resources_agent.py   # or on stdin
python3 adaptive_card_deploy_service_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy service resources Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_deploy_service_resources',
    "version": '2.0.0',
    "display_name": 'Deploy service resources Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-deploy-service-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-deploy-service-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68e6768fb608e5d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/deploy-service-resources'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-deploy-service-resources', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDeployServiceResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDeployServiceResources'
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
    print(AdaptiveCardDeployServiceResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
