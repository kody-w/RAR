---
name: "rar-cowork-cookbook-adaptive-card-subcontract-production"
description: "Produces a reusable Adaptive Card JSON snapshot of subcontract production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_subcontract_production", "rar_sha256": "68fb1529ce4397d4668abe8320ced359ece56aa6970d2fb0ec09f78e3dcd1cd3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_subcontract_production_agent.py` and embedded as the fenced Python below (sha256 68fb1529ce4397d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_subcontract_production_agent.py` first:

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
    "version": '2.0.0',
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
