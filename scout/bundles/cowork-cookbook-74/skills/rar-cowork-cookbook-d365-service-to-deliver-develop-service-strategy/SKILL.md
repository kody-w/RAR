---
name: "rar-cowork-cookbook-d365-service-to-deliver-develop-service-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver_develop_service_strategy", "rar_sha256": "1cb78f50010b775cc38c258b7aa3f6b56d8fd816677418e31373d200358ed8ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_develop_service_strategy_agent.py` and embedded as the fenced Python below (sha256 1cb78f50010b775c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_develop_service_strategy_agent.py` first:

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
    "version": '2.0.0',
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
