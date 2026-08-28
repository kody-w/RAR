---
name: "rar-cowork-cookbook-d365-service-to-deliver-develop-service-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver_develop_service_strategy", "rar_sha256": "b106cd02c707e51a5a6524e79f8f8b3c8a3c3cbd8a2d9e18e94d1f319313a643", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_service_to_deliver_develop_service_strategy`. The original RAPP
agent is preserved byte-for-byte in `d365_service_to_deliver_develop_service_strategy_agent.py` and in the RCI capsule.

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

D365 Develop service strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_develop_service_strategy_agent.py` and embedded as the fenced Python below (sha256 b106cd02c707e51a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_develop_service_strategy_agent.py` first:

```bash
python3 d365_service_to_deliver_develop_service_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_develop_service_strategy_agent.py   # or on stdin
python3 d365_service_to_deliver_develop_service_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop service strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver_develop_service_strategy',
    "version": '2.0.1',
    "display_name": 'D365 Develop service strategy Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-service-to-deliver-develop-service-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85834d26ade9f4b4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver-develop-service-strategy', 'uses_skills': {'custom': ['d365-service-to-deliver-develop-service-strategy'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ServiceToDeliverDevelopServiceStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliverDevelopServiceStrategy'
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
    print(D365ServiceToDeliverDevelopServiceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
