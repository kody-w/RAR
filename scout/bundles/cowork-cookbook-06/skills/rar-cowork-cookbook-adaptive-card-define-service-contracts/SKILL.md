---
name: "rar-cowork-cookbook-adaptive-card-define-service-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_service_contracts", "rar_sha256": "ed6a8a4efb01505234e96f532c1a4e824bb25f9b0e32c2bbe47a8372b9f453b9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_service_contracts_agent.py` and embedded as the fenced Python below (sha256 ed6a8a4efb015052…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_service_contracts_agent.py` first:

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
    "version": '2.0.1',
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
