---
name: "rar-cowork-cookbook-adaptive-card-define-service-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_service_contracts", "rar_sha256": "478b6d89b1cb22fe831bcf0ba19c9e14e87b6611b095d51b9fbf88cd03391d44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_service_contracts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_service_contracts_agent.py` and in the RCI capsule.

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

Define service contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 478b6d89b1cb22fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_service_contracts_agent.py` first:

```bash
python3 adaptive_card_define_service_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_service_contracts_agent.py   # or on stdin
python3 adaptive_card_define_service_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_service_contracts',
    "version": '2.0.0',
    "display_name": 'Define service contracts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-define-service-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-service-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2a540305e066e35d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-contracts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/adaptive-card-define-service-contracts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineServiceContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineServiceContracts'
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
    print(AdaptiveCardDefineServiceContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
