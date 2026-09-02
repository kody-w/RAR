---
name: "rar-cowork-cookbook-d365-service-to-deliver-develop-service-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop service strategy area (a level-2 subdomain of Service to deliver) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver_develop_service_strategy", "rar_sha256": "1cb78f50010b775cc38c258b7aa3f6b56d8fd816677418e31373d200358ed8ef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_service_to_deliver_develop_service_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-service-to-deliver-develop-service-strategy:30a490035206622f25a625d0090adc32aabeff110cab45d4f32c587fe80c3263", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_service_to_deliver_develop_service_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_service_to_deliver_develop_service_strategy_agent.py` is
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
