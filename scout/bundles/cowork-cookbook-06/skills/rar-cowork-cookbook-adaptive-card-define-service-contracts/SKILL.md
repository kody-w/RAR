---
name: "rar-cowork-cookbook-adaptive-card-define-service-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of define service contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_service_contracts", "rar_sha256": "478b6d89b1cb22fe831bcf0ba19c9e14e87b6611b095d51b9fbf88cd03391d44", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_define_service_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-define-service-contracts:b0e95be70b4caf05e21b1a5906f7ac6153ad8f0ded9bd5cf305d6de27df3ca26", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_define_service_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_define_service_contracts_agent.py` is
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
