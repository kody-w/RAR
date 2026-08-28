---
name: "rar-cowork-cookbook-adaptive-card-deploy-service-resources"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_service_resources", "rar_sha256": "720c89500ad31e47726151dfc39be100d918a247a44a98a9bbc9421cbc16731d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 720c89500ad31e47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_deploy_service_resources_agent.py` first:

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
    "version": '2.0.1',
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
