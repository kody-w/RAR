---
name: "rar-cowork-cookbook-adaptive-card-consolidate-requisitions"
description: "Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_consolidate_requisitions", "rar_sha256": "592d0e1eb1fb0a2a2b5cfc2cfe4f4a39741f8880b38239ba61da5cb8b7276fb1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_consolidate_requisitions`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_consolidate_requisitions_agent.py` and in the RCI capsule.

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

Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_consolidate_requisitions_agent.py` and embedded as the fenced Python below (sha256 592d0e1eb1fb0a2a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_consolidate_requisitions_agent.py` first:

```bash
python3 adaptive_card_consolidate_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_consolidate_requisitions_agent.py   # or on stdin
python3 adaptive_card_consolidate_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate requisitions Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_consolidate_requisitions',
    "version": '2.0.1',
    "display_name": 'Consolidate requisitions Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of consolidate requisitions status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-consolidate-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-consolidate-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd39bbfe80f8d0c24',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/consolidate-requisitions'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/adaptive-card-consolidate-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardConsolidateRequisitions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardConsolidateRequisitions'
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
    print(AdaptiveCardConsolidateRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
