---
name: "rar-cowork-cookbook-adaptive-card-define-routing-rules"
description: "Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_routing_rules", "rar_sha256": "a6dde59e197c7c94c5fdbb8ce2b9d2326129b3c1e5b3cc0e9a7f3a02c7887f6e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_routing_rules`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_routing_rules_agent.py` and in the RCI capsule.

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

Define routing rules Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_routing_rules_agent.py` and embedded as the fenced Python below (sha256 a6dde59e197c7c94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_routing_rules_agent.py` first:

```bash
python3 adaptive_card_define_routing_rules_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_routing_rules_agent.py   # or on stdin
python3 adaptive_card_define_routing_rules_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define routing rules Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_routing_rules',
    "version": '2.0.1',
    "display_name": 'Define routing rules Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define routing rules status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-define-routing-rules',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-routing-rules',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c722f1d95b5e5ca5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-routing-rules'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-define-routing-rules', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardDefineRoutingRules(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineRoutingRules'
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
    print(AdaptiveCardDefineRoutingRules().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
