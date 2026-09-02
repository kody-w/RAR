---
name: "rar-cowork-cookbook-adaptive-card-deploy-service-resources"
description: "Produces a reusable Adaptive Card JSON snapshot of deploy service resources status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_deploy_service_resources", "rar_sha256": "2f8ea7e99d6a23a2e637d10f2d058bd3d8b02ffc81dd70387bdc787624f1fee5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_deploy_service_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-deploy-service-resources:a1f570798d6abbb07adcf51870e32266032e277e59c248945495218d3c11ca46", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_deploy_service_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_deploy_service_resources_agent.py` is
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
