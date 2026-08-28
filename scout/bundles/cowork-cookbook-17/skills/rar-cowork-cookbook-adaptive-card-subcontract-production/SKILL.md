---
name: "rar-cowork-cookbook-adaptive-card-subcontract-production"
description: "Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_subcontract_production", "rar_sha256": "af78cc688ba5dbf235be34b74da4babc5e2a8b466d680f1af6c2f82fbe33c5e8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_subcontract_production`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_subcontract_production_agent.py` and in the RCI capsule.

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

Subcontract production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 af78cc688ba5dbf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_subcontract_production_agent.py` first:

```bash
python3 adaptive_card_subcontract_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_subcontract_production_agent.py   # or on stdin
python3 adaptive_card_subcontract_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Subcontract production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-subcontract-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_subcontract_production',
    "version": '2.0.1',
    "display_name": 'Subcontract production Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-subcontract-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-subcontract-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f75505b2fd3a03ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/subcontract-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-subcontract-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardSubcontractProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardSubcontractProduction'
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
    print(AdaptiveCardSubcontractProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
